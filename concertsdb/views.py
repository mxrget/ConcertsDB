from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class EventListView(APIView):
    """Get list of events"""

    def get(self, request):
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)


class EventDetailView(APIView):
    """Get event by id"""

    def get(self, request, pk):
        ev = Event.objects.get(id=pk)
        serializer = EventListSerializer(ev)
        return Response(serializer.data)


class EventCreateView(APIView):
    """Create event"""
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def post(self, request):
        event = EventSerializer(data=request.data)
        if event.is_valid():
            event.save()
        return Response(status=201)


class EventUpdateView(APIView):
    """Update event"""
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def put(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
        except:
            return Response(status=404)
        event_s = EventSerializer(event, data=request.data)
        if event_s.is_valid():
            event_s.save()
            return Response(status=201)
        return Response(status=400)


class EventDeleteView(APIView):
    """delete event"""

    def delete(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
        except:
            return Response(status=404)
        event.delete()
        return Response(status=204)


class PerformerListView(APIView):
    """Get list of performers"""

    def get(self, request):
        performers = Performer.objects.all()
        serializer = PerformerListSerializer(performers, many=True)
        return Response(serializer.data)


class PerformerDetailView(APIView):
    """Get performer by id"""

    def get(self, request, pk):
        per = Performer.objects.get(id=pk)
        serializer = PerformerListSerializer(per)
        return Response(serializer.data)


class PerformerCreateView(APIView):
    """Create performer"""
    serializer_class = PerformerSerializer
    queryset = Performer.objects.all()

    def post(self, request):
        performer = PerformerSerializer(data=request.data)
        if performer.is_valid():
            performer.save()
        return Response(status=201)


class PerformerUpdateView(APIView):
    """Update performer"""
    serializer_class = PerformerSerializer
    queryset = Performer.objects.all()

    def put(self, request, pk):
        try:
            performer = Performer.objects.get(id=pk)
        except:
            return Response(status=404)
        performer_s = PerformerSerializer(performer, data=request.data)
        if performer_s.is_valid():
            performer_s.save()
            return Response(status=201)
        return Response(status=400)


class PerformerDeleteView(APIView):
    """delete performer"""

    def delete(self, request, pk):
        try:
            performer = Event.objects.get(id=pk)
        except:
            return Response(status=404)
        performer.delete()
        return Response(status=204)


class AgeCategoryListView(APIView):
    """Get list of age categories"""

    def get(self, request):
        age_categories = AgeCategory.objects.all()
        serializer = AgeCategorySerializer(age_categories, many=True)
        return Response(serializer.data)


class AgeCategoryDetailView(APIView):
    """Get age category by id"""

    def get(self, request, pk):
        age_category = AgeCategory.objects.get(id=pk)
        serializer = AgeCategorySerializer(age_category)
        return Response(serializer.data)


class AgeCategoryCreateView(APIView):
    """Create age category"""
    serializer_class = AgeCategorySerializer
    queryset = AgeCategory.objects.all()

    def post(self, request):
        age_category = AgeCategorySerializer(data=request.data)
        if age_category.is_valid():
            age_category.save()
        return Response(status=201)


class AgeCategoryUpdateView(APIView):
    """Update age category"""
    serializer_class = AgeCategorySerializer
    queryset = AgeCategory.objects.all()

    def put(self, request, pk):
        try:
            age_category = AgeCategory.objects.get(id=pk)
        except:
            return Response(status=404)
        age_category_s = AgeCategorySerializer(age_category, data=request.data)
        if age_category_s.is_valid():
            age_category_s.save()
            return Response(status=201)
        return Response(status=400)


class AgeCategoryDeleteView(APIView):
    """delete age category"""

    def delete(self, request, pk):
        try:
            age_category = AgeCategory.objects.get(id=pk)
        except:
            return Response(status=404)
        age_category.delete()
        return Response(status=204)


class CityListView(APIView):
    """Get list of cities"""

    def get(self, request):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)


class CityDetailView(APIView):
    """Get city by id"""

    def get(self, request, pk):
        city = City.objects.get(id=pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)


class CityCreateView(APIView):
    """Create city"""
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def post(self, request):
        city = CitySerializer(data=request.data)
        if city.is_valid():
            city.save()
        return Response(status=201)


class CityUpdateView(APIView):
    """Update city"""
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def put(self, request, pk):
        try:
            city = City.objects.get(id=pk)
        except:
            return Response(status=404)
        city_s = CitySerializer(city, data=request.data)
        if city_s.is_valid():
            city_s.save()
            return Response(status=201)
        return Response(status=400)


class CityDeleteView(APIView):
    """delete city"""

    def delete(self, request, pk):
        try:
            city = City.objects.get(id=pk)
        except:
            return Response(status=404)
        city.delete()
        return Response(status=204)


class PlaceTypeListView(APIView):
    """Get list of place types"""

    def get(self, request):
        place_type = PlaceType.objects.all()
        serializer = PlaceTypeSerializer(place_type, many=True)
        return Response(serializer.data)


class PlaceTypeDetailView(APIView):
    """Get place type by id"""

    def get(self, request, pk):
        place_type = PlaceType.objects.get(id=pk)
        serializer = PlaceTypeSerializer(place_type)
        return Response(serializer.data)


class PlaceTypeCreateView(APIView):
    """Create place type"""
    serializer_class = PlaceTypeSerializer
    queryset = PlaceType.objects.all()

    def post(self, request):
        place_type = PlaceTypeSerializer(data=request.data)
        if place_type.is_valid():
            place_type.save()
        return Response(status=201)


class PlaceTypeUpdateView(APIView):
    """Update place type"""
    serializer_class = PlaceTypeSerializer
    queryset = PlaceType.objects.all()

    def put(self, request, pk):
        try:
            place_type = PlaceType.objects.get(id=pk)
        except:
            return Response(status=404)
        place_type_s = PlaceTypeSerializer(place_type, data=request.data)
        if place_type_s.is_valid():
            place_type_s.save()
            return Response(status=201)
        return Response(status=400)


class PlaceTypeDeleteView(APIView):
    """delete place type"""

    def delete(self, request, pk):
        try:
            place_type = PlaceType.objects.get(id=pk)
        except:
            return Response(status=404)
        place_type.delete()
        return Response(status=204)


class PlaceListView(APIView):
    """Get list of places"""

    def get(self, request):
        place = Place.objects.all()
        serializer = PlaceListSerializer(place, many=True)
        return Response(serializer.data)


class PlaceDetailView(APIView):
    """Get places by id"""

    def get(self, request, pk):
        place = Place.objects.get(id=pk)
        serializer = PlaceListSerializer(place)
        return Response(serializer.data)


class PlaceCreateView(APIView):
    """Create place"""
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def post(self, request):
        place = PlaceSerializer(data=request.data)
        if place.is_valid():
            place.save()
        return Response(status=201)


class PlaceUpdateView(APIView):
    """Update place"""
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def put(self, request, pk):
        try:
            place = Place.objects.get(id=pk)
        except:
            return Response(status=404)
        place_s = PlaceSerializer(place, data=request.data)
        if place_s.is_valid():
            place_s.save()
            return Response(status=201)
        return Response(status=400)


class PlaceDeleteView(APIView):
    """delete place"""

    def delete(self, request, pk):
        try:
            place = Place.objects.get(id=pk)
        except:
            return Response(status=404)
        place.delete()
        return Response(status=204)


class GenreListView(APIView):
    """Get list of genres"""

    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)


