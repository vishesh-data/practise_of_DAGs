from airflow import DAG
from datetime import datetime
from airflow.operators import python_operator
from airflow.operators import bash_operator
def print_hello():
    return'hello world'
with DAG("hello_world",
            start_date = datetime(2022 , 7 , 29),
             schedule_interval = '@daily' ,
             catchup = False) as dag:
    hello_python = python_operator.PythonOperatory(
        task_id='hello_task' ,
        python_callable= print_hello
    )
    good_bye = bash_operator.BashOperator(
        task_id='good_bye_task',
        python_callable='echo goodbye'
    )

hello_python >> good_bye