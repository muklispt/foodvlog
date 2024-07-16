from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,),
    path('<slug:c_slug>/', views.home, name='category_detail'),
    path('<slug:ct_slug>/<slug:prodect_slug>/', views.details, name='product_detail'),
    path('sarch', views.sarchea, name='sarch')

]
