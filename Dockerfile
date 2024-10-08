FROM python:3.11
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r /requirements.txt

ENV PYTHONPATH=/app


WORKDIR /app

COPY . .
COPY docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x ./docker-entrypoint.sh && \
	ln -s ./docker-entrypoint.sh /

# RUN alembic -n postgres upgrade head
# RUN alembic -n postgres revision --autogenerate -m "init" && alembic -n postgres upgrade head

# ENTRYPOINT ["sh", "./docker-entrypoint.sh" ]