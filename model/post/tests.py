from random import random
from random import randint

from django.db.models import Count
from django.test import TestCase

from member.models import Member
from post.models import Post


class PostTest(TestCase):
    # posts = []
    # # 랜덤한 회원을 작성자로 설정하기
    # member_queryset = Member.objects.all()
    # # 총 98개 게시글 작성하기
    # for i in range(98):
    #     post = {
    #         'post_title': f'테스트 제목{i+1}',
    #         'post_content': f'테스트 내용{i+1}',
    #         'member' : member_queryset[randint(1, len(member_queryset))-1]
    #
    #     }
    #     # posts.append(post)
    #     # 트러블 슈팅
    #     # Error: AttributeError: 'dict' object has no attribute 'pk'
    #
    #     # dict객체를 Django ORM에 전달하면 정확히 인식이 안되었다.
    #     # 이를 모델 객체에 담아서 전달하니 정확히 인식되었다.
    #
    #     posts.append(Post(**post))
    # Post.objects.bulk_create(posts)

    # 로그인된 회원의 마이페이지에서 내가 작성한 게시글 조회하기

    # member = Member.objects.get(member_status=True, id=3)
    # for post in member.post_set.all():
    #     print(post)

    # 나이가 30 미만인 회원이 작성한 게시글 목록 조회
    # 단, 회원의 이름과 회원의 나이까지 같이 조회하기

    # 1. 정방향으로 직접 참조
    # 2. (member__member_name, member__member_age)
    # members = Member.objects.filter(member_age__lt=30)
    # posts = Post.objects.filter(member_id__in=members)
    # for post in posts:
    #     print(post.post_title, post.post_content, post.member.member_name, post.member.member_age)
    #
    # members = Member.objects.filter(member_age__lt=30)
    # for member in members:
    #     print(member.post_set.values_list(), member.member_name, member.member_age)


    # 문제 답
    # posts = Post.objects.filter(member__member_age__lt=30)
    # for post in posts:
    #     print(post.pk, post.post_title, post.post_content, post.member.member_name, post.member.member_age)

    # 한번에 참조(member__member_name, memeber__member_age)
    # posts = Post.objects.filter(member__member_age__lt=30).values('id', 'post_title', 'post_content', 'member__member_name', 'member__member_age')
    # print(posts.query)
    # for post in posts:
    #     print(post)

    # LAZY 와 EAGER


    # EAGER(즉시)
    # 실행하는 순간 쿼리가 실행된 뒤, 이후 쿼리가 발생하지 않는다.
    # 하나의 서비스에서 여러 번 JOIN해야 할 경우 사용한다.

    # post = Post.objects.select_related('member').all()
    # print(post.__dict__)

    # A 필드에 b가 있다고 가정한다.
    # a.b : (정방향) a로 b필드에 접근하면 정방향 참조이고, b의 null 상태에 따라 내부 또는 외부 조인이 실행된다.
    # b.a : (역방향) b로 a필드에 접근하면 역방향 참조이고, b의 모든 정보가 나와야하기 때문에 항상 외부조인이 실행된다.

    # LAZY(지연)
    # 실행할 때 쿼리가 만들어지고, 필드에 접근할 때 마다 쿼리가 발생한다.
    # print(Post.objects.values('member__member_name').query)
    # print(Member.objects.values('post__post_title').query)

    # 게시글을 작성한 회원 중에서 게시글을 5개 이상 작성한 회원 찾기
    # print(Post.objects.filter(post_title__contains=3).count())
    # posts = Post.objects.values(
    #     'member_id',
    #     'member__member_name',
    #     'member__member_age',
    #     'member__member_email'
    # ).annotate(member_count = Count('member_id'))\
    # .filter(member_count__gte=5)
    #
    # for post in posts:
    #     print(post)

    pass