# Text2SQL

This project is LLM-based and it can help users to translate a query specified with human-readable text to Spark SQL statement,
then acquire the answer after Spark's execution.

## Summary of GitHub Repositories

texttosql: https://github.com/oap-project/text2sql-gluten

langchain: https://github.com/PZD-CHINA/langchain.git

pyspark-ai: https://github.com/oap-project/pyspark-ai

## Summary of Model Correctness and Time Performance
| Model                    | Correctness | Task1 Time (s) | Task2 Time (s) | Task3 Time (s) | Task4 Time (s)       |
| ------------------------ | ----------- | -------------- | -------------- | -------------- | -------------------- |
| defog/sqlcoder-70b-alpha | 93.0%       | 98.674         | 140.440        | 45.481         | 223.176              |
| defog/sqlcoder-7b-2      | 90.5%       | 7.824          | 10.042         | 12.121         | Retry failed 3 times |
| defog/sqlcoder-34b-alpha | 84.0%       | 143.395        | 65.929         | 24.730         | 48.097               |
| defog/sqlcoder2          | 74.5%       | 9.356          | 11.901         | 12.954         | 25.270               |
