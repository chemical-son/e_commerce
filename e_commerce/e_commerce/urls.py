from django.contrib import admin
from django.urls import path, include

app_name = 'e_commerce'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_dahsboard/', include('admin_dashboard.urls')),
    path('auth/', include('authentication.urls')),
    path('shop/', include('shop.urls')),
]
