
from django.urls import path
from . import views



urlpatterns = [

    path('', views.home, name='home'),
    path('crud', views.my_view, name='my_view'),
    path('delete/<int:id>', views.delete_info, name='confirm_delete'),
    path('edit/<int:id>', views.edit_info, name='updated'),
    path('success_page', views.success_page, name='success'),
    path('registration', views.registration, name= 'registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
