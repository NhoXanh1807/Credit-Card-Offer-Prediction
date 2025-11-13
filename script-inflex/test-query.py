# -------- Query data from InfluxDB using SQL --------
# Bạn cần đã ghi dữ liệu (từ ví dụ trước)
# ------------------------------------------

import os, time
from influxdb_client_3 import InfluxDBClient3, Point
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# ======= Cấu hình từ .env =======
token = os.getenv("INFLUX_TOKEN")
org = os.getenv("INFLUX_ORG")          # hoặc tên org thật trong InfluxDB Cloud
host = os.getenv("INFLUX_HOST")
database = os.getenv("INFLUX_DATABASE")

# ======= Kết nối client =======
client = InfluxDBClient3(host=host, token=token, org=org)

# ======= Câu truy vấn SQL =======
query = """
SELECT *
FROM 'census'
WHERE time >= now() - interval '24 hours'
  AND ('bees' IS NOT NULL OR 'ants' IS NOT NULL)
"""

# ======= Thực thi truy vấn =======
table = client.query(query=query, database=database, language='sql') 

df = table.to_pandas().sort_values(by="time")
print(df)
client.close()
