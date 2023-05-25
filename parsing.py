import requests
import json
import re
import time
from bs4 import BeautifulSoup


def date_deciding(date):
    month = '12'
    day = '28'
    if 'янв' in date:
        month = '01'
    elif 'фев' in date:
        month = '02'
    elif 'мар' in date:
        month = '03'
    elif 'апр' in date:
        month = '04'
    elif 'мая' in date:
        month = '05'
    elif 'июн' in date:
        month = '06'
    elif 'июл' in date:
        month = '07'
    elif 'авг' in date:
        month = '08'
    elif 'сен' in date:
        month = '09'
    elif 'окт' in date:
        month = '10'
    elif 'ноя' in date:
        month = '11'
    elif 'дек' in date:
        month = '12'
    nums_only = re.sub('[^0-9]', '', date)
    if len(nums_only) == 1:
        day = '0' + nums_only
    else:
        day = nums_only
    return month + '-' + day


def parsing_by_city(city, code):
    domain_found = False
    for domain in ['.ru/', '.kz/', '.by/']:
        if not domain_found:
            base_link = 'https://afisha.yandex'
            if code == 1:
                link_pt2 = '/selections/concert-hot'
            else:
                link_pt2 = '/concert?source=menu'
            link = base_link + domain + city + link_pt2
            r = requests.get(link)
            print(link)
            print(r.history)
            if len(r.history) > 0:
                time.sleep(2)
                continue
            else:
                domain_found = True
            r = r.text
            soup = BeautifulSoup(r, 'html.parser')
            if 'captcha' in str(soup):
                print('капча в списке афиш(')
            all_events = soup.findAll('div', class_='i-react event-card-react i-bem')
            for event in all_events:
                event_as_str = str(event)
                right_index = event_as_str.index("}}'>")
                json_info = json.loads(event_as_str[54:right_index + 2])
                event_link = base_link + domain + json_info.get('event-card-react').get('props').get('link')[1:]
                time.sleep(3)
                print(event_link)
                event_req = requests.get(event_link).text
                event_soup = BeautifulSoup(event_req, 'html.parser')
                if 'captcha' in str(event_soup):
                    print('капча в афише(')
                artist_info = list(event_soup.findAll('a', class_='ChipClickable-sc-16vu6es-1 iQELwv'))
                artists = list()
                artists_photos = list()
                for artist in artist_info:
                    artist = str(artist)
                    link_index = artist.index('><span class="StyledChip-wr23a4-0 gvYMnn"')
                    artist_link = base_link + domain + artist[51:link_index - 1]
                    try:
                        name_left_index = artist.index('<img alt="')
                        name_right_index = artist.index('" class="StyledLogo-u88k37-0 cYGlYr"')
                        artists.append(artist[name_left_index + 10:name_right_index])
                        photo_left_index = artist.index('src="')
                        photo_right_index = artist.index('" srcset="')
                        artists_photos.append(artist[photo_left_index + 5:photo_right_index])
                    except:
                        name_left_index = artist.index('</span><div><div>')
                        name_right_index = artist.index('</div></div></span>')
                        artists.append(artist[name_left_index + 17:name_right_index])
                        artists_photos.append(
                            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrYO97QZyLAUdjVTXl8n2tzoce2lBmZMBf1g&usqp=CAU')

                if not artists:
                    continue
                else:
                    title = json_info.get('event-card-react').get('props').get('title')
                    event_type = all_event_types.index(json_info.get('event-card-react').get('props').get('tag')) + 2
                    age_restriction = all_age_categories.index(
                        int(json_info.get('event-card-react').get('props').get('ageLimit')[:-1])) + 1
                    dt = json_info.get('event-card-react').get('props').get('additionalInfo')
                    if dt == 'постоянно' or dt.count(':') != 1:
                        continue
                    elif dt.count(':') != 1:
                        continue
                    else:
                        print('здарова')
                        event_time = dt[-5:] + ':00'
                        date_non_format = dt[:-7]
                        if '202' in date_non_format:
                            date_non_format = date_non_format.replace('2024', '')
                            date = '2024-' + date_deciding(date_non_format)
                        else:
                            date = '2023-' + date_deciding(date_non_format)
                        photo_link = json_info.get('event-card-react').get('props').get('image').get('url')
                        place_link = base_link + domain + json_info.get('event-card-react').get('props').get(
                            'place').get('url')[1:]
                        place_title = json_info.get('event-card-react').get('props').get('place').get('title')
                        try:
                            place_type = all_place_types.index(
                                json_info.get('event-card-react').get('props').get('place').get('tags')[0]['code']) + 2
                        except IndexError:
                            continue
                        place_long = json_info.get('event-card-react').get('props').get('place').get('coordinates').get(
                            'longitude')
                        place_lat = json_info.get('event-card-react').get('props').get('place').get('coordinates').get(
                            'latitude')
                        address = json_info.get('event-card-react').get('props').get('place').get('address')
                        city_name = cities_ru.index(
                            json_info.get('event-card-react').get('props').get('place').get('city').get('name')) + 2
                        if domain == '.ru/':
                            try:
                                min_price = int(re.sub('[^0-9]', '', json_info.get('event-card-react').get('props').get(
                                    'ticketsPrice')))
                            except TypeError:
                                continue
                        elif domain == '.kz/':
                            try:
                                min_price = (0.18 * int(re.sub('[^0-9]', '',
                                                               json_info.get('event-card-react').get('props').get(
                                                                   'ticketsPrice')))) // 1
                            except TypeError:
                                continue
                        else:
                            try:
                                min_price = (31.68 * int(re.sub('[^0-9]', '',
                                                                json_info.get('event-card-react').get('props').get(
                                                                    'ticketsPrice')))) // 1
                            except TypeError:
                                continue
                        all_event_tags = json_info.get('event-card-react').get('props').get('statEntry').get(
                            'event_tags')
                        genres = [all_genres.index(genre) + 4 for genre in all_event_tags if genre in all_genres]
                        event_desc = str(event_soup.findAll('div', class_='concert-description__text-wrap')).replace('\n', ' ')[45:-7]
                        if event_desc == '':
                            event_desc = '-'
                        time.sleep(3)
                        artist_req = requests.get(artist_link).text
                        artist_soup = BeautifulSoup(artist_req, 'html.parser')
                        if 'captcha' in str(artist_soup):
                            print('капча в профиле артиста(')
                        artist_desc = str(
                            artist_soup.findAll('div', class_='person-seo-description__text text-fader__text')).replace('\n', ' ')[105:-7]
                        if artist_desc == '':
                            artist_desc = '-'
                        for i in range(len(artists)):
                            cur_artist = artists[i]
                            cur_artist_photo = artists_photos[i]
                            if cur_artist not in all_artists:
                                all_artists.add(cur_artist)
                                with open('artists.txt', 'a+') as artists_file:
                                    msg = '{"genre_id": ' + str(genres)
                                    msg += ', "performer_type_id": 2, "performer_name": "' + cur_artist + '", "performer_description": "' + artist_desc + '", "performer_photo_link": "' + cur_artist_photo + '"},' + '\n'
                                    print(msg)
                                    print('----')
                                    artists_file.write(msg)
                        if place_title not in all_places:
                            all_places.add(place_title)
                            with open('places.txt', 'a+') as places_file:
                                places_file.write('{"type_id": ' + str(place_type) + ', "city_id": ' + str(
                                    city_name) + ', "place_name": "' + place_title + '", "long": ' + str(
                                    place_long) + ', "lat": ' + str(
                                    place_lat) + ', "address": "' + address + '", "place_link": "' + place_link + '"},' + '\n')
                        with open('info.txt', 'a+') as f:
                            # f.write('{"event_name": "' + title + '", "event_type_name": "' + event_type + '", "age_min": ' + str(age_restriction) + ', "price_min": ' + str(min_price) + ', "event_date": ' + date + ', "event_time": ' + event_time + ', "event_link": "' + event_link + '", "event_photo_link": "' + photo_link + '", "event_description": "' + event_desc + '", "place_name": "' + place_title +  '", place_link": "' + place_link + '", "place_type_name": ' + str(place_types) + ', "long": ' + str(place_long) + ', "lat": ' + str(place_lat) + ', "address": "' + address + '", "genres": ' + str(genres) + '"performer_type_name": " "' + ', "performer_name": ' + str(artists) + ', "performer_description": "' + artist_desc + '", "performer_photo_link": ' + str(artists_photos) + ', "city_name": "' + city_name + '", "country": "' + country + '"},' + '\n')
                            # f.close()
                            f.write('{"performer_id": [' + str(title) + '], "age_category_id": ' + str(
                                age_restriction) + ', "event_type_id": ' + str(event_type) + ', "place_id": {' + str(
                                place_title) + '}, "event_name": "' + str(title) + '", "event_date": "' + str(
                                date) + '", "event_time": "' + str(event_time) + '", "event_description": "' + str(
                                event_desc) + '", "event_link": "' + str(event_link) + '", "price_min": ' + str(
                                min_price) + ', "event_photo_link": "' + str(photo_link) + '"},' + '\n')


all_event_types = ['hiphop', 'nearest-events', 'concert', 'chanson', 'pop', 'estrada', 'sport', 'show', 'metal', 'kids', 'rock', 'festival', 'on_air']
all_place_types = ['concert_hall', 'cultural_centre', 'sport_complex', 'exhibition_room', 'stadium', 'culture_hall', 'park', 'conference_room', 'theater_place', 'club', 'restaurant', 'art_cluster', 'bar', 'hotel', 'museum', 'entertainment_center']
all_genres = ['contemporary_classical_music', 'classical_music', 'alternative', 'rock', 'metal', 'hiphop', 'pop', 'estrada', 'jazz-blues', 'electronic', 'indie', 'neoclassica', 'standup', 'chanson']
selection_cities = ['moscow', 'saint-petersburg', 'perm', 'novosibirsk', 'yekaterinburg', 'kazan', 'nizhny-novgorod', 'chelyabinsk', 'omsk', 'krasnodar', 'rostov-na-donu', 'ufa', 'krasnoyarsk', 'volgograd']
other_cities = ['astana', 'minsk', 'voronezh', 'samara']
cities_ru = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Нижний Новгород', 'Челябинск', 'Омск', 'Краснодар', 'Ростов-на-Дону', 'Уфа', 'Красноярск', 'Пермь', 'Волгоград', 'Воронеж', 'Самара', 'Астана', 'Минск']
all_age_categories = [14, 18, 0, 6, 12, 16, 21]
all_artists = set()
all_places = set()
for city in other_cities:
    parsing_by_city(city, 2)
for city in selection_cities:
    parsing_by_city(city, 1)