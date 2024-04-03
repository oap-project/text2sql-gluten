import os
import time
from langchain_community.llms import VLLM
from pyspark_ai import SparkAI

# Set the environment variable
os.environ["OMP_NUM_THREADS"] = "32"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Start timer
start_time = time.time()

# Initialize the VLLM
llm = VLLM(
    #optional models:
    #defog/sqlcoder-70b-alpha 93.0%
    #defog/sqlcoder-7b-2      90.5%
    #defog/sqlcoder-34b-alpha 84.0%
    #defog/sqlcoder2          74.5%
    #defog/sqlcoder-7b        71.0%
    #defog/sqlcoder           64.6%
    model="defog/sqlcoder-7b-2",
    trust_remote_code=True,
    download_dir="/mnt/DP_disk2/models/Huggingface/", #~/.conda/envs/zedong-vllm/lib/python3.10/site-packages/langchain_community/llms/vllm.py:88
)

# Initialize and activate SparkAI
spark_ai = SparkAI(llm=llm,verbose=True)
spark_ai.activate()

# create a dataframe productRevenue
df = spark_ai._spark.createDataFrame(
    [
        ("Normal", "Cellphone", 6000),
        ("Normal", "Tablet", 1500),
        ("Mini", "Tablet", 5500),
        ("Mini", "Cellphone", 5000),
        ("Foldable", "Cellphone", 6500),
        ("Foldable", "Tablet", 2500),
        ("Pro", "Cellphone", 3000),
        ("Pro", "Tablet", 4000),
        ("Pro Max", "Cellphone", 4500)
    ],
    ["product", "category", "revenue"]
)

init_time = time.time() - start_time
print(f"Init time: {init_time} seconds")

start_time = time.time()
df.ai.transform("What is the best-selling product?").show()
task1_time = time.time() - start_time
print(f"Task1 time: {task1_time} seconds")

start_time = time.time()
df.ai.transform("Pivot the data by product and the revenue for each product").show()
task2_time = time.time() - start_time
print(f"Task2 time: {task2_time} seconds")

start_time = time.time()
df.ai.transform("Pivot the data by catagory and the revenue for each product").show()
task3_time = time.time() - start_time
print(f"Task3 time: {task3_time} seconds")

start_time = time.time()
df.ai.transform("What are the best-selling and the second best-selling products in every category?").show()
task4_time = time.time() - start_time

#df.ai.transform("What is the difference between the revenue of each product and the revenue of the best-selling product in the same category of that product?").show()

#df.ai.plot()

print(f"Init time: {init_time} seconds")
print(f"Task1 time: {task1_time} seconds")
print(f"Task2 time: {task2_time} seconds")
print(f"Task3 time: {task3_time} seconds")
print(f"Task4 time: {task4_time} seconds")