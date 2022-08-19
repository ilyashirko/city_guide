# City Guide
Сервис отображения любимых мест на карте с админкой для модераторов.
Фронтенд by [DEVMAN team](https://dvmn.org)
Бэк by [IlyaShirko](https://github.com/ilyashirko)

## Установка
Понадобится python 3.*
```
git clone https://github.com/ilyashirko/city_guide && cd city_guide &&
python3 -m venv env && source env/bin/activate && pip3 install -r requirements.txt &&
python3 manage.py migrate && python3 manage.py createsuperuser
```

## Запуск
Для локального запуска:
```
python3 manage.py runserver
```
Вам потребуются данные для отображения на карте, для этого зайдите в админку `localhost:port/admin` (по умолчанию: `127.0.0.1:8000/admin`) и создайте места. Фотографии можете загрузить во время создания локации или отдельно. Упорядочить фотографии можно также создавая или редактируя локацию.

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

