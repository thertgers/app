from django.contrib import admin
from .models import Note, Project, Category

# Register your models here.
admin.site.register(Note)
admin.site.register(Project)
admin.site.register(Category)
