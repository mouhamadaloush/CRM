from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'created_at',
            'first_name',
            'last_name',
            'email',
            'phone',
            'state',
            'city',
            'id',
        ]
