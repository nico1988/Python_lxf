# 按照mysql驱动 pip install mysql-connector-python --allow-external mysql-connector-python
# 或者 pip install mysql-connector
import mysql.connector
conn = mysql.connector.connect(user='root',password='nico',database='test')