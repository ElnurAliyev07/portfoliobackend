from rest_framework import serializers
from apps.project.models import Project
import json

class ProjectSerializer(serializers.ModelSerializer):
    featured_image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'short_description', 'description', 'featured_image', 'technologies',
            'github_url', 'live_url', 'category', 'year', 'team_size',
            'duration', 'impact', 'is_featured', 'stats_views',
            'stats_stars', 'stats_forks', 'created_at'
        ]

    def get_featured_image(self, obj):
        if obj.featured_image:
            return obj.featured_image.url
        return None

    def validate_technologies(self, value):
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                raise serializers.ValidationError("Technologies must be a valid JSON list of strings.")
        if not isinstance(value, list) or not all(isinstance(tech, str) for tech in value):
            raise serializers.ValidationError("Technologies must be a list of strings.")
        return value

    def validate_awards(self, value):
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                raise serializers.ValidationError("Awards must be a valid JSON list of strings.")
        if not isinstance(value, list) or not all(isinstance(award, str) for award in value):
            raise serializers.ValidationError("Awards must be a list of strings.")
        return value
