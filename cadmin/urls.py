from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='cadmin_index'),
    path('login', views.login_view, name='cadmin_login'),
    path('logout', views.logout_view, name='cadmin_logout'),

]
