# Generated by Django 4.1.2 on 2022-10-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_procedure_delete_procedures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='date',
            field=models.DateField(verbose_name='Procedure Date'),
        ),
    ]
