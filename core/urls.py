from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gioi-thieu/", views.about, name="about"),
    path("lien-he/", views.contact, name="contact"),
    path("co-cau-to-chuc/", views.structure, name="structure"),
    path("tin-tuc/", views.news_list, name="news_list"),
    path("tin-tuc/<slug:slug>/", views.news_detail, name="news_detail"),
    path("tai-lieu/", views.document_list, name="document_list"),
    path("ban-tin/", views.bulletin_list, name="bulletin_list"),
    path("ban-tin/<slug:slug>/", views.bulletin_detail, name="bulletin_detail"),
]
