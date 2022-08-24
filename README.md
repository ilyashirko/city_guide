# City Guide
Сервис отображения любимых мест на карте с админкой для модераторов.  
Фронтенд by [DEVMAN team](https://dvmn.org)  
Бэк by [IlyaShirko](https://github.com/ilyashirko)

## Установка
Понадобится python 3.*
```
git clone https://github.com/ilyashirko/city_guide &&
cd city_guide &&
python3 -m venv env &&
source env/bin/activate &&
pip3 install -r requirements.txt &&
```  

для работы понадобится файл .env:
```
SECRET_KEY=
DEBUG=True or False
ALLOWED_HOSTS=
SECURE_HSTS_SECONDS=0
SECURE_HSTS_INCLUDE_SUBDOMAINS=True or False
SECURE_HSTS_PRELOAD=True or False
SECURE_SSL_REDIRECT=True or False
SESSION_COOKIE_SECURE=True or False
CSRF_COOKIE_SECURE=True or False
```  

после добавления .env запускаем:
```
python3 manage.py migrate &&
python3 manage.py createsuperuser
```  

если миграция не создала модели place и image:
```
python3 manage.py migrate where_to_go
```
## Добавление локаций
Для добавления новой локации введите команду:
```
python3 manage.py load_place -j {path to json} or {url with content type == application/json} or {path with jsons}
```
Словарь должен быть формата:
```
{
    "title": str(),
    "imgs": [
        {url1},
        {url2},
        ...
    ],
    "description_short": str(),
    "description_long": str(),
    "coordinates": {
        "lng": str(),
        "lat": str()
    }
}
```

## Запуск
Для локального запуска:
```
python3 manage.py runserver
```
Вам потребуются данные для отображения на карте.  
Для этого зайдите в [админку](http://127.0.0.1:8000/admin) и создайте локации.  
Фотографии можете загрузить во время создания локации или отдельно.  
Упорядочить фотографии можно также создавая или редактируя локацию.

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде


## Демо-версия сайта
[City_Guide](https://ilyashirko.pythonanywhere.com/)