from rest_framework import serializers
from .models import GameReview

# Serializer for API
class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameReview
        fields = '__all__'