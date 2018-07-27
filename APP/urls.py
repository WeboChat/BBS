from django.conf.urls import url

from APP import views

urlpatterns=[
    url(r'^hello/',views.hello,name='hello'),
]