


def precheck(form):

    return True

def insertion(form, mydb):
    if precheck(form):
        mycursor = mydb.cursor()

        sql = "INSERT INTO wx.wxdata (wxid, xing, app1,id1,app2,id2,app3,id3) VALUES (%s,%s,%s,%s,%s,%s, %s,%s)"
        val = (form.mywxid.data,form.mylname.data, form.app1.data, form.id1.data,
        form.app2.data, form.id2.data, form.app3.data, form.id3.data)
        mycursor.execute(sql, val)
        mydb.commit()
    return val





def searchdb(form, mydb,number=1):

    mycursor = mydb.cursor()

    sql="SELECT * FROM wx.wxdata where wxid = '{}' and xing = '{}' ORDER BY id DESC  LIMIT {} ".format(form.wxid.data,form.lastname.data,number)
    print(sql)
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return myresult