from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import contacts, home

urlpatterns = [
                  path("", contacts),
                  path("catalog/", contacts, name="contacts"),
                  path("home/", home, name="home"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
