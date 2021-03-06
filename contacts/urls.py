from django.urls import path
from django.urls import re_path
from contacts.views import index
from contacts.views import ContactsList
from contacts.views import ContactsDetail


urlpatterns = [
    path('', index, name='index'),
    re_path('api/?$', ContactsList.as_view(), name='list'),
    re_path('api/(?P<pk>[0-9]+)/?$', ContactsDetail.as_view(), name='detail'),
]
