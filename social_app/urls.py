from django.urls import path
from social_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("logout/", views.logout, name="logout"),
]
