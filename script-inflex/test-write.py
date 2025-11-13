# -------- InfluxDB Python Example --------
# Ghi dữ liệu mẫu vào bucket "credit-card-analytics"
# ------------------------------------------

import os, time
from influxdb_client_3 import InfluxDBClient3, Point
from dotenv import load_dotenv

load_dotenv()

# ======= Cấu hình từ .env =======
token = os.getenv("INFLUX_TOKEN")
org = os.getenv("INFLUX_ORG")
host = os.getenv("INFLUX_HOST")
database = os.getenv("INFLUX_DATABASE")

# ======= Kết nối đến InfluxDB =======
client = InfluxDBClient3(host=host, token=token, org=org)


data = {
  "point1": {
    "location": "Klamath",
    "species": "bees",
    "count": 23,
  },
  "point2": {
    "location": "Portland",
    "species": "ants",
    "count": 30,
  },
  "point3": {
    "location": "Klamath",
    "species": "bees",
    "count": 28,
  },
  "point4": {
    "location": "Portland",
    "species": "ants",
    "count": 32,
  },
  "point5": {
    "location": "Klamath",
    "species": "bees",
    "count": 29,
  },
  "point6": {
    "location": "Portland",
    "species": "ants",
    "count": 40,
  },
}

for key in data:
  point = (
    Point("census")
    .tag("location", data[key]["location"])
    .field(data[key]["species"], data[key]["count"])
  )
  client.write(database=database, record=point)
  time.sleep(1) # separate points by 1 second

print("Complete. Return to the InfluxDB UI.")

# ======= Đóng kết nối =======
client.close()
