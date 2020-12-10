from rest_framework import serializers

from blog.models import New, NewsName
from user.models import User


class NewsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsName
        fields = [
            'language',
            'title',
            'description'
        ]


class NewsAddSerializer(serializers.ModelSerializer):

    news_name = NewsNameSerializer(many=True,required=True)

    class Meta:
        model = New
        fields = [
            'tags',
            'author',
            'news_name',
        ]

    def create(self, validated_data):
        news = validated_data.pop('news_name')
        tags = validated_data.pop("tags")
        news_object = New.objects.create(**validated_data)
        for tag in tags:
            news_object.tags.add(tag)
        for new in news:
            NewsName.objects.create(news=news_object, **new)
        return news_object

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags")
        instance.tags.set(tags)
        author = validated_data.pop("author")
        instance.author = author
        news_name = NewsName.objects.filter(
            news=instance
        )
        news_name.delete()
        news = validated_data.pop("news_name")
        for new in news:
            NewsName.objects.create(news=instance, **new)
        return instance