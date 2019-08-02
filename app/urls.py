from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('', include('app.pools.urls')),
    path('', include('app.transactions.urls')),
    path('admin/', admin.site.urls),
    path('auth-token', views.obtain_auth_token)
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
