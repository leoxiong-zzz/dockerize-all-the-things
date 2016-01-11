FROM ubuntu:15.10

RUN apt-get install -y --no-install-recommends python3

COPY . /

ENTRYPOINT [ "python3" ]
CMD [ "/irc.py" ]
