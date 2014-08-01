from rest_framework import serializers

from ..common import models

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Show