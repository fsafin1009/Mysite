from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

# Cоздание с помощью функции

# def index(request):
#     article = Article.objects.all()
#     context = {
#         'article': article,
#         'title': "List newses",
#     }
#     return render(request, template_name='polls/index.html', context=context)

# def edit_page(request):
#     secces = False
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             secces = True
#     context = {
#         'list_articles' : Article.objects.all().order_by('-id'),
#         'form' : ArticleForm(),
#         'succes' : secces,
#     }
#     return render(request, template_name='polls/edit.html', context=context)

# def update_page(request, pk):
#     success_update = False
#     get_article = Article.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, instance=get_article)
#         if form.is_valid():
#             form.save()
#             success_update = True
#
#     context = {
#         'ger_article' : get_article,
#         'update' : True,
#         'form': ArticleForm(instance=get_article),
#         'success_update' :success_update
#     }
#     return render(request, template_name='polls/edit.html', context=context)

#
# def delete_page(request, pk):
#     get_article = Article.objects.get(pk=pk)
#     get_article.delete()
#     return redirect(reverse('polls:edit_page'))


# def detail(request, id):
#     get_article = Article.objects.get(id=id)
#     context = {
#         'get_article' :get_article
#     }
#     return render(request, template_name='polls/detail.html', context=context)


# Cоздание с помощью класса
# -----------------------------------------------------------
class HomeListView(ListView):
    model = Article
    template_name = 'polls/index.html'
    context_object_name = 'article'

class HomeDetaiView(DetailView):
    model = Article
    template_name = 'polls/detail.html'
    context_object_name = 'get_article'


# Класс отображени усешной надписи по оперциям
class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(CustomSuccessMessageMixin, self).form_valid(form)


class ArticleCreateView(LoginRequiredMixin,CustomSuccessMessageMixin,CreateView):
    model = Article
    template_name = 'polls/edit.html'
    form_class = ArticleForm
    success_msg = "Запись создана"
    success_url = reverse_lazy('polls:edit_page')
    def get_context_data(self, **kwargs):
        kwargs ['list_articles'] = Article.objects.all().order_by('-id')
        return super(ArticleCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(LoginRequiredMixin, self).form_valid(form)

class ArticleUpdateView(LoginRequiredMixin,CustomSuccessMessageMixin,UpdateView):
    model = Article
    template_name = 'polls/edit.html'
    form_class = ArticleForm
    success_msg = "Запись обновлена"
    success_url = reverse_lazy('polls:edit_page')
    def get_context_data(self, **kwargs):
        kwargs ['update'] = True
        return super(ArticleUpdateView, self).get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs =  super(ArticleUpdateView, self).get_form_kwargs()
        # проверка пользователя на принадлежность авторства
        if self.request.user !=  kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class ArticleDeleteView(LoginRequiredMixin,CustomSuccessMessageMixin,DeleteView):
    model = Article
    template_name = 'polls/edit.html'
    success_msg = "Запись удалена"
    success_url = reverse_lazy('polls:edit_page')
    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super(CustomSuccessMessageMixin, self).post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user !=  self.object.author:
            return self.handle_no_permission()
        success_url =  self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
# - -------------------------------------------------------------------------------------------------
# Cоздание класса для Аторизации пользователя

class MyLoginView(LoginView):
    template_name = 'polls/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('polls:edit_page')

    def get_success_url(self):
        return self.success_url

# Cоздание класса для Регистраци пользователя

class RegisterLoginView(CreateView):
    model = User
    template_name = 'polls/register.html'
    form_class = RegisterUserForm
    success_msg = "Пользователь создан"
    success_url = reverse_lazy('polls:edit_page')

# Cоздание функции для авторизации пользователя

    def form_valid(self, form):
        form_valid = super(RegisterLoginView, self).form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user =  authenticate(username = username, password = password)
        login(self.request, aut_user)
        return form_valid

# Cоздание класса для Выхода пользователя

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('polls:login_page')






