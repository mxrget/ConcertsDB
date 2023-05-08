from django.db import models


class City(models.Model):
    city_name = models.CharField('city', max_length=60)
    country = models.CharField('country', max_length=200)

    def __str__(self):
        return str(self.city_name)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class PlaceType(models.Model):
    place_type_name = models.CharField('place type', max_length=100)

    def __str__(self):
        return str(self.place_type_name)

    class Meta:
        verbose_name = 'Площадка проведения'
        verbose_name_plural = 'Площадки проведения'


class Place(models.Model):
    place_name = models.CharField('place name', max_length=250)
    long = models.FloatField('longtitude')
    lat = models.FloatField('latitude')
    address = models.CharField('address', max_length=300)
    place_link = models.URLField('Place URL')
    type_id = models.ForeignKey(PlaceType, on_delete=models.CASCADE, verbose_name='place type')
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='place city')

    def __str__(self):
        return str(self.place_name)

    class Meta:
        verbose_name = 'Место проведения'
        verbose_name_plural = 'Места проведения'


class Genre(models.Model):
    genre_name = models.CharField('genre', max_length=100)

    def __str__(self):
        return str(self.genre_name)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class PerformerType(models.Model):
    performer_type_name = models.CharField('performer type', max_length=50)

    def __str__(self):
        return str(self.performer_type_name)

    class Meta:
        verbose_name = 'Тип исполнителей'
        verbose_name_plural = 'Типы исполнителей'


class Performer(models.Model):
    performer_name = models.CharField('performer name', max_length=200)
    performer_description = models.TextField('performer description')
    performer_photo_link = models.URLField('performer photo url')
    genre_id = models.ManyToManyField(Genre, verbose_name='genre list')
    performer_type_id = models.ForeignKey(PerformerType, on_delete=models.CASCADE, verbose_name='performer type')

    def __str__(self):
        return str(self.performer_name)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class EventType(models.Model):
    event_type_name = models.CharField('event type', max_length=100)

    def __str__(self):
        return str(self.event_type_name)

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы события'


class AgeCategory(models.Model):
    age = models.IntegerField('age')

    def __str__(self):
        return str(self.age)

    class Meta:
        verbose_name = 'Возрастное ограничение'
        verbose_name_plural = 'Возрастные ограничения'


class Event(models.Model):
    event_name = models.CharField('event name', max_length=150)
    event_date = models.DateField('date')
    event_time = models.TimeField('time')
    event_description = models.TextField('event description')
    event_link = models.URLField('event url')
    price_min = models.IntegerField('minimum price')
    event_photo_link = models.URLField('event photo url')
    age_category_id = models.ForeignKey(AgeCategory, on_delete=models.CASCADE, verbose_name='minimum age')
    event_type_id = models.ForeignKey(EventType, on_delete=models.CASCADE, verbose_name='event type')
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='place')
    performer_id = models.ManyToManyField(Performer, verbose_name='performers')

    def __str__(self):
        return str(self.event_name)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'