from django_filters import rest_framework as filters
from django_filters import NumberFilter
from .models import Item

class ItemFilter(filters.FilterSet):

	cost_gte = NumberFilter(name='cost_gte',method='filter_cost_gte') 
	cost_lte = NumberFilter(name='cost_lte',method='filter_cost_lte') 

	def filter_cost_gte(self, queryset, name, value):
		return queryset.filter(cost__gte=value)
	
	def filter_cost_lte(self, queryset, name, value):
		return queryset.filter(cost__lte=value)
	class Meta:
		model = Item
		fields = ('name','size',)