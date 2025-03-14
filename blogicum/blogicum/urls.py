from django.contrib import admin
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
    path('category/', include('blog.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
