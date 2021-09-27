from rest_framework import serializers
from .models import Post, Vote

# create a serializer for each model

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = 'poster.username')
    poster_id = serializers.ReadOnlyField(source = 'poster.id')
    votes = serializers.SerializerMethodField()


    #what fields do you want associated with the API?
    #can also add some additional properties
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'poster_id', 'created', 'votes']
    
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
        class Meta:
            model = Vote
            fields = ['id']