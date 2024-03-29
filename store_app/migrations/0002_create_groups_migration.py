# Generated by Django 4.2.6 on 2024-03-11 18:39

from django.db import migrations
from django.contrib.auth.models import Group


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')  # Import the Group model
    Group.objects.get_or_create(name='ADMIN')
    Group.objects.get_or_create(name='ACCOUNTANT')
    Group.objects.get_or_create(name='SALESPERSON')

class Migration(migrations.Migration):
    dependencies = [
        ("store_app", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(create_groups),
    ]
# 