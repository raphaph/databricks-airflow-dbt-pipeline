from airflow.decorators import task_group
from airflow.operators.empty import EmptyOperator
from airflow import DAG
import datetime as dt

dag = DAG(
    'dag_agrupada',
    start_date=dt.datetime(2024, 6, 25),
    catchup=False,
    schedule_interval="@daily",
    default_args={"retries": 3},
)

@task_group(dag=dag)
def group1():
    task1 = EmptyOperator(task_id="task1", dag=dag)
    task2 = EmptyOperator(task_id="task2", dag=dag)

task3 = EmptyOperator(task_id="task3", dag=dag)

group1() >> task3