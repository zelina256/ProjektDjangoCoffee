from django.urls import path
from . import views

urlpatterns = [
    # path('slug', views.emriFunksion, name="cfaredo")
    # vlera e name perdoret tek href ne tag-un a
    path("", views.home, name="homePage"), 
    path("about/", views.about, name="aboutPage"),
    path("menu/", views.menu, name="menuPage"),
    path("contact/", views.contact, name="contactPage"),
]