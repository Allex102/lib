Инструкция к активации

У вас должен быть установлен сервер postgres с данными указанными в файле settings.py в разделе DATABASES

Команды manage.py делать в терминале в той же папке где находится файл manage.py
1. python manage.py migrate
2. Если будете создавать свои данные для базы ничего делать не нужно, если нужны готовые данные импортируйте в бд dump.sql 
3. python manage.py runserver