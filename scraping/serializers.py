from rest_framework import serializers
from .models import MainNews

class MainNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainNews
        fields = ('title',
                'summary',
                'publishDay',
                'link')
        