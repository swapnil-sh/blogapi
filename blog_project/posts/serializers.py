
# DRF takes care of the heavy lifting of transforming our database models into a RESTful API.
# There are two main steps to this process: first, a serializer is used to transform the data into JSON so it can be sent over the internet, then a View is used to define what data is sent.

from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post