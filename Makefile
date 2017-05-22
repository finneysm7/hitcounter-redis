
app-build:
	docker build -f Dockerfile.node -t finney/counter .

redis-build:
	docker build -f Dockerfile.redis -t finney/redis .

nginx-build:
	docker build -f Dockerfile.nginx -t finney/nginx .
