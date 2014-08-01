from rest_framework import serializers

from bathtub.common import models

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Show