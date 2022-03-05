# database connectivity file
import pymysql as pm

class Connection:
    def __init__(self):
        self.con = pm.connect(host='localhost',user='root',password='admin',database='boi')
        self.cursor = self.con.cursor()

    def storeUser(self,email,pass1):
        sql="insert into users values ('%s','%s')" % (email,pass1)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        return self.status

    def checkUser(self,email,pass1):
        sql="select * from users where emailid = '%s' and password = '%s'" % (email,pass1)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status

    def storeAccount(self,email, acno, amt):
        sql = "insert into account values ('%s','%d','%f')" % (email, acno, amt)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status = True
        except:
            self.con.rollback()
            self.status = False
        return self.status

    def checkAccount(self, email, acno):
        sql = "select * from account where emailid = '%s' and acno = '%d'" % (email, acno)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            data = self.cursor.fetchone()
            balance = data[2]
        else:
            balance = -1
        return balance

    def storeTrans(self,email, acno, amt, type):
        if type=='Deposit':
            sql = "update account set balance = balance + '%f' where emailid ='%s' and acno = '%d'" % (amt, email, acno)
        else:
            sql = "update account set balance = balance - '%f' where emailid ='%s' and acno = '%d'" % (amt, email, acno)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status = True
        except:
            self.con.rollback()
            self.status = False
        return self.status

    def storeRecharge(self,email, acno, amt, type):
        sql = "update account set balance = balance - '%f' where emailid ='%s' and acno = '%d'" % (amt, email, acno)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status = True
        except:
            self.con.rollback()
            self.status = False
        return self.status

    def storeFundTranser(self,email, acno1, acno2, amt):
        sql = "update account set balance = balance - '%f' where emailid ='%s' and acno = '%d'" % (amt, email, acno1)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            sql = "update account set balance = balance + '%f' where emailid ='%s' and acno = '%d'" % (
            amt, email, acno2)
            self.cursor.execute(sql)
            self.con.commit()
            self.status = True
        except:
            self.con.rollback()
            self.status = False
        return self.status

    def checkAccount(self, email, acno):
        sql = "select * from account where emailid = '%s' and acno = '%d'" % (email, acno)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            data = self.cursor.fetchone()
            balance = data[2]
        else:
            balance = -1
        return balance

    def checkPassword(self, email, pass1):
        sql = "select * from users where emailid = '%s' and password = '%s'" % (email, pass1)
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            status = True
        else:
            status = False
        return status

    def updatePassword(self,email, oldp, newp):
        sql = "update users set password = '%s' where emailid ='%s' and password = '%s'" % (newp, email, oldp)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status = True
        except:
            self.con.rollback()
            self.status = False
        return self.status