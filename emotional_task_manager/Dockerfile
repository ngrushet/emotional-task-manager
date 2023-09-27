# Используйте базовый образ Python
FROM python:3.9

# Установите переменную окружения PYTHONUNBUFFERED в значение 1
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файлы requirements.txt в контейнер
COPY requirements.txt /app/

# Установите зависимости проекта
RUN pip install -r requirements.txt

# Скопируйте все файлы проекта в контейнер
COPY . /app/

# Запустите команду для запуска сервера Django
CMD python ./emotional_task_manager/manage.py runserver 0.0.0.0:8000
# CMD ls -a emotional_task_manager