from django.shortcuts import render, redirect

from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
# Create your views here.


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


class HomeListView(ListView):
    model = Article
    template_name = 'polls/index.html'
    context_object_name = 'article'

class HomeDetaiView(DetailView):
    model = Article
    template_name = 'polls/detail.html'
    context_object_name = 'get_article'

class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(CustomSuccessMessageMixin, self).form_valid(form)



class ArticleCreateView(CustomSuccessMessageMixin,CreateView):
    model = Article
    template_name = 'polls/edit.html'
    form_class = ArticleForm
    success_msg = "Запись создана"
    success_url = reverse_lazy('polls:edit_page')
    def get_context_data(self, **kwargs):
        kwargs ['list_articles'] = Article.objects.all().order_by('-id')
        return super(ArticleCreateView, self).get_context_data(**kwargs)

class ArticleUpdateView(CustomSuccessMessageMixin,UpdateView):
    model = Article
    template_name = 'polls/edit.html'
    form_class = ArticleForm
    success_msg = "Запись обновлена"
    success_url = reverse_lazy('polls:edit_page')
    def get_context_data(self, **kwargs):
        kwargs ['update'] = True
        return super(ArticleUpdateView, self).get_context_data(**kwargs)


class ArticleDeleteView(CustomSuccessMessageMixin,DeleteView):
    model = Article
    template_name = 'polls/edit.html'
    success_msg = "Запись удалена"
    success_url = reverse_lazy('polls:edit_page')
    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super(CustomSuccessMessageMixin, self).post(request)













