"""
Runs every day at 6am.

Has two tasks:

Task 1: Runs a Databricks job (simulate with a Python function called run_databricks_job that just prints “Databricks job started!”)

Task 2: Sends a notification (simulate with a Python function send_notification that prints “Notification sent!”)
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# step functions

def start_pipeline():
    print("Start pipeline")

def transform_data():
    print("Transform data")


# Default DAG arguments

default_args = {
        "owner": "manuel",
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes =5),
        }

with DAG(
        dag_id="data_pipeline_simulation",
        default_args=default_args,
        description="A simple airflow DAG for pipelines",
        schedule_interval = "0 6 * * *",
        start_date=datetime(2025, 5, 14),
        catchup = False,
        tags = ["example"]
) as dag:

    step1 = PythonOperator(
            task_id = "start_pipeline",
            python_callable=start_pipeline

            )


    step2 = PythonOperator(
            task_id = "transform_data",
            python_callable=transform_data
            )

    step1 >> step2
