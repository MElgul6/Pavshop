from re import template
from django.urls import path
from User.views import (CustomLoginView,RegisterView,
                        logout_page,ActiveAccountView,
                        password_success,PasswordsChangeView)
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views
# from User import views as user_views

  
urlpatterns = [
    path('login/', CustomLoginView.as_view(),name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name="logout_page"),
    path('activate/<str:uidb64>/<str:token>/', ActiveAccountView.as_view(), name="activate"),
    path('password_change/', PasswordsChangeView.as_view(template_name='change_password.html'), name='password_change'),
    path('password_success/',views.password_success,name='password_success'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
      
]

 
