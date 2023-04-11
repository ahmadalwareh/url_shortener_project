from rest_framework import serializers
from .models import URLMapping


class URLMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapping
        fields = ['short_url', 'original_url']
