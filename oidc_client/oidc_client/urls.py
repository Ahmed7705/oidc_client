
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oidc-client/', include('oidc_client_app.urls')),

]
