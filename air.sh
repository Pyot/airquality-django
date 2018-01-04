#!/bin/sh

# Define your function here
celerybeatlog () {
watch -n 1 tail -n 45 /var/www/venv/src/logs/celery-beat.log 
}

celeryworkerlog () {
watch -n 1 tail -n 45 /var/www/venv/src/logs/celery-worker.log 
}

