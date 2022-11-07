from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('dashboard/', include('PanaceaApp.urls')),
    path('', include('accounts.urls')),
]
