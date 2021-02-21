from django import forms
from django.test import TestCase
from django.db import models
from django.forms import ModelForm
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

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Naam', 'autofocus': True}),
        }
        labels = {
            'name': '',
            'forProject': 'Voor Project',
            'forNote': 'Voor Notitie'
        }


class Project(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Projects')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='2')

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(forProject=True)

class Note(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    description = models.TextField(max_length=2048)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notes')
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='2')

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['description', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Plaats hier een notitie. Voer "lorem" in voor 3 gegenereerde paragrafen.', 'autofocus': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(forNote=True)
