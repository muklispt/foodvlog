from django.urls import path
from . import views
urlpatterns = [ path('mu',views.mu,name='mu'),
                path ('login',views.login,name='login'),
                path('logout',views.logout,name='logout')
                
    
]