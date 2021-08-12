from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from hw15.models import Films, People, PeopleFilmsManyToMany

fake = Faker()


class Command(BaseCommand):
    help = u'Fills database with some data'  # noqa A003

    # fills db with 10 publishers, 15 stores and 20 authors
    def handle(self, *args, **kwargs):
        # clear database
        # Films.objects.all().delete()
        # People.objects.all().delete()

        # create 10000 films
        self.stdout.write('creating films')
        films = [Films(name=fake.word().title(), release_date=fake.date()) for i in range(1, 10001)]
        Films.objects.bulk_create(films)
        self.stdout.write('films created')

        # create 50000 people
        self.stdout.write("creating people")
        people = []
        for i in range(50000):
            people.append(People(name=fake.name(),
                                 date_birth=fake.date(),
                                 age=randint(0, 100)))
        People.objects.bulk_create(people)
        self.stdout.write('people created')

        # add from 0 to 10 films for each person
        self.stdout.write('creating dependencies')
        for person in People.objects.all():
            films_people = []
            for i in range(1, randint(1, 11)):
                films_people.append(PeopleFilmsManyToMany(person=person,
                                                          film=Films.objects.get(id=randint(1, 10000))))
            PeopleFilmsManyToMany.objects.bulk_create(films_people)
        self.stdout.write('dependencies set')
