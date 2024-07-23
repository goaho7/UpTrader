### Запуск проекта локально:

Склонируйте проект и перейдите в директорию UpTrader
``` 
git clone git@github.com:goaho7/UpTrader.git 
``` 
``` 
cd UpTrader 
```


Выполните команды
``` 
poetry install 
``` 
``` 
poetry shell 
``` 

перейдите в каталог с файлом manage.py
``` 
cd src 
``` 

Запустите миграции
``` 
python manage.py migrate 
``` 

Создайте суперюзера
``` 
python manage.py createsuperuser 
```

Запустите проект
``` 
python manage.py runserver 
``` 
