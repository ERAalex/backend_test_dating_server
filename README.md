
#### Django API.
# Project - Dating Web Server 

<img src="https://img.freepik.com/premium-vector/couple-situations-young-people-woman-and-man-in-love-kiss-walk-quarrel-and-couch-sofa_81894-3579.jpg?w=500">

<br><a href="mailto:erapyth@gmail.com"><img src="https://img.shields.io/badge/-Gmail%20contact%20me-red"></a>
<br><a href="https://t.me/espinosa_python"><img src="https://img.shields.io/badge/-Telegram-blue"></a>

## About the project.

  <a href="#" target="_blank" rel="noreferrer nofollow">
    <img src="https://github.com/ERAalex/new_test/blob/main/website_icons.jpg" >
  </a>

Данный проект в дальнейшем можно оптимизировать.
Сайт направлен на подготовку API для онлайн-платформы встреч.<br>
Для работы и проверки сервера на части API использовался Postman.
###### Стек технологий: Django REST Framework, PostgreSQL, Celery, Redis.<br>


### Выполненные моменты.
<a href="#" target="_blank" rel="noreferrer nofollow">
      <img src="https://github.com/ERAalex/PREVIEW_project_site_buisness_card_Maria-/blob/main/website_icons.jpg" >
</a>

1. Подготовлена модель пользователя с необходимыми полями: имя, фамилия, пол,
аватар, почта и поля с местоположением пользователя (долгота и широта). <br>
Подготовлена дополнительная модель для объединения понравившихся друг другу пользователей
2. API /api/clients/create для регистрации пользователя.<br>
Но для удобства подключен и настроен Djoser для дальнейшей инеграции проекта с фронтендом 
и подтверждением дейтсвий через JWT токены.
3. При регистрации пользователя аватарка обрабатывается:
- изменяются размеры под требования
- создается папка пользователя с уникальным именем куда грузится картинка для дальнейшей удобной
эксплуатации бекенда.
- при сохранении добавляется водяной знак через библиотеку PILLOW.
4. API /api/clients/{id}/match  добавление пользователей в понравившиеся. Продумана логика, что
если Вы уже находитесь в понравившихся пользователя, то у Вас образуется взаимосвязь (поле в БД) и отправляется 
письмо клиенту с фразой «Вы понравились <клиент>! Почта участника: <почта>.
- Настроен CELERY для отправки письма.
5. API /api/list отображение пользователей с возможностью фильтрации (по имени, полу, фамилии)
через библиотеку django-filters.
6. Реализована идея поиска ближайших от клиента пользователей через специальный кастомный фильтр.
Реализована сложная функция по расчету дальности клиентов в км. Great Circle Distance.
<br> <br>

Дополнитьная работа по серверу:<br>
1. Хранение всей чувствительной информации в .env, настройка .gitignore
2. Настройка и подключение Swagger для удобства просмотра документации проекта.
3. Настройка и подключение Debud Toolbar
4. Подключение celery
5. Создание Dockerfile и docker-compose.yml для запуска проекта.<br>
- PrintScreen результата: 

<a href="#" target="_blank" rel="noreferrer nofollow">
      <img src="https://github.com/ERAalex/ERA_Fast_API_course_money/blob/main/docker_img.png" width="450" height="250">
</a>


<br>


## 1. Подготовка к запуску проекта <a id="preparation"></a>

- Скачайте репозиторий.
```shell
git clone https://github.com/ERAalex/backend_test_dating_server -b main
```

- Установите зависимости.
```shell
pip install -r requirements.txt
```


- Настройка переменных окружения. Перед запуском проекта необходимо создать файл
```.env``` в директории `core`.
> **внимание**: вы можете развернуть postgresql в контейнере, если Вам так удобно.

```shell
[settings]

SECRET_KEY =
DEBUG_STATUS =

[database]

DB_ENGINE =
DB_NAME =
DB_PASS =
DB_USER =
DB_HOST =
DB_PORT =

[email_host]

EMAIL_HOST =
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD =
EMAIL_PORT =
EMAIL_USE_TLS =
```

- Проведите первые миграции и запустите проект

```shell
python manage.py migrate
```


### 2. Запуск через docker-compose
Ваши шаги до запуска docker-compose:
- до запуска docker-compose измените в settings параметры в коде, они подписаны. 
Например:
```shell
"HOST": "db"
CELERY_BROKER_URL = 'redis://redis:...'
```

- создайте файл .env для переменных окружения рядом с docker-compose.yml, запишите необходимые данные.
- проект готов к контейниризации. Наберите комманду:
```shell
docker-compose up -d
```
Ваши шаги после запуска docker-compose:
- проверьте и настройте БД (например удобно через контейнер PgAdmin http://localhost:5050/).
- зайдите через в контейнер с проектом и создайте superuser для удобства работы и контроля админ панели.
<br><br>


> **** Это начальная версия проекта, поэтмоу я буду рад Вашим комментариям и рекомендациям по улучшению.
- мой телеграм ---> <a href="https://t.me/espinosa_python"><img src="https://img.shields.io/badge/-Telegram-blue"></a>

<br>
<br>
