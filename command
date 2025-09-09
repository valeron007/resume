python -m venv venv

docker ps

docker compose up
docker compose down
docker-compose ps

docker exec -it postgres sh

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres

docker network create --gateway 172.19.1.1 --subnet 172.19.1.0/24 fstapi_static-network

docker network ls

docker network rm fstapi_static-network

docker network create --gateway 172.16.1.1 --subnet 172.16.1.0/24 --scope swarm app_subnet


pip install pip-tools

pip-compile
pip-sync

alembic init alembic

alembic revision --autogenerate -m 'initial'

alembic upgrade 143a57a7c33f

uvicorn main:app

# front

 npm start
    Starts the development server.

  npm run build
    Bundles the app into static files for production.

  npm test
    Starts the test runner.

  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd frontend
  npm start


