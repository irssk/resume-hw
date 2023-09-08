from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from . import models
from . import serializers


# Create your views here.
class PersonalInformation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id=1):
        info = models.PersonalInformation.objects.get(id=user_id)
        serialized_info = serializers.SerializedPersonalInformation(info)
        return Response(serialized_info.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass


class Skills(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass


class Educations(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass
