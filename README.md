# Summary of GitHub Repositories

texttosql: https://github.com/oap-project/text2sql-gluten

vllm: https://github.com/PZD-CHINA/vllm/tree/vllm-cpu-only

langchain: https://github.com/PZD-CHINA/langchain.git

pyspark-ai: https://github.com/PZD-CHINA/pyspark-ai.git

demo result: http://mlp-sdp-spr-7639.jf.intel.com:8888/tree/zedong/texttosql-demo (password: intel123)

# Summary of Model Correctness and Time Performance
| Model                    | Correctness from doc | Time                        |
|--------------------------|----------------------|-----------------------------|
| defog/sqlcoder-70b-alpha | 93.0%                | Init time: 24.536 seconds   |
|                          |                      | Task1 time: 98.674 seconds  |
|                          |                      | Task2 time: 140.440 seconds |
|                          |                      | Task3 time: 45.481 seconds  |
|                          |                      | Task4 time: 223.176 seconds |
| defog/sqlcoder-7b-2      | 90.5%                | Init time: 5.174 seconds    |
|                          |                      | Task1 time: 7.824 seconds   |
|                          |                      | Task2 time: 10.042 seconds  |
|                          |                      | Task3 time: 12.121 seconds  |
|                          |                      | Task4 time: retry failed 3 times |
| defog/sqlcoder-34b-alpha | 84.0%                | Init time: 24.161 seconds   |
|                          |                      | Task1 time: 143.395 seconds |
|                          |                      | Task2 time: 65.929 seconds   |
|                          |                      | Task3 time: 24.730 seconds   |
|                          |                      | Task4 time: 48.097 seconds   |
| defog/sqlcoder2          | 74.5%                | Init time: 16.764 seconds   |
|                          |                      | Task1 time: 9.356 seconds    |
|                          |                      | Task2 time: 11.901 seconds   |
|                          |                      | Task3 time: 12.954 seconds   |
|                          |                      | Task4 time: 25.270 seconds   |
