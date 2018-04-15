from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from .models import Item
from .serializers import ItemModelSerializer
from .filters import ItemFilter


class ItemModelViewSet(ModelViewSet):
	queryset = Item.objects.all().order_by('id')
	serializer_class = ItemModelSerializer
	http_method_names = [u'get', u'post', u'put', u'delete']	
	filter_class = ItemFilter