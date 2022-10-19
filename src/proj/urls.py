"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homepage.views import index
from references import views as ref_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #Author
    path('author/detail_a/<int:pk>/', ref_views.DetailReferencesAuthor.as_view()),
    path('author/create_a/', ref_views.CreateReferencesAuthor.as_view()),
    path('author/update_a/<int:pk>/', ref_views.UpdateReferencesAuthor.as_view()),
    path('author/list_a/', ref_views.ListReferencesAuthor.as_view()),
    path('author/delete_a/<int:pk>/', ref_views.DeleteReferencesAuthor.as_view()),
    #Genre
    path('genre/detail_g/<int:pk>/', ref_views.DetailReferencesGenre.as_view()),
    path('genre/create_g/', ref_views.CreateReferencesGenre.as_view()),
    path('genre/update_g/<int:pk>/', ref_views.UpdateReferencesGenre.as_view()),
    path('genre/list_g/', ref_views.ListReferencesGenre.as_view()),
    path('genre/delete_g/<int:pk>/', ref_views.DeleteReferencesGenre.as_view()),
    #Currenсy
    path('currenсy/detail_c/<int:pk>/', ref_views.DetailReferencesCurrenсy.as_view()),
    path('currenсy/create_c/', ref_views.CreateReferencesCurrenсy.as_view()),
    path('currenсy/update_c/<int:pk>/', ref_views.UpdateReferencesCurrenсy.as_view()),
    path('currenсy/list_c/', ref_views.ListReferencesCurrenсy.as_view()),
    path('currenсy/delete_c/<int:pk>/', ref_views.DeleteReferencesCurrenсy.as_view())
]
