from django.urls import path

from polls import views

app_name = 'polls'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('detail/<int:id>', views.detail, name='detail'),
    path('', views.HomeListView.as_view(), name='index'),
    path('detail/<int:pk>', views.HomeDetaiView.as_view(), name='detail'),
    path('edit-page', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.ArticleDeleteView.as_view(), name= 'delete_page'),
]