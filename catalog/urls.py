from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import contacts, catalog, product,base,menu

urlpatterns = [
                  path("", contacts),
                  path("contacts/", contacts, name="contacts"),
                  path("catalog/", catalog, name="catalog"),
                  path("product/", product, name='product'),
                  path("base/",base,name="base"),
                  path("menu/",menu,name="menu"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
