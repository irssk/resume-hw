from django.db import models


# Create your models here.

class Skills(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class Educations(models.Model):
    title = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.specialization}"


class PersonalInformation(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    photo = models.ImageField(upload_to='api/static/api/photo/')
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skills)
    educations = models.ManyToManyField(Educations)

    def __str__(self):
        return f"{self.name} {self.surname}"
