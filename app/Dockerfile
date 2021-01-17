FROM python:3.9-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 4000
ENV PYTHONUNBUFFERED 0
CMD ["python", "-u", "app.py"]