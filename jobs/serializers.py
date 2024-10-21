from rest_framework import serializers

class JobRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)

class JobDetailedRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
