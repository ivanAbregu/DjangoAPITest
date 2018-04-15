from rest_framework import serializers

from .models import Item

class ItemModelSerializer(serializers.ModelSerializer):
    """
    size_display = serializers.SerializerMethodField()

    def get_size_display(self, obj):
        return obj.get_size_display()
	"""
    class Meta:
        model = Item
        fields = '__all__'
