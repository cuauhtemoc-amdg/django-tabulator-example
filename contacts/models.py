from django.db import models


# -----------------------------------------------------------------------------
# Contacts Address
# -----------------------------------------------------------------------------
class Contacts(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    nick_name = models.CharField(max_length=40)
    title = models.CharField(max_length=10)

    company = models.CharField(max_length=40)
    job_title = models.CharField(max_length=40)
    email = models.EmailField()

    notes = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
