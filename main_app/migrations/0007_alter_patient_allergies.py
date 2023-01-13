# Generated by Django 4.1.2 on 2022-10-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_patient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.CharField(choices=[('R', 'Root Canal'), ('C', 'Cleaning'), ('F', 'Filling'), ('E', 'Extraction'), ('B', 'BiteWings'), ('P', 'Panoramic')], default='R', max_length=1),
        ),
    ]