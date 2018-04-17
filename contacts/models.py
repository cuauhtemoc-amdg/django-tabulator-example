from django.db import models


# -----------------------------------------------------------------------------
# Contacts Address
# -----------------------------------------------------------------------------
class Contacts(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    nick_name = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=10, blank=True)

    company = models.CharField(max_length=40, blank=True)
    #job_title = models.CharField(max_length=40,default='x')
    email = models.EmailField(blank=True)

    #notes = models.TextField(null=True, blank=True, default='none')

    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name