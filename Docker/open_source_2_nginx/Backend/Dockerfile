FROM python:3.10
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app 
WORKDIR /app 

COPY ./entrypoint.sh .
ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]





# =============================== GUNICORN ========================
# Dockerfile for Django Backend

# # Use the official Python image from the Docker Hub
# FROM python:3.10

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set the working directory in the container
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the project files into the container
# COPY . /app/

# # Expose the port that the app runs on
# EXPOSE 8000

# # Command to run the application
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "reg_blog.wsgi:application"]