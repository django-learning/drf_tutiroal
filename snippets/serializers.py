from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={"base_templates": "textarea.html"})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")

    def create(self, validated_data):
        return Snippet.objects.create(validated_data)

    def update(self, instance, valdiated_data):
        instance.title = valdiated_data.get("title", instance.title)
        instance.code = valdiated_data.get("code", instance.title)
        instance.linenos = valdiated_data.get("linenos", instance.title)
        instance.language = valdiated_data.get("language", instance.title)
        instance.style = valdiated_data.get("style", instance.title)
        instance.save()
        return instance
