from rest_framework import serializers
from contacts.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id',
                  'first_name', 'last_name', 'nick_name',
                  'title', 'company', 'job_title',
                  'email', 'notes')
