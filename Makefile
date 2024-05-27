export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up-d test

build:
	docker-compose build

up:
	docker-compose up

up-d:
	docker-compose up -d

up-build:
	docker-compose up --build

down:
	docker-compose down

test:
	docker-compose exec api python -m pytest "src/tests"
