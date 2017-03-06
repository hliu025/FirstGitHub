# coding=utf-8
import unittest
import requests


class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid':1,'':'','limit':'','address':"",'start_time':''}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        ''' id已经存在 '''
        payload = {'eid':1,'name':'一加4发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' 名称已经存在 '''
        payload = {'eid':11,'name':'一加3手机发布会','limit':2000,'address':"深圳宝体",'start_time':'27'}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10023)
        self.assertEqual(result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        self.assertIn('start_time format error.', result['message'])

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid':3,'name':'三星note7手机发布会','limit':2000,'address':"北京奥运村",'start_time':'2017-04-10 12:00:00'}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'add event success')



if __name__ == '__main__':
    unittest.main()


#===========
#部分用例数据还原
#DELETE FROM `sign_event` WHERE id = 11;
#DELETE FROM `sign_guest` WHERE event_id=1 AND phone=13711001100;
#UPDATE `sign_guest` SET SIGN=0   WHERE event_id=1 AND phone=13800112999;
#===========
