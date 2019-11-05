FROM ubuntu:14.04

MAINTAINER deepak

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && apt-get install -y \
	git \
	python \
	python-dev \
	python-setuptools \
	nginx \
	supervisor \
	libmysqlclient-dev \
  && rm -rf /var/lib/apt/lists/*

RUN easy_install pip

# Install uwsgi now because it takes a little while
RUN pip install uwsgi

# Setup all the config files
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of our code, this will cause Docker's caching mechanism
# to prevent re-installinig (all our) dependencies when we made a change in a line or two in our app.

COPY requirements.txt /home/coosta/
RUN pip install -r /home/coosta/requirements.txt

ARG build_environment=PROD

ENV COOSTA_ENVIRON=$build_environment

# Add (the rest of) our code
COPY . /home/coosta/

VOLUME /var/log/supervisor/

EXPOSE 80
CMD ["supervisord", "-n"]