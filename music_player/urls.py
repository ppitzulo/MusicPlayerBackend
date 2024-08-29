"""
URL configuration for music_player project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from audiomanager.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list-songs/', AudioAPIView.as_view(), name='audio_fetch'),
    path('api/audio/<int:song_id>/', AudioAPITest.as_view(), name='audioAPITest'),
    path('api/csrf-token', CSRFTokenAPIView.as_view(), name='csrf_token'),
    path('api/search/', SearchView.as_view(), name="audio_search"),
]

if not settings.DEMO_MODE:
    urlpatterns += [
        path('api/upload/', AudioUploadAPIView.as_view(), name='audio_upload'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
