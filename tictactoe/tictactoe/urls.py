
from django.contrib import admin
from django.urls import path, include
from tictactoe.game import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('change/', views.change, name='change'),
    path('reset/', views.reset, name='reset'),
    path('admin/', admin.site.urls),
]
