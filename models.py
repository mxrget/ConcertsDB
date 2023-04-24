from django.db import models


class City(models.Model):
    name = models.TextField('Город')
    country = models.TextField('Страна')


class PlaceType(models.Model):
    name = models.TextField('Тип места')


class Place(models.Model):
    name = models.TextField('Название площадки')
    long = models.TextField('Длительность мероприятия')
    lat = models.TextField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField('Адресс')
    type_id = models.ForeignKey(PlaceType, on_delete=models.CASCADE)
    link = models.URLField('Ссылка на место')


class Genre(models.Model):
    name = models.TextField('Жанр')


class ArtistType(models.Model):
    name = models.TextField('Тип артиста')


class Artist(models.Model):
    name = models.TextField('Имя артиста')
    genre = models.ManyToManyField(Genre)
    artist_type_id = models.ForeignKey(ArtistType, on_delete=models.CASCADE)


class EventType(models.Model):
    name = models.TextField('Тип мероприятия')


class AgeCategory(models.Model):
    min = models.IntegerField('Минимальный возраст')
    write = models.TextField()


class Price(models.Model):
    min = models.IntegerField('Минимальная цена')


class Event(models.Model):
    name = models.TextField('Название мероприятия')
    date = models.DateField('Дата проведения')
    time = models.TimeField('Время проведения')
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    artist_id = models.ManyToManyField(Artist)
    link = models.URLField('Ссылка на мероприятие')
    age_category_id = models.ForeignKey(AgeCategory, on_delete=models.CASCADE)
    event_type_id = models.ForeignKey(EventType, on_delete=models.CASCADE)
    price_id = models.ForeignKey(Price, on_delete=models.CASCADE)
