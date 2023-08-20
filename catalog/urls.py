from django.urls import path
from catalog.views import contacts,home


urlpatterns = [
    path("", contacts),
    path("catalog/", contacts, name="contacts"),
    path("home/", home,name="home"),
]


