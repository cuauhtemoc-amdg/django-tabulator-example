from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from contacts.models import Contacts
from contacts.serializers import ContactsSerializer


# -----------------------------------------------------------------------------
# Main Default View
# -----------------------------------------------------------------------------
def index(request):
    return render(request, 'contacts/index.html')


# -----------------------------------------------------------------------------
# ContactList View
# -----------------------------------------------------------------------------
class ContactsList(APIView):
    """
    List all contacts, or create a new contact.
    """

    def get(self, request, format=None):
        contacts = Contacts.objects.all()
        serializer = ContactsSerializer(contacts, many=True)
        ret_val = Response(serializer.data)
        return ret_val

    def post(self, request, format=None):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ContactsDetail(APIView):

    def get_object(self, pk):
        try:
            return Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactsSerializer(contact, data=request.data)
        serializer.is_valid()
        str_sz = repr(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        err_str = serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
