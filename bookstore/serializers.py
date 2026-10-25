from rest_framework import serializers
from .models import Books, Author

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)

            return user


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.get_absolute_uri(obj.image.url)
        return None
