# Получаем базовый образ
FROM python:3.10

# Уставнавиливаем зависимости
COPY requirements.txt /temp/requirements.txt
# Копирование проекта
COPY . /Currency_converter/

# Уставка рабочий директории
WORKDIR /Currency_converter

RUN pip install -r /temp/requirements.txt
