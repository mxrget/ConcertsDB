# ConcertsDB
ConcertsDB - сайт афиша, на котором хранится информация о концертах и различных ближайших выступлениях в 16 городах-миллиониках по всей России, а также в Астане и Минске. База данных составлена на основании ресурса Яндекс Афиша (https://afisha.yandex.ru/), откуда мы брали информацию путем парсинга.   
Сам сайт написан полностью на языке Python, для фронтенда использовался html и css. За бэкенд отвечает библиотека Django, как веб-фреймворк, и djangorestframework, фреймворк для разработки API. Для парсинга Яндекс афиши использовались библиотеки beautifulsoup и requests, а для фронтенда дополнительно был использован Bootstrap. 
На ГитХабе можно найти все исходные файлы нашего проекта, которые рабиты на несколько веток. Пояснения для каждой ветки:
* concertsdb - папка где хранятся основные файлы основного приложения django. На Гитхаб загружены не все, только то, что было изменено. Содержание остальных файлов по умолчанию.
* frontend_app - приложение django, нужное для создания фронтенда.
* project_files - основная папка проекта, где находятся настройки django и ссылки на апи и на административную панель.
* static - статичные файлы для фронтенда, такие как css и фото.
* templates - основной фронтенд, файлы html.
 
