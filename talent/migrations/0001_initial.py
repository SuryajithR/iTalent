# Generated by Django 3.2.12 on 2022-09-09 10:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='skills')),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('role', models.CharField(default='', max_length=50)),
                ('status', models.IntegerField(default='1')),
            ],
        ),
        migrations.CreateModel(
            name='talent_uploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(max_length=501)),
                ('files', models.ImageField(upload_to='skills', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('can_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.signup')),
            ],
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(default='', max_length=501)),
                ('talent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.talent_uploads')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.signup')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('talent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.talent_uploads')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.signup')),
            ],
        ),
    ]
