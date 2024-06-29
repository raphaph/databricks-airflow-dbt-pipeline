#!/bin/bash
# permissão de execução ~$ chmod +x ./start_airflow.sh

airflow webserver &
sleep 5
airflow scheduler &
airflow flower &
airflow celery worker