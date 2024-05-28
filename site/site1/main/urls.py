from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faq', views.faq, name='faq'),
    path('sozvezdie/', views.sozvesdie, name='sozvezdie'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    ]

