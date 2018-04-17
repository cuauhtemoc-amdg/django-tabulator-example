from rest_framework import serializers
from contacts.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id',
                  'title',
                  'first_name', 'last_name', 'nick_name',
                   'company',
                  'email')
