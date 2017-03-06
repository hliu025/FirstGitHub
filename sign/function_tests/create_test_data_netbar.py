#coding=utf-8
'''
创建表（ap_group）测试数据。
'''
f = open("ap_group.txt",'w')

for i in range(1, 300):
    id = str(i)
    name = "testeAP" + id
    remark="add successfully"
    #ap_num=1
    store_id = 100+ i
    merchant_id=100+i
    #config_version=1
    #portal_id=1
    ssid="hliuSSID"
    sql = 'INSERT INTO ap_group (id, name, remark, ap_num,store_id, merchant_id, config_version, portal_id,ssid) VALUES ('+id+',"'+name+'","'+remark+'",1,"'+str(store_id)+'","'+str(merchant_id)+'",1,1,"'+ssid+'" );'
    f.write(sql)
    f.write("\n")

f.close()
