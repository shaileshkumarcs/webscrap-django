from django.conf.urls import url

from . import views

app_name = 'web_scraping'

urlpatterns = [
    url(r'^indeed/$', views.ScrapIndeed.as_view(), name='indeed'),
    url(r'^exportcsv/$', views.ExportCsv.as_view(), name='exportcsv'),
]