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
    path('login', views.MyLoginView.as_view(), name= 'login_page'),
    path('register', views.RegisterLoginView.as_view(), name= 'register_page'),
    path('logout', views.MyLogoutView.as_view(), name= 'logout_page'),
]