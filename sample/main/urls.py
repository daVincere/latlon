from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
		url(r'data/$', views.DataListing.as_view()),
		url(r'data/(?P<pk>[0-9]+)/$', views.DataDetail.as_view()),
	]

urlpatterns = format_suffix_patterns(urlpatterns)