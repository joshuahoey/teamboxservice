from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from . import serializers

# Create your views here.


class ExampleView(APIView):
    pass

    ## These two lines require the request to have a valid JWT in the headers. Use on any views that should be protected.
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]


class RegisterViewSet(APIView):

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response({'username': serializer.data['username'],
                             'is_employee': serializer.data['is_employee']},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
