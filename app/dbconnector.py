import mysql.connector


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="yizhou"
# )

def connect2db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="bot",
    password="botpass"
    )
    

    return mydb



if __name__ == "__main__":


    mycursor = mydb.cursor()

    sql = "INSERT INTO wx.wxdata (wxid, xing, app1,id1,app2,id2,app3,id3) VALUES (%s,%s,%s,%s,%s,%s, %s,%s)"
    val = ("asdf", 'asdf','inbvia','sadf',"asdf", 'asdf','inbvia','sadf')
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")



    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM wx.wxdata limit 10")

    myresult = mycursor.fetchall()



