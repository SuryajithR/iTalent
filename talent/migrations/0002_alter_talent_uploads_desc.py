# Generated by Django 3.2.12 on 2022-09-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent_uploads',
            name='desc',
            field=models.CharField(default='', max_length=501),
        ),
    ]
