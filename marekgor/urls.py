from django.contrib.sitemaps.views import sitemap
from marekgor.sitemaps import StaticViewSitemap
from django.urls import path
from marekgor import views

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('calc/', views.calc, name='calc'),
    path('gallery/', views.gallery, name='gallery'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
