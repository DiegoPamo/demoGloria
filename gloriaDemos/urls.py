from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables', views.tables, name='tables'),
    path('editar/<int:id>/', views.edit_register, name='edit_register'),
    path('generar-pdf/<int:id>/', views.generar_pdf, name='generar_pdf'),

    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout, name='logout'),
]