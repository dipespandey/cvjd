from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.model_form_upload, name="index"),
]
