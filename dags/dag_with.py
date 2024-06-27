from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# com o uso do with, não é necessário definir dag=dag na task
with DAG('dag_with', description="Task simples com with",
        schedule_interval=None, start_date=datetime(2024,6,25),
        catchup=False) as dag:
# se colocar uma data muito passada o schedule vai executar todos intervalos passados, portanto o catchup=False faz com que isso não aconteça

    task1 = BashOperator(task_id='tsk1', bash_command="sleep 5")
    task2 = BashOperator(task_id='tsk2', bash_command="sleep 5")
    task3 = BashOperator(task_id='tsk3', bash_command="sleep 5")

    # equivalente ao task1 >> task2...
    task1.set_downstream(task2)
    task2.set_downstream(task3)
    
    # set_upstream faz o contrário, de baixo pra cima