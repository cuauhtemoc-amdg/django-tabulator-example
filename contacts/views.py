from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# -----------------------------------------------------------------------------
# Main Default View
# -----------------------------------------------------------------------------
def index(request):
    return render(request, 'contacts/index.html')
