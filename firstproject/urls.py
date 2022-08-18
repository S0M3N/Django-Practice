from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
]
 