from rest_framework import serializers

from statistic.models import PageView


class PageViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageView
        fields = ('property', 'viewed_by', 'viewed_on')


class PageViewCountSerializer(serializers.Serializer):
    count = serializers.IntegerField(read_only=True)