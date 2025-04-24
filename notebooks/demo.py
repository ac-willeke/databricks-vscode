# COMMAND ----------
# adapated from: https://docs.databricks.com/aws/en/dev-tools/vscode-ext/tutorial
# Define schema and data
import pandas as pd

columns = ["CustomerID", "FirstName", "LastName"]
data = [
    [1000, "Mathijs", "Oosterhout-Rijntjes"],
    [1001, "Joost", "van Brunswijk"],
    [1002, "Stan", "Bokenkamp"],
]

# Create a pandas DataFrame
customers = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(customers)
