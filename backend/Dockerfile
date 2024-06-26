# pull official base image
FROM python:3.12.4-slim-bullseye

# Define build arguments
ARG USER_ID
ARG GROUP_ID

# Define environment variables
ENV USER_ID=$USER_ID
ENV GROUP_ID=$GROUP_ID
ENV USER_ID=${USER_ID:-1001}
ENV GROUP_ID=${GROUP_ID:-1001}

# Add group and user based on build arguments
RUN addgroup --gid ${GROUP_ID} devt
RUN adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} devt
# set working directory
WORKDIR /usr/src/app
RUN chown -R devt:devt .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# # add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# # run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]