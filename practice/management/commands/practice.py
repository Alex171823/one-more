from random import randint

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User as User
from django.core.management.base import BaseCommand

from faker import Faker

from practice.models import Comments, Posts

fake = Faker()


class Command(BaseCommand):
    help = u'Fills database with some data'  # noqa A003

    # fills db with 10 publishers, 15 stores and 20 authors
    def handle(self, *args, **kwargs):
        # clear database
        # Films.objects.all().delete()
        # People.objects.all().delete()

        # create 100 users
        self.stdout.write('creating users')
        for i in range(1, 10):
            User.objects.create(username=fake.name(), password=make_password(fake.password()), is_staff=0)
            self.stdout.write(f'user created {i}')

        # create up to 10 posts for each user
        self.stdout.write('creating posts')
        posts = []
        for user in User.objects.all():
            for i in range(1, 11):
                posts.append(Posts(post_text=fake.text(),
                                   short_description=fake.text(),
                                   full_description=fake.text(),
                                   picture="./" + fake.word(),
                                   is_draft=randint(0, 1),
                                   user=user))
        Posts.objects.bulk_create(posts)
        self.stdout.write('posts created')

        # add 10 comments to each post
        self.stdout.write('creating comments')
        comments = []
        for post in Posts.objects.all():
            for i in range(1, 11):
                comments.append(Comments(text=fake.text(),
                                         username=fake.name(),
                                         post=post))
        Comments.objects.bulk_create(comments)
