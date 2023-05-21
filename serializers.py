from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PerformerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformerType
        fields = '__all__'


class PerformerListSerializer(serializers.ModelSerializer):
    genre_id = GenreSerializer(read_only=True, many=True)
    performer_type_id = PerformerTypeSerializer(read_only=True)

    class Meta:
        model = Performer
        fields = '__all__'


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'


class AgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeCategory
        fields = '__all__'


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'


class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceType
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class PlaceListSerializer(serializers.ModelSerializer):
    type_id = PlaceTypeSerializer(read_only=True)
    city_id = CitySerializer(read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    performer_id = PerformerListSerializer(read_only=True, many=True)
    age_category_id = AgeCategorySerializer(read_only=True)
    event_type_id = EventTypeSerializer(read_only=True)
    place_id = PlaceListSerializer(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
