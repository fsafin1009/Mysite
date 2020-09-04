from django import forms
from django.contrib.auth.models import User

from .models import Article
from django.contrib.auth.forms import AuthenticationForm



# Создани Формы Создане отчета
class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = 'title', 'content'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control" , "rows" : 10}

# Создани Формы Авторизации

class AuthUserForm(AuthenticationForm,forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}

# Создани Формы регистрации

class RegisterUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}

    # Пролучение авоматического шифорвание пароля
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user