from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('trigger_dag_all_failed', description="executará a task3 somente se houver uma falha",
          schedule_interval=None, start_date=datetime(2024,6,25),
          catchup=False) as dag: 

    task1 = BashOperator(task_id='tsk1', bash_command="exit 1") # simula falha para a task3 executar
    task2 = BashOperator(task_id='tsk2', bash_command="exit 1")
    task3 = BashOperator(task_id='tsk3', bash_command="sleep 5", trigger_rule='one_failed')
    

    [task1, task2] >> task3