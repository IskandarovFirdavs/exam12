from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from exam12 import settings
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('folder.urls', namespace='folder')),
    path('users/', include('users.urls', namespace='users')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
