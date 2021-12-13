# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app


# So, we started with a slim-buster-based Docker image for Python 3.9.5. We then set a working directory along with two environment variables:
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
# -B If given, Python won’t try to write .pyc files on the import of source modules.

ENV PYTHONUNBUFFERED 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
# -u Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.


# install system dependencies
RUN apt-get update && apt-get install -y netcat
# Netcat functions as a back-end tool that allows for port scanning and port listening.
# In addition, you can actually transfer files directly through Netcat or use it 
# as a backdoor into other networked systems

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]