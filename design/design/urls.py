from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', include('designstudio.urls'))
]
urlpatterns += static(settings.STATIC_URL)