from notice.models import Notice
from rest_framework import serializers, exceptions


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'content']

        def save(self):
            new_notice = Notice(
                title =self.validated_data['title'],
                content = self.validated_data['content'],
            )

            new_notice.save()

            return new_notice
