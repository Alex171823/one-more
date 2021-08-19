import debug_toolbar

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mysite.urls')),
    path('hw15/', include('hw15.urls')),
    path('practice/', include('practice.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
    path('silk/', include('silk.urls', namespace='silk')),
]
