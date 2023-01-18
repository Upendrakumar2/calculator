import mlflow

import calculator.logic
import calculator.logger


data_path="datasets"

with mlflow.start_run(run_name="calculator",) as run:
    num1=int(input("input the number one: "))
    num2=int(input("input the number one: "))
    ans=calculator.logic.add(num1,num2)
    print("add is being done.")
    mlflow.log_param(key="first", value=num1)
    mlflow.log_param(key="second", value=num2)
    mlflow.log_metrics({"sum": ans})
    print("sum of two numbers: ", ans)
    calculator.logger.log_class.add_done()
    mlflow.log_artifact(data_path)
