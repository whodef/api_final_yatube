# API для Yatube

## Описание
API (основанный на DRF) для социальной сети YaTube.

Реализация:

- Авторизация по JWT (JSON Web Token)
- Сериализация данных для всех моделей проекта (Group, Follow, Post, Comment)
- Обработка GET, POST, PATCH, PUT и DELETE запросов к БД YaTube

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/whodef/api_final_yatube.git
```

```
cd api_yatube
```

Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Эндпоинты проекта


- `api/v1/api-token-auth/` (POST): передать логин и пароль, получить токен.

- `api/v1/posts/` (GET, POST): получить список всех постов или создать новый пост.

- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получить, редактировать или удалить пост по id.

- `api/v1/posts/{post_id}/comments/` (GET, POST): получить список всех комментариев поста с id=post_id или создать новый, указав id поста, который нужно прокомментировать.

- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получить, редактировать или удалить комментарий по id у поста с id=post_id.

- `api/v1/groups/` (GET): получить список всех групп.

- `api/v1/groups/{group_id}/` (GET): получить информацию о группе по id.

- `api/v1/follow/` (GET, POST): Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.

- `api/v1/jwt/create/` (POST): Получение JWT-токена.

- `api/v1/jwt/refresh/` (POST): Обновление JWT-токена.

- `api/v1/jwt/verify/` (POST): Проверка JWT-токена.
