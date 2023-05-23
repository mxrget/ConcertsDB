from django.contrib import admin
from .models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'country')
    list_display_links = ('city_name',)
    search_fields = ('city_name', 'country')
    list_filter = ('country', 'city_name')


@admin.register(PlaceType)
class PlaceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_type_name')
    list_display_links = ('place_type_name',)
    search_fields = ('place_type_name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'address', 'type_id', 'city_id')
    list_display_links = ('place_name',)
    search_fields = ('place_name', 'address', 'type_id__place_type_name', 'city_id__city_name')
    list_filter = ('type_id__place_type_name', 'city_id__city_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name')
    list_display_links = ('genre_name',)
    search_fields = ('genre_name',)
    list_filter = ('genre_name', )


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = ('id', 'performer_name', 'get_genre', 'performer_type_id')
    list_display_links = ('performer_name',)
    search_fields = ('performer_name', 'genre_id__genre_name', 'performer_type_id__performer_type_name')
    list_filter = ('performer_type_id__performer_type_name', 'genre_id__genre_name')


@admin.register(PerformerType)
class PerformerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'performer_type_name')
    list_display_links = ('performer_type_name',)
    search_fields = ('performer_type_name',)
    list_filter = ('performer_type_name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'event_date', 'price_min', 'age_category_id', 'get_performer')
    list_display_links = ('event_name',)
    search_fields = ('event_name', 'event_date', 'performer_id__performer_name')
    list_filter = ('event_date', 'price_min', 'age_category_id__age')


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_type_name')
    list_display_links = ('event_type_name',)
    search_fields = ('event_type_name',)


@admin.register(AgeCategory)
class AgeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'age')
    list_display_links = ('age',)
    search_fields = ('age',)
    list_filter = ('age',)
