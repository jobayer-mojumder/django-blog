from django.urls import path, include

urlpatterns = [
    path('cadmin/', include('cadmin.urls')),
    path('blog/', include('blog.urls')),
]
