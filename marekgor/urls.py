from django.contrib.sitemaps.views import sitemap
from marekgor.sitemaps import StaticViewSitemap
from django.urls import path
import views

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('marek/', views.marek, name='marek'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
