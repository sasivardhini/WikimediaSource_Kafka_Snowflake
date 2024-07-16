from snowflake.snowpark.session import Session
connection_parameters = {
  "account": "https://zb66500.ap-southeast-1.snowflakecomputing.com",
  "user": "ACCOUNTADMIN",
  "password": "Sasi@007",
  "role": "API_ROLE",
  "warehouse": "API_WH",
  "database": "TEST_DB",
  "schema": "TEST_SCHEMA"
}

session = Session.builder.configs(connection_parameters).create()

print(session.sql("SELECT CURRENT_TIMESTAMP()").collect())

session.close()