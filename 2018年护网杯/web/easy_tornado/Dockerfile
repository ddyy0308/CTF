FROM python:2.7-alpine

LABEL Author="Virink <virink@outlook.com>"
LABEL Blog="https://www.virzz.com"

ADD ssti_tornado.py /app/app.py

RUN pip install \
	-i http://mirrors.aliyun.com/pypi/simple/ \
	--trusted-host mirrors.aliyun.com \
	-U tornado && \
	touch /app/error.html && \
	chmod 777 /app/error.html

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python","/app/app.py"]