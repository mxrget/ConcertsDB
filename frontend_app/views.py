from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.response import Response
from datetime import datetime

import requests
import json


class MainPageView(View):
    """Главная страница"""

    def get(self, request):
        req = requests.get('http://127.0.0.1:8000/api/v1/events/')

        if req.status_code == requests.codes.ok:
            concerts = req.json()

            if len(concerts) > 12:
                concerts = concerts[:12]

            concerts = sorted(concerts, key=lambda x:
                datetime.strptime(x["event_date"] + " " + x["event_time"], "%Y-%m-%d %H:%M:%S"))

            return render(request, "html/main_page.html", {"data": concerts})
        else:
            return Response(status=500)


class EventDetailView(View):
    """Информация об евенте"""

    def get(self, request, pk):
        req = requests.get('http://127.0.0.1:8000/api/v1/events/')

        if req.status_code == requests.codes.ok:
            concerts = req.json() # return

            event = list(filter(lambda x: x["id"] == pk, concerts))[0]
            event["place_id"]["long"] = str(event["place_id"]["long"]).replace(",", ".")
            event["place_id"]["lat"] = str(event["place_id"]["lat"]).replace(",", ".")

            event["event_time"] = str(event["event_time"])[:-3]

            return render(request, "html/event_detail.html", {"event": event})
        else:
            return Response(status=500)


class PerformerView(View):
    """Информация о выступающем"""

    def get(self, request, pk):
        req = requests.get('http://127.0.0.1:8000/api/v1/events/')


        if req.status_code == requests.codes.ok:
            concerts = req.json() # return

            events_with_performer = \
                list(filter(lambda x: len(list(filter(lambda z: z["id"] == pk, x["performer_id"]))) != 0, concerts))

            performer = list(filter(lambda x: x["id"] == pk, events_with_performer[0]["performer_id"]))[0]

            events_with_performer = sorted(events_with_performer, key=lambda x:
                datetime.strptime(x["event_date"] + " " + x["event_time"], "%Y-%m-%d %H:%M:%S"))

            data = {"performer": performer, "events_with_performer": events_with_performer}

            return render(request, "html/performer_detail.html", data)
        else:
            return Response(status=500)


class SearchView(View):
    """Страница поиска"""

    def get(self, request):
        req = requests.get('http://127.0.0.1:8000/api/v1/events/')

        def searchfilter(event, key_stroke):
            key_stroke = key_stroke.lower()

            look_for_data = []

            look_for_data.append(event["event_name"].lower())
            look_for_data.append(event["event_description"].lower())
            look_for_data.append(event["event_type_id"]["event_type_name"].lower())
            look_for_data.append(event["place_id"]["place_name"].lower())
            look_for_data.append(event["place_id"]["type_id"]["place_type_name"].lower())
            look_for_data.append(event["place_id"]["city_id"]["city_name"].lower())
            look_for_data.append(event["place_id"]["city_id"]["country"].lower())
            look_for_data.append(" ".join(list(map(lambda x: x["performer_name"], event["performer_id"]))).lower())
            look_for_data.append(" ".join(list(map(lambda x: x["performer_description"], event["performer_id"]))).lower())
            look_for_data.append(" ".join(list(map(lambda x: x["performer_type_id"]["performer_type_name"], event["performer_id"]))).lower())

            event_performer_generes = []

            for performer in event["performer_id"]:
                event_performer_generes += list(map(lambda x: x["genre_name"], performer["genre_id"]))

            look_for_data.append(" ".join(event_performer_generes))

            return key_stroke in " ".join(look_for_data).lower()

        if req.status_code == requests.codes.ok:
            concerts = req.json() # return

            query = str(self.request.GET.get('search-field'))

            if query == "None" or query == "":
                status = 'Вы ввели пустой поисковой запрос. Попробуйте "Кино" или "Рок"'

            else:
                concerts = list(filter(lambda x: searchfilter(x, query), concerts))

                if not concerts:
                    status = 'К сожалению, по вашему запросу "' + query + '" ничего не найдено'

                else:
                    status = 'Вот, что удалось найти запросу "' + query + '"'

            concerts = sorted(concerts, key=lambda x:
                datetime.strptime(x["event_date"] + " " + x["event_time"], "%Y-%m-%d %H:%M:%S"))

            return render(request, "html/search.html", {"data": concerts, "status": status})
        else:
            return Response(status=500)


