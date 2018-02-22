from rest_framework import serializers


class RepoSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=140)
    created_at = serializers.DateTimeField()
    pushed_at = serializers.DateTimeField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
