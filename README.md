This is a basic python flask application with Redis and and Nginx load balancer. In order to run this application locally, run the following commands to build the flask and nginx images.
~~~~ docker build -f Dockerfile.node -t finney/counter . ~~~~
~~~~ docker build -f Dockerfile.nginx -t finney/nginx . ~~~
Then the docker conatiners can be built by running
~~~~ docker-compose up ~~~~