class AllEventsView(View):
    """Список всех событий"""

    def get(self, request):
        req = requests.get('http://127.0.0.1:8000/api/v1/events/')

        if req.status_code == requests.codes.ok:
            concerts = req.json() # return

            age_filter_var = []
            type_filter_var = []
            city_filter_var = []
            genre_filter_var = []

            for event in concerts:
                age = {"option": event["age_category_id"]["age"], "id": event["age_category_id"]["id"]}

                if age not in age_filter_var:
                    age_filter_var.append(age)

                type = {"option": event["event_type_id"]["event_type_name"], "id": event["event_type_id"]["id"]}

                if type not in type_filter_var:
                    type_filter_var.append(type)

                city = {"option": event["place_id"]["city_id"]["city_name"], "id": event["place_id"]["city_id"]["id"]}

                if city not in city_filter_var:
                    city_filter_var.append(city)

                for performer in event["performer_id"]:
                    for genre in performer["genre_id"]:
                        if {"option": genre["genre_name"], "id": genre["id"]} not in genre_filter_var:
                            genre_filter_var.append({"option": genre["genre_name"], "id": genre["id"]})

            age_filter_var = sorted(age_filter_var, key=lambda x: x["option"])
            type_filter_var = sorted(type_filter_var, key=lambda x: x["option"])
            city_filter_var = sorted(city_filter_var, key=lambda x: x["option"])
            genre_filter_var = sorted(genre_filter_var, key=lambda x: x["option"])

            query_date = str(self.request.GET.get('date-input'))

            try:
                query_age = int(self.request.GET.get('age-category-input'))
            except:
                query_age = 0

            try:
                query_type = int(self.request.GET.get('event-type-input'))
            except:
                query_type = 0

            try:
                query_city = int(self.request.GET.get('event-city-input'))
            except:
                query_city = 0

            try:
                query_genre = int(self.request.GET.get('genre-input'))
            except:
                query_genre = 0

            concerts_to_show = []

            for event in concerts:
                date_filter = query_date == "" or event["event_date"] == query_date
                age_filter = query_age == 0 or event["age_category_id"]["id"] == query_age
                type_filter = query_type == 0 or event["event_type_id"]["id"] == query_type
                city_filter = query_city == 0 or event["place_id"]["city_id"]["id"] == query_city

                event_geners = []

                for performer in event["performer_id"]:
                    for genre in performer["genre_id"]:
                        if genre["id"] not in event_geners:
                            event_geners.append(genre["id"])

                genre_filter = query_genre == 0 or query_genre in event_geners

                if genre_filter and date_filter and age_filter and type_filter and city_filter:
                    concerts_to_show.append(event)

            if len(concerts_to_show) == 0:
                status = "К сожалению мы не смогли найти подходящих событий"

            else:
                status = ""

            concerts_to_show = sorted(concerts_to_show, key=lambda x:
                datetime.strptime(x["event_date"] + " " + x["event_time"], "%Y-%m-%d %H:%M:%S"))

            context = {
                "data": concerts_to_show,
                "status": status,
                "age_filter_var": age_filter_var,
                "type_filter_var": type_filter_var,
                "city_filter_var": city_filter_var,
                "genre_filter_var": genre_filter_var,
            }

            return render(request, "html/all-events.html", context)
        else:
            return Response(status=500)


class AboutView(View):
    """Информация о проекте"""

    def get(self, request):
        return render(request, "html/about.html")


def PageNotFoundView(request, exception):
    "Заглушка 404"

    return render(request, 'html/404.html', status=404)
