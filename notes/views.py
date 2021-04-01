from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import Note, Project, Category
from .forms import RegisterForm, LoginForm, CategoryForm, ProjectForm, NoteForm, AttachmentForm
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, update_session_auth_hash,
)
# Create your views here.
# Zet hier de Python functies in.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.save()

            return redirect('../../home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form":form})

def Userlogin(request):
    logout(request)
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../../home')
        else:
            print(form.errors)

    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {"form":form})

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required()
def navbar(request):
    return render(request, 'navbar.html', {'username': (request.user.username)})

@login_required()
def home(request):
    username = request.user.username
    projectCount = Project.objects.filter(created_by=request.user).count()
    noteCount = Note.objects.filter(created_by=request.user).count()
    return render(request, 'home.html', {'username': username, 'projectCount': projectCount, 'noteCount': noteCount})

@login_required()
def category_list(request):
    return render(request, 'category_list.html', {'categories': Category.objects.all()})

@login_required()
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            return redirect('/category/list')
    else:
        form = CategoryForm()
    listCategories = Category.objects.all()
    return render(request, 'category_add.html', {'categories': listCategories, 'CategoryForm': form})

@login_required()
def category_get(request, id):
    return render(request, 'category_get.html', {'categorie': Category.objects.all()})

@login_required()
def category_delete(request,id):
    projectCount = Project.objects.filter(categorie=id)
    noteCount = Note.objects.filter(categorie=id)
    if((projectCount == 0) & (noteCount == 0)):
        Category.objects.filter(id=id).Delete()
        return redirect('category/list')
    else:
        return HttpResponseForbidden()

@login_required()
def category_update(request, id):
    cat = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=cat)
    if request.method == 'POST':
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            return redirect('/category/list')

    listCategories = Category.objects.all()
    return render(request, 'category_update.html', {'categories': listCategories, 'CategoryForm': form})

@login_required()
def project_list(request):
    return render(request, 'project_list.html', {'projects': Project.objects.all()})

@login_required()
def project_get(request, id):
    form = NoteForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            categorie = get_object_or_404(Category, id=1)
            note = form.save(commit=False)
            note.Project = Project.objects.get(id=id)
            note.category = categorie
            note.created_by = request.user
            note.save()
            listNotes = list(Note.objects.filter(Project=id))
            return redirect('/project/get/' + str(id))
    else:
        form = NoteForm()
    objectProject = get_object_or_404(Project, id=id)
    listNotes = list(Note.objects.filter(Project=objectProject))
    listProjects = Project.objects.all()
    request.session['activeProject'] = objectProject.id
    return render(request, 'project_get.html', {'projects': listProjects, 'project': objectProject, 'notes':listNotes, 'NoteForm': form})

@login_required()
def project_add(request):
    form = ProjectForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            categorie = get_object_or_404(Category, id=1)
            project = form.save(commit=False)
            project.category = categorie
            project.created_by = request.user
            project.save()
            return redirect('/project/get/' + str(project.id))
    else:
        form = ProjectForm()
    listProjects = Project.objects.all()
    return render(request, 'project_add.html', {'projects': listProjects, 'ProjectForm': form})

@login_required()
def project_delete(request, id):
    Project.objects.filter(id=id).delete()
    projects = Project.objects.all()
    username = request.user.username
    return redirect('project/list')

@login_required()
def note_add(request):
    form = NoteForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            note = form.save(commit=False)
            note.Project = Project.objects.get(id=(request.session.get('activeProject')))
            note.category = get_object_or_404(Category, id=1)
            note.created_by = request.user
            note.save()
            #return render(request, 'project_get.html', {'project': note.Project})
            return redirect('/project/get/' + str(note.Project.id))
    else:
        form = NoteForm()
    return render(request, 'note_add.html', {'id': id, 'NoteForm': form})

@login_required()
def note_delete(request, id):
    Project = Note.objects.get(id=id).Project.id
    Note.objects.filter(id=id).delete()
    return redirect(('/project/get/' + str(Project)))

def note_update(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(request.POST or None, instance=note)
    if request.method == 'POST':
        if form.is_valid():
            note.save()
            #return render(request, 'project_get.html', {'project': note.Project})
            return redirect('/project/get/' + str(note.Project.id))

    objectProject = note.Project
    listNotes = list(Note.objects.filter(Project=objectProject))
    listProjects = Project.objects.all()
    return render(request, 'note_update.html', {'projects': listProjects, 'notes':listNotes, 'NoteForm': form})

def note_upload(request, id):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    else:
        form = AttachmentForm()
        form.note = id
    return render(request, 'note_upload.html', {'AttachmentForm': form})
