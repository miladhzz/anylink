from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shortlink import views

urlpatterns = [
    path('', views.CreateLink.as_view(), name='create_link'),
    path('detail/<slug:slug>', views.LinkDetail.as_view(), name='link_detail'),
    path('<slug:slug>', views.Redirect.as_view(), name='redirect'),
    path('links/', views.LinkList.as_view(), name='links'),
    path('api/v1', views.ListLinkApi.as_view()),
    path('api/v1/<int:pk>', views.DetailLinkApi.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
