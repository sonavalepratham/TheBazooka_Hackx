# Generated by Django 3.0.8 on 2021-10-09 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HealthMonitor', '0002_symptomsinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptomsinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
