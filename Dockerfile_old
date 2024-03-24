FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim dos2unix

RUN useradd -rms /bin/bash phonebook && chmod 777 /opt /run

WORKDIR /phonebook

RUN mkdir /phonebook/static && chown -R phonebook:phonebook /phonebook && chmod 755 /phonebook

COPY --chown=phonebook:phonebook . .

RUN pip install -r requirements.txt

USER phonebook

CMD ["gunicorn","-b","0.0.0.0:8001","DjangoPhonebook.wsgi:application"]
