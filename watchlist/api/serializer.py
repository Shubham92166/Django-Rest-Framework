from rest_framework import serializers
from watchlist.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        #fields = "__all__"
        exclude = ['id']
    '''
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.is_active = validated_data.get('is_active')
        instance.save()
        return instance
    
    '''
    
    def get_len_name(self, object):
        length = len(object.name)
        return length
        
    def validate_name(self, name):
        if len(name) <= 1:
            raise serializers.ValidationError("Name is too short")
        return name
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name cannot be same as description")
        return data

    
    

