from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('members/', include('django_templetes.urls')),
    path('admin/', admin.site.urls),
]