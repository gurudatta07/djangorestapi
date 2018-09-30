from rest_framework import serializers
from .models import Dataset1

class Dataset1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset1
        fields = ('name', 'title', 'date_created')
        read_only_fields = ('date_created')