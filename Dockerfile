FROM ubuntu
MAINTAINER Shravan <shsh9888@colorado.edu>
RUN mkdir -p /srv
WORKDIR /srv
RUN apt-get update && apt-get install -y python3 python3-pip  && pip3 install cassandra-driver && pip3 install jsonpickle && pip3 install flask

COPY entrypoint.sh /srv
COPY rest-server.py /srv

RUN chmod 777 /srv/rest-server.py
RUN chmod 777 /srv/entrypoint.sh
ENTRYPOINT ["/srv/entrypoint.sh"]
