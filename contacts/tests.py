from django.test import TestCase
from contacts.models import Contacts

# Create your tests here.
class ContactsTests(TestCase):
    def add_contacts(self):
        """
        Add item to contacts table.
        """
        c_mgr = Contacts.objects
        c_mgr.all().delete()
        c1 = Contacts()
        c1.first_name = "Oli"
        c1.last_name = "Folkerd"
        c1.nick_name = "Oli"
        c1.title = "Mr."
        c1.company = "Tabulator"
        c1.job_title = "Head of Development"
        c1.email = "test@github.com"
        c1.notes = "This is a test note"
        c1.save()
        cnt = c_mgr.count()
        self.assertTrue(cnt==1, 'Record not created')


