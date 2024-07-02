from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

# Listado de las URL de la app social de proyecto

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

