from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='img_upl'),
    path('crud', views.my_view, name='my_view'),
    path('delete/<int:id>', views.delete_info, name='confirm_delete'),
    path('edit/<int:id>', views.edit_info, name='updated'),
    path('success_page', views.success_page, name='success'),
    path('registration', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('changepassword/', views.change_password, name='change-password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
