# Databricks VSCode Tutorial

## Requirements

- [uv package manager](https://docs.astral.sh/uv/)
- [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/)
- [VS Code databricks Extension](https://docs.databricks.com/aws/en/dev-tools/vscode-ext/)

## Configure OAuth

```shell
# show login options
databricks auth login --help

# login to dev using serverless cluster
databricks auth login --host https://xxxxx.x.azuredatabricks.net --profile dev

# login to prod using configured cluster
databricks auth login --configure-cluster --host https://xxxxx.x.azuredatabricks.net --profile prod
```

This opens a browser window where you can connect using Entra ID and  creates the file `.databrickscfg`on your user:

```shell
; The profile defined in the DEFAULT section is to be used as a fallback when no profile is explicitly specified.
[DEFAULT]

[dev]
host      = https://xxxxxxxxx.x.azuredatabricks.net/
auth_type = databricks-cli

[prod]
host      = https://xxxxxxxxxxx.x.azuredatabricks.net/
cluster_id = xxxxxxx
auth_type = databricks-cli
```

## VS Code Setup

Based on the docs from [Databricks](https://docs.databricks.com/aws/en/dev-tools/vscode-ext/). 

Usefull tips:
- ensure databricks-connect is same version as your Cluster
- remember to run spark sessions remotely on Databricks using DatabricksSession instead of using SparkSession