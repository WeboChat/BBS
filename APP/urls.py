from django.conf.urls import url

from APP import views

urlpatterns=[
    url(r'^post/create/', views.create,name='create'),
    url(r'^post/read/', views.read,name='read'),
    url(r'^post/edit/', views.edit,name='edit'),
    url(r'^post/search/', views.search,name='search'),

    url(r'^user/register/', views.register, name='register'),
    url(r'^user/login/', views.login, name='login'),
    url(r'^user/loginout/', views.loginout, name='loginout'),
    url(r'^user/info/', views.info, name='info'),
]