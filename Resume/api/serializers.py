from rest_framework.serializers import ModelSerializer

from . import models


class SerializedSkills(ModelSerializer):
    class Meta:
        model = models.Skills
        fields = ['id', 'title']


class SerializedEducations(ModelSerializer):
    class Meta:
        model = models.Educations
        fields = ['id', 'title', 'specialization', 'start_year', 'end_year']


class SerializedPersonalInformation(ModelSerializer):
    skills = SerializedSkills(read_only=True, many=True)
    educations = SerializedEducations(read_only=True, many=True)

    class Meta:
        model = models.PersonalInformation
        fields = ['name', 'surname', 'year_of_birth', 'photo', 'phone', 'email', 'skills', 'educations']
