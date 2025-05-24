# AWS Glue + DBT + Snowflake ELT Pipeline

This project demonstrates a scalable data pipeline using AWS Glue, S3, dbt, and Snowflake. It showcases data extraction from an external API, storage in S3, and transformation and modeling in Snowflake using dbt.

## 🚀 Overview

- **Ingestion**: AWS Glue extracts data from an external API
- **Storage**: JSON data stored in an S3 bucket
- **Modeling & Transformation**: dbt loads and models data into Snowflake

## Architecture
![Architecture Diagram](diagrams/architecture.png)

## DBT Lineage
![Linage Diagram](diagrams/DBTLineage.png)


## 📌 Project Steps

### 1. Create AWS IAM Role for Glue Job
- Permissions to read from and write to S3

### 2. Set Up S3 Bucket
- Used to store extracted JSON data

### 3. Create AWS Glue Job
- Python script to extract data from API
- Writes JSON files to S3 bucket

### 4. Set Up IAM Role and Storage Integration in Snowflake
- Allows Snowflake to read from S3
- Configure `STORAGE INTEGRATION` in Snowflake

### 5. Create DBT Cloud Account via Snowflake Partner Connect
- Enables integrated data modeling and transformation

### 6. Set Up DBT Models
- `raw/`: landing zone for S3-ingested data
- `transform/`: cleaned and enriched tables
- `mart/`: business-ready reporting layers

### 7. Set Up Deployment Environment in dbt
- Configure production jobs and environments
- Automate model runs and materializations

---

## 🛠 Tools & Tech
- **AWS Glue**: serverless ETL engine
- **AWS S3**: cloud object storage
- **Snowflake**: cloud data warehouse
- **dbt Cloud**: analytics engineering platform

---

## 📂 Repository Structure
```
aws-glue-dbt-snowflake-pipeline/
│
├── README.md                  → Project overview and architecture details
├── .gitignore                 → Specifies intentionally untracked files to ignore
├── dbt_project.yml            → Configuration file for the dbt project
├── diagrams/
│   └── architecture.png       → Visual diagram of the AWS Glue + dbt + Snowflake pipeline
├── glue/
│   └── extract_api.py         → AWS Glue job script for extracting data from an external API
├── macros/
│   └── [macro_files].sql      → Custom dbt macros for reusable SQL snippets
├── models/
│   ├── raw/                   → dbt models for raw data staging
│   ├── transform/             → dbt models for data transformation
│   └── mart/                  → dbt models for data marts
├── seeds/
│   └── [seed_files].csv       → Seed data files for dbt
├── snapshots/
│   └── [snapshot_files].sql   → dbt snapshots for capturing slowly changing dimensions
├── snowflake/
│   └── snowpipe_trigger.sql   → SQL script to configure Snowpipe for auto-ingestion
├── src/
│   └── DiagramGenerator/
│       └── architecture.py    → Python script to generate architecture diagrams
└── tests/
    └── sample.json            → Sample JSON file used to test the API and Lambda function

```

---


## 📥 Requirements
```
boto3
snowflake-connector-python
dbt-core
dbt-snowflake
```

---

