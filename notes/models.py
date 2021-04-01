from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Zet hier de database tabellen met kolommen in
# Een class is een kolom (in dit geval)
# Nadat er hier wijzigingen zijn:man
#   1. python.exe manage.py makemigrations (Converteerd dit bestand naar een migratie (voor SQL) bestand)
#   2. python.exe manage.py migrate (Voert een SQL opdracht uit met het migratie bestand)

class Category (models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=2048)
    forProject = models.BooleanField(default=True)
    forNote = models.BooleanField(default=True)

    def projectCount(self):
        return Project.objects.filter(categorie_id=self.id).count()

    def noteCount(self):
        return Note.objects.filter(categorie_id=self.id).count()

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=64)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Projects')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='2')
    created_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    description = models.TextField(max_length=2048)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notes')
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='2')
    created_at = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    description = models.CharField(max_length=255)
