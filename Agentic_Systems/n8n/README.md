Local **N8N**

To use **n8n** on you must:
 1. Install docker and docker compose(optional) on your local device.
 2. You can create a docker_compose.yml file to config your custom setup.
 3. Run **n8n** image on your local host by ```docker compose up -d```.(It will try to pull images the first time you use it)

You can use [docker-compose.yml](./docker-compose.yml) as your config file which will create a **postgres** and **n8n** container and connect them using network.
