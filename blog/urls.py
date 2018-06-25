from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('register/',views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/<int:user_id>/', views.view_profile, name='view_profile'),
    path('users/<int:user_id>/edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_post/',views.create_post, name='create_post'),
    path('<int:post_id>/create_comment/',views.create_comment, name='create_comment'),
]