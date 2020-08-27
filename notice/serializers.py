from notice.models import Notice
from rest_framework import serializers, exceptions


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'content']
