from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['index', 'about', 'contact', 'marek']  # Nazwy widoków z `urls.py`

    def location(self, item):
        return reverse(item)
