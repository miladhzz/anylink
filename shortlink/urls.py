from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shortlink import views

urlpatterns = [
                  path('', views.CreateLink.as_view(), name='create_link'),
                  path('detail/<slug:slug>', views.LinkDetail.as_view(), name='link_detail'),
                  path('<slug:slug>', views.Redirect.as_view(), name='redirect'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
