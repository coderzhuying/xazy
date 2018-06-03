from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^.html$',views.news),
    url(r'^/company/list/(.+)$',views.companycontent),
    url(r'^/local/list/(.+)$',views.localcontent),
    url(r'^/media/list/(.+)$',views.mediacontent)
]