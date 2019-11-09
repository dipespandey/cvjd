from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url(r'^$', views.render_matches, name="index"),
    url(r'^jobwise/(?P<job_name>[\w ]+)/$', views.jobwise_results, name="jobwise_results"),
    url(r'^upload$', views.model_form_upload, name="upload"),
    url(r'^candidates/(?P<id>[0-9]+)/$', views.candidate_details, name="candidates"),
]

admin.site.site_header = "ExclusiveTailored Admin"
admin.site.site_title = "ExclusiveTailored Admin Portal"
admin.site.index_title = "Welcome to ExclusiveTailored Portal"
