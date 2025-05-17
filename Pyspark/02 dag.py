from airflow import DAG
from airflowl.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
        "owner": "manuel.arce",
        "retries": 1,
        "retry_delay":timedelta(minutes=5),
        }

# DAG definition
with DAG(
    dag_id="high_value_orders_daily_dag",
    default_args=default_args,
    description="Daily pipeline to extract high value orders > $500",
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 6 * * *",  # Every day at 6am
    catchup=False,
    tags=["pyspark", "daily", "etl"],
) as dag:

    def run_pyspark_job():
        os.system("path")

    run_spark_task = PythonOperator(
        task_id = "run_high_value_orders",
        python_callable = run_pyspark_job,
    )
