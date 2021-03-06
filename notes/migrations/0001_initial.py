# Generated by Django 3.0.6 on 2021-04-01 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=2048)),
                ('forProject', models.BooleanField(default=True)),
                ('forNote', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='notes.Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(max_length=2048)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.Project')),
                ('category', models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='notes.Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('file', models.FileField(upload_to='files')),
                ('description', models.CharField(max_length=255)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.Note')),
            ],
        ),
    ]
