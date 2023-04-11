from rest_framework import views, status
from rest_framework.response import Response
from .models import URLMapping
from .serializers import URLMappingSerializer
import string
import random


class URLShortenView(views.APIView):
    def post(self, request):
        original_url = request.data.get('original_url')
        short_url = self.generate_short_url()
        mapping = URLMapping.objects.create(
            short_url=short_url, original_url=original_url)
        serializer = URLMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def generate_short_url(self):
        short_url = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=6))
        while URLMapping.objects.filter(short_url=short_url).exists():
            short_url = ''.join(random.choices(
                string.ascii_lowercase + string.digits, k=6))
        return short_url
