from rest_framework import serializers
from .models import Project, Pledge
# there is no textfield in serializers, charfield is used instead

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

# split Projectserializer in two - one for proejct info, one for project info AND pledges


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)



