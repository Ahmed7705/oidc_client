# C:\Users\ahmed\Desktop\SSO Project\SSO\oidc_client\oidc_client\oidc_client_app\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.oidc_login, name='oidc_login'),
    path('callback/', views.oidc_callback, name='oidc_callback'),
    path('test-access/', views.test_access_view, name='test_access'),
    path('no-access/', views.no_access_view, name='no_access'),

]
