import sys
sys.path.append('../db_fixture')
from mysql_db import DB


# create data
datas = {
    'ap_group':[
        {'id':1,'name':'testAP1','remarks':'add successfully','ap_num':1,'store_id':103,'merchant_id':102,'config_version':1,'portal_id':1,'ssid':'hliussid'},
        {'id':2,'name':'testAP1','remarks':'add successfully','ap_num':1,'store_id':103,'merchant_id':102,'config_version':1,'portal_id':1,'ssid':'hliussid'},
        {'id':3,'name':'testAP3','remarks':'add successfully','ap_num':1,'store_id':103,'merchant_id':102,'config_version':1,'portal_id':1,'ssid':'hliussid'},
        {'id':4,'name':'testAP4','remarks':'add successfully','ap_num':1,'store_id':103,'merchant_id':102,'config_version':1,'portal_id':1,'ssid':'hliussid'},
    ],
}
# Inster table datas
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()

if __name__ == '__main__':
    init_data()
