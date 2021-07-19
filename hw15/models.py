from django.db import models


class Films(models.Model):
    name = models.CharField(max_length=30)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name}"


class People(models.Model):
    name = models.CharField(max_length=30)
    date_birth = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.date_birth} {self.age}"


class PeopleFilmsManyToMany(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person} {self.film}"
