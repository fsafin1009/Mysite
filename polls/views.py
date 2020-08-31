from django.shortcuts import render, redirect

from .models import Article
from django.views.generic import ListView, DetailView
from .forms import ArticleForm
from django.urls import reverse
# Create your views here.


# Cоздание с помощью функции
# def index(request):
#     article = Article.objects.all()
#     context = {
#         'article': article,
#         'title': "List newses",
#     }
#     return render(request, template_name='polls/index.html', context=context)


# Cоздание с помощью класса


class HomeListView(ListView):
    model = Article
    template_name = 'polls/index.html'
    context_object_name = 'article'

class HomeDetaiView(DetailView):
    model = Article
    template_name = 'polls/detail.html'
    context_object_name = 'get_article'


# def detail(request, id):
#     get_article = Article.objects.get(id=id)
#     context = {
#         'get_article' :get_article
#     }
#     return render(request, template_name='polls/detail.html', context=context)
#


def edit_page(request):
    secces = False
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            secces = True
    context = {
        'list_articles' : Article.objects.all().order_by('-id'),
        'form' : ArticleForm(),
        'succes' : secces,
    }
    return render(request, template_name='polls/edit.html', context=context)


def update_page(request, pk):
    success_update = False
    get_article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            success_update = True

    context = {
        'ger_article' : get_article,
        'update' : True,
        'form': ArticleForm(instance=get_article),
        'success_update' :success_update
    }
    return render(request, template_name='polls/edit.html', context=context)

def delete_page(request, pk):
    get_article = Article.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('polls:edit_page'))




