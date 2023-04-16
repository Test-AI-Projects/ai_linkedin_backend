from rest_framework import serializers

from .models import College



class CollegeMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = ("label", "value")
