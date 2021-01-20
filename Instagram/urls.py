
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include("app.urls")),
    path('portfolio/', include("Portfolio.urls")),
    path('portfolio/polls', include("polls.urls")),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
