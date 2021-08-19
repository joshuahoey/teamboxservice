from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

class ExampleView(APIView):

    ## These two lines require the request to have a valid JWT in the headers. Use on any views that should be protected.
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]