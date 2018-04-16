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
