from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# com o uso do with, não é necessário definir dag=dag na task
with DAG('dag_complex', description="Task simples com with",
        schedule_interval=None, start_date=datetime(2024,6,25),
        catchup=False) as dag:
# se colocar uma data muito passada o schedule vai executar todos intervalos passados, portanto o catchup=False faz com que isso não aconteça

    task1 = BashOperator(task_id='tsk1', bash_command="sleep 2")
    task2 = BashOperator(task_id='tsk2', bash_command="sleep 2")
    task3 = BashOperator(task_id='tsk3', bash_command="sleep 2")
    task4 = BashOperator(task_id='tsk4', bash_command="sleep 2")
    task5 = BashOperator(task_id='tsk5', bash_command="sleep 2")
    task6 = BashOperator(task_id='tsk6', bash_command="sleep 2")
    task7 = BashOperator(task_id='tsk7', bash_command="sleep 2")
    task8 = BashOperator(task_id='tsk8', bash_command="sleep 2")   
    task9 = BashOperator(task_id='tsk9', bash_command="sleep 2", trigger_rule='one_failed')
    
task1 >> task2
task3 >> task4
[task2,task4] >> task5 >> task6
task6 >> [task7, task8, task9]
    
