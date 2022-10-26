from django.urls import path, re_path
from . import views


app_name = "references"

urlpatterns = [
    path('list-author', views.ListReferencesAuthor.as_view(), name='list-author'),
    path('list-genre', views.ListReferencesGenre.as_view(), name='list-genre'),
    path('list-currenсy', views.ListReferencesCurrenсy.as_view(), name='list-currenсy'),

    path('detail/author/<int:pk>/', views.DetailReferencesAuthor.as_view(), name='detail-author'),
    path('detail/genre/<int:pk>/', views.DetailReferencesGenre.as_view(), name='detail-genre'),
    path('detail/currenсy/<int:pk>/', views.DetailReferencesCurrenсy.as_view(), name='detail-currenсy'),

    path('create/author/', views.CreateReferencesAuthor.as_view(), name='create-author'),
    path('create/genre/', views.CreateReferencesGenre.as_view(), name='create-genre'),
    path('create/currenсy/', views.CreateReferencesCurrenсy.as_view(), name='create-currenсy'),

    path('update/author/<int:pk>/', views.UpdateReferencesAuthor.as_view(), name='update-author'),
    path('update/genre/<int:pk>/', views.UpdateReferencesGenre.as_view(), name='update-genre'),
    path('update/currenсy/<int:pk>/', views.UpdateReferencesCurrenсy.as_view(),  name='update-currenсy'),
    
    path('delete/author/<int:pk>/', views.DeleteReferencesAuthor.as_view(), name='delete-author'),
    path('delete/genre/<int:pk>/', views.DeleteReferencesGenre.as_view(), name='delete-genre'),
    path('delete/currenсy/<int:pk>/', views.DeleteReferencesCurrenсy.as_view(), name='delete-currenсy')
]
