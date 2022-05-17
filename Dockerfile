FROM tensorflow/tensorflow:2.7.2
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["waitress-serve", "app:app" ]