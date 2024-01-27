from django.contrib import admin
from django.urls import path, include

import blogapi.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blogapi.urls'), name="api"),
]