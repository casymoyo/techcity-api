# Generated by Django 5.0.3 on 2024-03-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store_app", "0003_user_phonenumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="code",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
