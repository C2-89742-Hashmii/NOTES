
# input username & password from user and display login success/failed message

import mysql.connector

try:
    with mysql.connector.connect(
      host = "localhost",
      user = "appusr",
      password = "app@usr",
      database = "myapp"
    ) as db:
      with db.cursor() as cur:
        user = input("Enter username: ")
        passwd = input("Enter password: ")
        sql = f"SELECT * FROM users WHERE username=%s AND password=%s"
        print("executing :", sql)
        cur.execute(sql, params=(user, passwd))
        users = cur.fetchall()
        if users:
          print(f"Welcome, {user}!")
        else:
          print("Invalid Login.")
  except Exception as e:
      print(e)
      
