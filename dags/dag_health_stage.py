from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dbt_path = "cd /home/mantis/airflow-dbt/databricks-dbt-etl/"

with DAG('dag_health_stage', 
         description="health_stage",
         schedule_interval="@daily",
         start_date=datetime(2024,6,25),
         catchup=False,
         tags=["stage","health"]) as dag:
    

    task2 = BashOperator(task_id="health_stage", bash_command=f"{dbt_path} && dbt run -s stg_health")
    
    task2