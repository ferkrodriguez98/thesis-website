from django.urls import path
from . import views

app_name = 'app_tesis'

urlpatterns = [
    path('', views.home, name='home'),
    path('person-form/', views.person_form, name='person_form'),
    path('success/', views.success, name='success'),
    path('change_language/<str:language>/', views.switch_language, name='switch_language'),
]