class GenreDetailView(APIView):
    """Get gernes by id"""

    def get(self, request, pk):
        genre = Genre.objects.get(id=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


class GenreCreateView(APIView):
    """Create genre"""
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def post(self, request):
        genre = GenreSerializer(data=request.data)
        if genre.is_valid():
            genre.save()
        return Response(status=201)


class GenreUpdateView(APIView):
    """Update genre"""
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def put(self, request, pk):
        try:
            genre = Genre.objects.get(id=pk)
        except:
            return Response(status=404)
        genre_s = GenreSerializer(genre, data=request.data)
        if genre_s.is_valid():
            genre_s.save()
            return Response(status=201)
        return Response(status=400)


class GenreDeleteView(APIView):
    """delete genre"""

    def delete(self, request, pk):
        try:
            genre = Genre.objects.get(id=pk)
        except:
            return Response(status=404)
        genre.delete()
        return Response(status=204)


class PerformerTypeListView(APIView):
    """Get list of performer types"""

    def get(self, request):
        performer_type = PerformerType.objects.all()
        serializer = PerformerTypeSerializer(performer_type, many=True)
        return Response(serializer.data)


class PerformerTypeDetailView(APIView):
    """Get performer type by id"""

    def get(self, request, pk):
        performer_type = PerformerType.objects.get(id=pk)
        serializer = PerformerTypeSerializer(performer_type)
        return Response(serializer.data)


class PerformerTypeCreateView(APIView):
    """Create performer type"""
    serializer_class = PerformerTypeSerializer
    queryset = PerformerType.objects.all()

    def post(self, request):
        performer_type = PerformerTypeSerializer(data=request.data)
        if performer_type.is_valid():
            performer_type.save()
        return Response(status=201)


class PerformerTypeUpdateView(APIView):
    """Update performer type"""
    serializer_class = PerformerTypeSerializer
    queryset = PerformerType.objects.all()

    def put(self, request, pk):
        try:
            performer_type = PerformerType.objects.get(id=pk)
        except:
            return Response(status=404)
        performer_type_s = PerformerTypeSerializer(performer_type, data=request.data)
        if performer_type_s.is_valid():
            performer_type_s.save()
            return Response(status=201)
        return Response(status=400)


class PerformerTypeDeleteView(APIView):
    """delete performer type"""

    def delete(self, request, pk):
        try:
            performer_type = PerformerType.objects.get(id=pk)
        except:
            return Response(status=404)
        performer_type.delete()
        return Response(status=204)


class EventTypeListView(APIView):
    """Get list of event types"""

    def get(self, request):
        event_type = EventType.objects.all()
        serializer = EventTypeSerializer(event_type, many=True)
        return Response(serializer.data)


class EventTypeDetailView(APIView):
    """Get event type by id"""

    def get(self, request, pk):
        event_type = EventType.objects.get(id=pk)
        serializer = EventTypeSerializer(event_type)
        return Response(serializer.data)


class EventTypeCreateView(APIView):
    """Create event type"""
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()

    def post(self, request):
        event_type = EventTypeSerializer(data=request.data)
        if event_type.is_valid():
            event_type.save()
        return Response(status=201)


class EventTypeUpdateView(APIView):
    """Update event type"""
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()

    def put(self, request, pk):
        try:
            event_type = EventType.objects.get(id=pk)
        except:
            return Response(status=404)
        event_type_s = EventTypeSerializer(event_type, data=request.data)
        if event_type_s.is_valid():
            event_type_s.save()
            return Response(status=201)
        return Response(status=400)


class EventTypeDeleteView(APIView):
    """delete event type"""

    def delete(self, request, pk):
        try:
            event_type = EventType.objects.get(id=pk)
        except:
            return Response(status=404)
        event_type.delete()
        return Response(status=204)

