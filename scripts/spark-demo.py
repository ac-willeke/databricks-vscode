# source: https://docs.databricks.com/aws/en/dev-tools/vscode-ext/tutorial

from databricks.connect import DatabricksSession
from pyspark.sql.types import *

# Create a remote Databricks session
spark = DatabricksSession.builder.getOrCreate()

schema = StructType(
    [
        StructField("CustomerID", IntegerType(), False),
        StructField("FirstName", StringType(), False),
        StructField("LastName", StringType(), False),
    ]
)

data = [
    [1000, "Mathijs", "Oosterhout-Rijntjes"],
    [1001, "Joost", "van Brunswijk"],
    [1002, "Stan", "Bokenkamp"],
]

customers = spark.createDataFrame(data, schema)
customers.show()
