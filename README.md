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
pip3 install -r requirements.txt
```  

для работы понадобится файл `.env`, ниже его дефолтные значения для тестов:
```
SECRET_KEY='fa7zg0io9snm&1_4htv6b5(z86h-pntdfa=y=om4q!2m-t&e#j'
DEBUG=True
ALLOWED_HOSTS="*"
SECURE_HSTS_SECONDS=0
SECURE_HSTS_INCLUDE_SUBDOMAINS=False
SECURE_HSTS_PRELOAD=False
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```  
также можете указать свои значения для переменых:
- STATIC_ROOT
[подробнее об остальных настройках](https://docs.djangoproject.com/en/4.1/ref/settings/)  
для запуска в прод не забудьте выпустить уникальный SECRET_KEY 


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
python3 manage.py load_place -j {path_to_json}
```
> Примечание  
> {path_to_json} может быть:  
> - ссылкой, где content_type == application/json;  
> - относительным или абсолютным путем хранения JSON файла;  
> - папкой, содержащей в себе JSONы если их надо добавить несколько.    

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
