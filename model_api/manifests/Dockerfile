FROM python:3.8-alpine
WORKDIR /model_api
ENV FLASK_APP=flask_app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=/model_api/app.py
EXPOSE 5000
CMD ["flask", "run"]