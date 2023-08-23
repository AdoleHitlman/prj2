from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import contacts, catalog

urlpatterns = [
                  path("", contacts),
                  path("contacts/", contacts, name="contacts"),
                  path("catalog/", catalog, name="catalog"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
