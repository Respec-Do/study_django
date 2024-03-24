from django.test import TestCase

from member.models import Member


class MemberTest(TestCase):
    # member = Member.objects.get(id=4)
    # member.member_status = 0
    # member.save()

    data = {
        'member_email' : 'manngu@gmail.com',
        'member_password' : '1234',
        'member_name' : '맹구',
        'member_phone' : '010-6544-4456'
    }

    member = Member(**data)
    member.save()