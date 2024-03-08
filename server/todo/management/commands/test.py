from models import User

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    自定义命令
    """

    def handle(self, *args, **options):
        """
        自定义命令
        :return:
        """
        print(123456789)
        User.objects.create(**{'user_name':'小黄鱼'})
        with open('thisisdingshitest.f','a+') as f:
            f.write('1234\n')
