from rest_framework import serializers
from .models import GameReview

class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameReview
        fields = '__all__'