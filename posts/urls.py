from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # / /
    path('', views.post_list_view, name='post_list'),
    # /5/react
    path('<int:post_id>/react', views.react, name='react'),
    # /5/add_comment
    path('<int:post_id>/add_comment', views.add_comment, name='add_comment')
]
