# Step 1: Import the Os
FROM python:3

RUN pip install --upgrade pip

# Step 3: Create a Work Directory
WORKDIR /app

# Step 4: copy all Project Files
COPY . /app

RUN pip install -r requirements.txt

# Step 6:  run the command to start uWSGI
CMD ["uwsgi", "app.ini"]