#Вазно соблюдать порядок
#FROM(в каком образе хотим все хапустить)
FROM python:3.8
#ENV система буфирезации что бы нормально выводить логи
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#Отдельно выставели DEBUG
ENV DEBUG=1
#COPY поместить проет в образ .(из папке в которой нахожусь) .(в папку в нутри контейнера)
#WORKDIR /src создаем папку в образе где будут лезать наши фаилы
WORKDIR /usr/src/
#COPY поместить проет в образ .(из папке в которой нахожусь) .(в папку в нутри контейнера)
COPY requirements.txt requirements.txt
#RUN команда запуска (можно запускать к примеру pip)
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/
#Сигнал что процесс на порту 8000(для общения контейнеров достаточно его указать без проброски портов из вне)
EXPOSE 8000
#CMD команда при запуске контейнера (docker run -it test_docker)
# docker run -it -p 8000:8000 test_docker (в командной строке запуска docker с указание портов)
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]


#Способ проверки правильности докер фаила через командную строку (docker run -i hadolint/hadolint < Dockerfile)
#.dockerignor фал данные которого не попадают в docker contener(стандарный набор данных +что то свое)