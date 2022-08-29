from airflow.operators import bash
from airflow import DAG
from datetime import datetime
with DAG("bq_dataset",
            start_date = datetime(2022 , 7 , 29),
             schedule_interval = '@daily' ,
             catchup = False) as dag:

    make_bq_dataset = bash.BashOperator(
        task_id="make_bq_dataset",

        bash_command=f"bq ls {deepu_table} || bq mk {deepu_table}",
    )