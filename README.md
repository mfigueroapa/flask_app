# Dockerized Flask App with Postgress, Gunicorn and Nginex

## Requirements

1. Docker version 20.10.8 or greater.
2. Python 3.

## Local Development

2. Build development container:

    ```
       $ docker-compose build
    ```

3. Run container
   <!-- 
   -d - run the container in detached mode (in the background) 
   -p 80:80 - map port 80 of the host to port 80 in the container
   docker run -dp 80:80 docker/getting-started
   -t flag tags our image. Think of this simply as a human-readable name for the final image. Since we named the image getting-started, we can refer to that image when we run a container.


   -->

    ```
       $ docker-compose up -d
    ```
   

4. Run container 
    ```
       $ docker-compose up -d --build
    ```


5. Run container Create the table:
```
       $ docker-compose exec web python manage.py create_db
    ```

6. Access db

      ```
         docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev
         \c hello_flask_dev
         \dt
      ```

