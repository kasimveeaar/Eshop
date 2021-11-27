from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.Profiles , name='profile'),
    

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)