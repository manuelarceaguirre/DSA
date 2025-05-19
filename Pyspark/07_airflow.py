"""
Runs every day at 6am.

Has two tasks:

Task 1: Runs a Databricks job (simulate with a Python function called run_databricks_job that just prints “Databricks job started!”)

Task 2: Sends a notification (simulate with a Python function send_notification that prints “Notification sent!”)
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Step functions
def run_databricks_job():
    print("Databricks job started!")

def send_notification():
    print("Notification sent!")

# Default DAG arguments
default_args = {
    "owner": "your_name",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id="my_first_dag",
    default_args=default_args,
    description="A basic example DAG",
    schedule_interval="0 6 * * *",  # runs daily at 6AM
    start_date=datetime(2025, 5, 1),
    catchup=False,
    tags=["example"],
) as dag:

    run_task1 = PythonOperator(
        task_id="run_task1",
        python_callable=task1,
    )

    run_task2 = PythonOperator(
        task_id="run_task2",
        python_callable=task2,
    )

    # Set task order
    run_task1 >> run_task2


