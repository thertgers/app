from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import (
    get_user_model, password_validation
)
from django.utils.translation import gettext, gettext_lazy as _
from django import forms

from .models import Category, Project, Note, Attachment


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Wachwoord'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Wachtwoord controle'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Gebruikersnaam'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email adres'}),
        }
        labels = {
            'username': '',
            'email': '',
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Gebruikersnaam'}),
            'password': forms.TextInput(attrs={'placeholder': 'Wachtwoord'}),
        }
        labels = {
            'username': '',
            'email': '',
        }

    def confirm_login_allowed(self, user):
        pass

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Gebruikersnaam'})

        self.fields['password'].label = ''
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Wachtwoord'})


class CategoryForm(forms.ModelForm):
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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(forProject=True)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['description', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Plaats hier een notitie. Voer "lorem" in voor 3 gegenereerde paragrafen.', 'autofocus': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(forNote=True)


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['note', 'file', 'description']
