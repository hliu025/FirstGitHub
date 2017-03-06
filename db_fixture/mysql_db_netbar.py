# coding=utf-8
import pymysql.cursors
import os
import configparser as cparser


# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
print(base_dir)
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config_netbar.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db   = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")

# ======== MySql base operating ===================
class DB:
    def __init__(self):
        try:
            # Connect to the database
            '''self.connection = pymysql.connect(host=host,
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)'''
            self.connection=pymysql.connect(host='127.0.0.1',
                                            user='root',
                                            password='123456',
                                            port=3309,
                                            db='netbar',
                                            charset='utf8mb4',
            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()
    # close database
    def close(self):
        self.connection.close()


if __name__ == '__main__':
    db = DB()
    table_name = "ap_group"
    data = {'id':12,'name':'testAP','remarks':'add successfully','ap_num':1,'store_id':104,'merchant_id':102,'config_version':1,'portal_id':1,'ssid':'hliussid'}
    db.clear(table_name)
    db.insert(table_name, data)

    db.close()
