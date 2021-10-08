from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
            
]