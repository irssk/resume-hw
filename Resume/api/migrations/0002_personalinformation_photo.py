# Generated by Django 4.2.3 on 2023-09-05 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='photo',
            field=models.TextField(default=''),
        ),
    ]