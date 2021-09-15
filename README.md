# Фотоальбом
Задача проекта - создание API фотоальбома на Django и DRF

## С помощью API, можно получить доступ к следующим ресурсам:

### Album
* Посмотреть все папки пользователя;
* Создать новую папку;
* Изменить имя папки по id;
* Удалить папку по id;
* Вывод json- автор папки, сколько фото в папке, дата создания.

### AlbumImage
* Посмотреть все фотографии и их уменьшиные копии;
* Добавить новую фотографию в альбом, размером не более 5 мб;
* Удалить фотографию;
* Вывод json- id, оригинал фото, уменьшенная копия, тэг, дата создания и редактирования. 

### AUTH
* аутентификация (Получение JWT-токена)

### USERS
* Получить список всех пользователей;
* Создать учетную запись пользователя;
* Изменить пользовательские данные по id;
* Удалить пользователя.

## Стек
 
Python 3, Django 3.2.6, Django REST Framework, SQLite3, GIT


## Установка 
Клонируем репозиторий на локальную машину:

```$ git clone https://github.com/Basil2587/api_foto.git```

В директории проекта создайте файл .env: 
  - SECRET_KEY=можно сгенерировать [по адресу](https://djecrety.ir)

Создаем виртуальное окружение:  ```python3 -m venv venv```

Активировать виртуальное окружение (для Linux): ```source venv/bin/activate```

Устанавливаем зависимости: ```pip install -r requirements.txt```

Создание и применение миграций: ```python manage.py makemigrations``` и ``` python manage.py migrate```

Создадим суперпользователя: ```python manage.py createsuperuser```

Запускаем django сервер: ```python manage.py runserver```

Адрес API: http://localhost:8000/api/v1/

## Подробная документация методов API c примерами команд:

http://localhost:8000/swagger/

Примеры работа с аккаунтами пользователя с помощью запросов: 
 
  GET  http://localhost:8000/api/v1/users/        #Посмотреть всех пользователей 
   
  GET  http://localhost:8000/api/v1/users/{id}/   #Получить конкретного пользователя по id 
        
  POST  http://localhost:8000/api/v1/users/       #Создание пользователя
   
  PUT   http://localhost:8000/api/v1/users/{id}/  #Обновить данные о пользователе по id 
   
  PATCH http://localhost:8000/api/v1/users/{id}/  #Частично обновить данные о пользователе по id 
   
  DELETE http://localhost:8000/api/v1/users/{id}/ #Удалить пользователя по id 
  

   JWT-токен: 
    
   http://localhost:8000/api/v1/token/           #Получить JWT-токен 
    
   http://localhost:8000/api/v1/token/refresh/   #Обновить JWT-токен 

