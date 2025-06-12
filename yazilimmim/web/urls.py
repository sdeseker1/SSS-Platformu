from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Kayıt ve Giriş
    path('register/', views.register_view, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='web/login.html'), name='login'),

    # Kullanıcıların soru sorduğu sayfa
    path('ask/', views.ask_question, name='ask_question'),

    # SSS listesi
    path('sss/', views.sss_view, name='sss'),

    # Admin Paneli
    path('admin_panel/', views.admin_panel, name='admin_panel'),
   path('admin_panel/', views.admin_panel, name='admin_panel'),
path('admin_panel/delete/<int:question_id>/', views.delete_question, name='delete_question'),
path('admin_panel/delete/<int:question_id>/', views.delete_question, name='delete_question'),

]
