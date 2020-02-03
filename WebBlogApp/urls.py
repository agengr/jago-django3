from django.urls import path
from . import views

urlpatterns=[
    path('',views.WebBlogListView.as_view(),name='beranda'),
    path('post/<int:pk>/', views.WebBlogDetailView.as_view(), name='post_detail')
]