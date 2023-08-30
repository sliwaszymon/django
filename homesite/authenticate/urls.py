from django.urls import path, re_path
from . import views
from django.contrib.auth.views import (PasswordChangeView, PasswordResetView, PasswordChangeDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView)

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done.', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset_done'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
