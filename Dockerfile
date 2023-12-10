FROM python
WORKDIR /jarvis
WORKDIR /jarvis
COPY . /jarvis
CMD [ "python3","./jarvis.py" ]