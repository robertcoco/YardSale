"""YardSale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shop import views
from django.views.defaults import page_not_found

urlpatterns = [
    path('', views.home, name='home'),
    path("shop/", include("shop.urls")),
    path('accounts/', include('allauth.urls')),
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('accounts/password/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='account_reset_password_confirm'),
    path('accounts/password/done/', auth_views.PasswordResetCompleteView.as_view(), name='account_reset_password_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

handler404 = page_not_found