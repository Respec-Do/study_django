from rest_framework import serializers

from member.models import Member
from post.models import Post


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        # 파이썬 데이터를 JSON타입(문자열)의 데이터로 변환해줌.