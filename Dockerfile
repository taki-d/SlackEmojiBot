FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config/
RUN pip install -r /config/requirements.pip
RUN mkdir /SlackEmojiBot
ADD . /SlackEmojiBot
WORKDIR /SlackEmojiBot
ENTRYPOINT ["python", "run.py"]
