# Generated by Django 2.0.3 on 2018-03-21 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20180320_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='class_level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'intermediate'), ('Advanced', 'Advanced'), ('No Class', 'No Class')], max_length=50, verbose_name='Level'),
        ),
    ]
