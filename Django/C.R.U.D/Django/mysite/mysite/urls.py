from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from core.views import index,contact
from core import views

urlpatterns = [
    path('',include('core.urls')),
    path("new/", views.inde, name="inde"),
    path("admin/", admin.site.urls),
    path("item/",include('item.urls')),
    path("dashboard/",include('dashboard.urls')),
]     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
