FROM python:3.7-alpine
copy . /opt/myapp/
WORKDIR /opt/myapp/
ENTRYPOINT ["python3"]
CMD ["1hashmap.py L2.txt L3.txt"]+
