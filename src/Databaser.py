import MySQLdb
import datetime
DB_SESSION_Table = "Table_1"




class Databaser():
    counter = 0
    count=0
    TABLENO=1

    def __init__(self):
        global DB_SESSION_Table
        try:
            fo = open("eboard.cnf", "rb")
            self.DB_IP = fo.readline()
            fo.close()
        except:
            self.DB_IP = "193.11.187.1"

        self.DB_UserName = "eboard"
        self.DB_Password = "eboard"
        self.DB_PORT = 3306
        self.DB_DBName = "electroblitz"
        self.DB_Table = "user_table"
        self.DB_SESSION_Table = "Table_1"

    def UPDATE(self):
        global DB_SESSION_Table
        try:
            fo = open("eboard.cnf", "rb")
            self.DB_IP = fo.readline()
            fo.close()
        except:
            self.DB_IP = "193.11.187.1"

        self.DB_UserName = "eboard"
        self.DB_Password = "eboard"
        self.DB_PORT = 3306
        self.DB_DBName = "electroblitz"
        self.DB_Table = "user_table"
        self.DB_SESSION_Table = DB_SESSION_Table

    def CREATE_TABLE(self):
        db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT,
                             user=self.DB_UserName)
        cursor = db.cursor()
        sql = "create table %s(user CHAR(30), passcode CHAR(155), user_type CHAR(20), moderator CHAR(10), locked CHAR(10), loggedin CHAR(10))" % self.DB_Table
        cursor.execute(sql)
        db.commit()

        db.close()

    def CREATE_SESSION_TABLE(self):
        global DB_SESSION_Table
        try:
           db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT,
                             user=self.DB_UserName)
        except:
           print ""
        cursor = db.cursor()
        sql = "create table Table_1(SNO INT(10), SHEET_NO INT(10), MODIFICATION CHAR(200), USER CHAR(10), TIME_STAMP TIMESTAMP)"
        DB_SESSION_Table = "Table_1"

        cursor.execute(sql)
        db.commit()

        db.close()


    def REMOVE_USER(self, user):

            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "delete from %s where user = '%s'" % (self.DB_Table, user)
            cursor.execute(sql)
            db.commit()

            db.close()

    def POP_USER(self):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "SELECT user FROM %s" % self.DB_Table
            cursor.execute(sql)
            result = cursor.fetchall()
            result = list(result)
            list1 = []
            for row in result:
                p = row[0]
                list1.append(p)
            db.close()
            return list1

    def POP_TYPE(self, type):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "SELECT user FROM %s where user_type = '%s'" % (self.DB_Table, type)
            result = cursor.fetchall()
            result = list(result)
            list1 = []
            for row in result:
                p = row[0]
                list1.append(p)
            db.close()
            return list1

    def POP_LOCK(self):
                db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
                cursor = db.cursor()
                sql = "SELECT user FROM %s where locked = 'YES'" % self.DB_Table
                cursor.execute(sql)
                result = cursor.fetchall()
                result = list(result)
                list1 = []
                for row in result:
                    p = row[0]
                    list1.append(p)
                db.close()
                return list1

    def POP_USER_TYPE(self,user):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "SELECT user_type FROM %s where user = '%s'" % (self.DB_Table, user)
            cursor.execute(sql)
            result = cursor.fetchall()
            result = list(result)
            print result
            result = result[0][0]
            return result


    def POP_MODERATOR(self):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "SELECT user FROM %s where moderator = 'YES'" % self.DB_Table
            cursor.execute(sql)
            result = cursor.fetchall()
            result = list(result)
            list1 = []
            for row in result:
                p = row[0]
                list1.append(p)
            db.close()
            return list1

    def PUSH_DATA(self,user,type):

           db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
           cursor = db.cursor()
           sql = "INSERT INTO %s(user, user_type, moderator, locked, loggedin) VALUES ('%s', '%s', 'NO', 'NO', 'NO')" % (self.DB_Table,user, type)
                # Execute the SQL command
           cursor.execute(sql)
            # Commit your changes in the database
           db.commit()

           db.close()


    def PUSH_LOCK(self, user):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "UPDATE %s set locked = 'YES' where user = '%s'" % (self.DB_Table,user)
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()

            db.close()

    def PUSH_LOGGEDIN(self, user):
        db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT,
                             user=self.DB_UserName)
        cursor = db.cursor()
        sql = "UPDATE %s set loggedin = 'YES' where user = '%s'" % (self.DB_Table, user)
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()

        db.close()

    def PUSH_LOGGEDOUT(self, user):
        db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT,
                             user=self.DB_UserName)
        cursor = db.cursor()
        sql = "UPDATE %s set loggedin = 'NO' where user = '%s'" % (self.DB_Table, user)
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()

        db.close()



    def PUSH_UNLOCK(self, user):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "UPDATE %s set locked = 'NO' where user = '%s'" % (self.DB_Table,user)
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()

            db.close()

    def PUSH_MODERATOR(self,user):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "UPDATE %s set moderator = 'YES' where user = '%s'" % (self.DB_Table,user)
            # Execute the SQL command
            cursor.execute(sql)
            #   Commit your changes in the database
            db.commit()

            db.close()

    def kicker(self,user):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "SELECT * FROM %s" % self.DB_Table
            cursor.execute(sql)
            result = cursor.fetchall()
            result = list(result)
            now=datetime.datetime.now()
            for index,row in enumerate(result):
                p = row[0]
                if (user==p):
                    v= row[1]
                    k=now-v
                    period=k.total_seconds()
                    if (period>259200):

                        print ('Validity expired')
                        sql = "delete from %s where user = '%s'"  % (self.DB_Table,user)
                        cursor.execute(sql)
                        db.commit()

                    else:
                            print ('Valid user')
            db.close()

    def PUSH_UNMODERATOR(self, user):
            db = MySQLdb.connect(passwd=self.DB_Password, db=self.DB_DBName, host=self.DB_IP, port=self.DB_PORT, user=self.DB_UserName)
            cursor = db.cursor()
            sql = "UPDATE %s set moderator = 'NO' where user = '%s'" % (self.DB_Table,user)
            # Execute the SQL command
            cursor.execute(sql)
            #   Commit your changes in the database
            db.commit()
            db.close()
