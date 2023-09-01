from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import CatalogView, IndexView, ProductView, ContactsView,BlogDetailView,BlogUpdateView,PublishedBlogListView

urlpatterns = [
                  path("", IndexView.as_view()),
                  path("contacts/", ContactsView.as_view(), name="contacts"),
                  path("catalog/", CatalogView.as_view(), name="catalog"),
                  path('product/<int:product_id>/', ProductView.as_view(), name='product'),
                  path("index/", IndexView.as_view(), name="index"),
                  path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
                  path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
                  path('blog/published/', PublishedBlogListView.as_view(), name='blog-published'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
