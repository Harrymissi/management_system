# Generated by Django 2.0.3 on 2018-03-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20180321_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='class_day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wendsday', 'Wendsday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('No Class so far', 'No Class so far')], default='No Class so far', max_length=20, verbose_name='Class day'),
        ),
    ]