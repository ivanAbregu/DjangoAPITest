from django.conf.urls import include, url

from rest_framework import routers
from rest_framework.authtoken import views

from django.contrib import admin
from django.views.generic import TemplateView

from apps.appItems.views import ItemModelViewSet


router = routers.DefaultRouter()
router.register(r'items', ItemModelViewSet)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', views.obtain_auth_token),
    url(r'^$', TemplateView.as_view(template_name ='appItems/list.html'),
        name='index'),
]
