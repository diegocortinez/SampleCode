from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('checking/', include('Checking.urls')),
    path('savings/', include('Savings.urls')),
    path('user/', include('User.urls')),
    path('api/user/', include('User.API.urls')),
] + static(settings.MEDIA_URL, document_root=settings.STATICFILES_DIRS)
