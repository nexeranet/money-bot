FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive
ENV APP /app

RUN mkdir $APP

WORKDIR $APP

ADD . $APP

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000

# define the default command to run when starting the container
ENTRYPOINT ["sh", "./setup.sh"]
