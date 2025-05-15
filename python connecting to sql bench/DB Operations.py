import mysql.connector

con = mysql.connector.connect(host="localhost",port='3306',user="root",passwd="admin",database="schooldb")

curs = con.cursor()

curs.execute("select * from Invest")
for row in curs :
    print(row[0],row[1],row[2])

con.close()
print('finished')



# curs = con.cursor()
# curs.execute("Update students set Firstname = 'Jacky' where Firstname = 'smith';")
# con.commit()
# con.close()
# print("Finished")
