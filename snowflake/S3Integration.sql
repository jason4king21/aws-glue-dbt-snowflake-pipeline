-- AWS S3-Snowflake Integration

USE ROLE ACCOUNTADMIN;
USE WAREHOUSE COMPUTE_WH;

CREATE OR REPLACE DATABASE GLUEDB;

CREATE OR REPLACE STORAGE INTEGRATION GLUE_S3_INT
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'Your_snowflake_role_arn_from_aws'
  STORAGE_ALLOWED_LOCATIONS = ('Your_GLUE_S3_URI_of_bucket_with_folder');
 

DESC INTEGRATION GLUE_S3_INT;

-- Open your AWS Management Console and navigate to AWS IAM (you can search for "IAM" in the search bar).

-- Replace Existing AWS value with STORAGE_AWS_IAM_USER_ARN  and ExternalId with STORAGE_AWS_EXTERNAL_ID values fetched from snowflake in previous step in the Trusted entities

CREATE OR REPLACE STAGE GLUEDB.PUBLIC.GLUE_S3_STAGE
STORAGE_INTEGRATION = GLUE_S3_INT
URL= 'Your_GLUE_S3_URI_of_bucket_with_folder';

ls @GLUEDB.PUBLIC.GLUE_S3_STAGE;

CREATE OR REPLACE TABLE GLUEDB.PUBLIC.COUNTRY_DETAILS_CP
(
DATA VARIANT
);
