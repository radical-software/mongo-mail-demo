FROM ubuntu:trusty

MAINTAINER <stephane.rault@radicalspam.org>

ENV MMS_SERVER mongo-quarantine
ENV MMS_REAL_RCPT 0
ENV MMS_HOST 127.0.0.1
ENV MMS_PORT 14001
ENV MMS_TIMEOUT 600
ENV MMS_DATA_SIZE_LIMIT 0
ENV MMS_MONGODB_URI mongodb://localhost/message
ENV MMS_MONGODB_DATABASE message
ENV MMS_MONGODB_COLLECTION message
#ENV MMS_DEBUG 1

ENV MMW_SETTINGS mongo_mail_web_demo.settings.Demo
ENV MMW_MODE 1
ENV MMW_MONGODB_URI mongodb://localhost/message
ENV MMW_SUPERADMIN_EMAIL admin@example.net
ENV MMW_SUPERADMIN_PASSWORD password

ENV MMW_DEMO_MMS_HOST 127.0.0.1
ENV MMW_DEMO_MMS_PORT 14001

RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \
  echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" > /etc/apt/sources.list.d/nginx-stable-trusty.list && \
  apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  build-essential \
  ca-certificates \
  git \
  curl \
  language-pack-en \
  iptables \
  python-dev \
  cython \
  python-gevent \
  fail2ban \
  nginx \
  mongodb-org
  
ENV PATH /usr/local/bin:${PATH}
ENV LANG en_US.UTF-8

RUN curl -k -O https://bootstrap.pypa.io/ez_setup.py && python ez_setup.py --insecure && rm -f ez_setup.py setuptools*zip

RUN curl -k -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm -f get-pip.py

#RUN pip install https://github.com/srault95/mongo-mail-tools/tarball/master
#RUN pip install --process-dependency-links https://github.com/srault95/mongo-mail-web/tarball/master

RUN pip install 'pymongo<3.0,>=2.8' \
   https://github.com/MongoEngine/flask-mongoengine/tarball/master \
   https://github.com/srault95/flanker/tarball/light_deps \
   https://github.com/srault95/geoip-data/tarball/master

ADD . /code/
WORKDIR /code/
RUN pip install --process-dependency-links .

RUN mkdir -p /data/db

RUN mkdir -p /var/run/fail2ban
ADD fail2ban.conf /etc/fail2ban/filter.d/mmw.conf
ADD jail-mmw.conf /etc/fail2ban/jail.d/mmw.conf

RUN mkdir -p /etc/supervisor/conf.d /var/log/supervisor
ADD supervisord.conf /etc/supervisor/
RUN echo "alias ctl='/usr/local/bin/supervisorctl -c /etc/supervisor/supervisord.conf'" >> /root/.bashrc

RUN rm -f /etc/nginx/sites-enabled/* /etc/nginx/sites-available/*
RUN mkdir -vp /var/log/nginx && chown www-data /var/log/nginx
ADD nginx.conf /etc/nginx/

ADD start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh

WORKDIR /var/log

EXPOSE 80

CMD ["/usr/local/bin/start.sh"]
