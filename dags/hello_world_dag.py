from airflow import DAG
from datetime import datetime
from airflow.operators import python_operator
def print_hello():
    return'hello world'
with DAG("hello_world",
            start_date = datetime(2022 , 7 , 29),
             schedule_interval = '@daily' ,
             catchup = False) as dag:
    hello_operator = python_operator.PythonOperator(task_id='hello_task' , python_callable= print_hello , dag=dag )

hello_operator