from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG('dag_simples', description="dag simples",
          schedule_interval=None, start_date=datetime(2024,6,25),
          catchup=False) 
# se colocar uma data muito passada o schedule vai executar todos intervalos passados, portanto o catchup=False faz com que isso não aconteça

task1 = BashOperator(task_id='tsk1', bash_command="ls", dag=dag)
task2 = BashOperator(task_id='tsk2', bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command="sleep 5", dag=dag)

task1 >> task2 >> task3