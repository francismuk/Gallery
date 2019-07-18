from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single_image, name='single_image'),
    url(r'^location/(?P<location>\d+)', views.location_filter, name='location_filter'),
    url(r'^search', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)