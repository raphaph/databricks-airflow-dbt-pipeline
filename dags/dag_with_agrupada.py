from airflow.decorators import task_group
from airflow.operators.empty import EmptyOperator
from airflow import DAG
import datetime as dt

with DAG('dag_with_agrupada', description="Agrupa 2 tasks e executa o grupo antes da 3ª task",
    start_date=dt.datetime(2024, 6, 25),
    catchup=False,
    schedule_interval="@daily",
    default_args={"retries": 3},
) as dag:

    @task_group()
    def group1():
        task1 = EmptyOperator(task_id="task1")
        task2 = EmptyOperator(task_id="task2")

    task3 = EmptyOperator(task_id="task3")

    group1().set_downstream(task3) # executa group1 em seguida task3
   # set_upstream faz o contrário, de baixo pra cima