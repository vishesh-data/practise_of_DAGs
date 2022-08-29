from airflow.providers.google.cloud.operators import bigquery
from airflow import DAG
from datetime import datetime
with DAG("bq_dataset",
            start_date = datetime(2022 , 7 , 29),
             schedule_interval = '@daily' ,
             catchup = False) as dag:


    bq_recent_questions_query = bigquery.BigQueryInsertJobOperator(
        task_id="bq_recent_questions_query",
        configuration={
            "query": {
                "query":deepu123_query,

                "destinationTable": {
                    "projectId": bq_deepu123,
                    "datasetId":deepu123,
                    "tableId": marks345,
                },
            }
        },
        location=location,
    )