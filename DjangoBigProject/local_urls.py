import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include(debug_toolbar.urls)),
    path('silk/', include('silk.urls', namespace='silk')),
]