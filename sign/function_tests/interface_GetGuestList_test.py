# coding=utf-8
import unittest
import requests



class GetGuestListTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/get_guest_list/"

    def test_get_guest_list_eid_null(self):
        ''' eid 参数为空 '''
        r = requests.get(self.base_url, params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'eid cannot be empty')

    def test_get_event_list_eid_error(self):
        ''' 根据 eid 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':901})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':2})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data'][0]['realname'],'张三')
        self.assertEqual(result['data'][0]['phone'],'13800138000')

    def test_get_event_list_eid_phone_null(self):
        ''' 根据 eid 和phone 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':2,'phone':'10000000000'})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_list_eid_phone_success(self):
        ''' 根据 eid 和phone 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':2,'phone':'13800138000'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['realname'],'张三')
        self.assertEqual(result['data']['phone'],'13800138000')

if __name__ == '__main__':
    unittest.main()


#===========
#部分用例数据还原
#DELETE FROM `sign_event` WHERE id = 11;
#DELETE FROM `sign_guest` WHERE event_id=1 AND phone=13711001100;
#UPDATE `sign_guest` SET SIGN=0   WHERE event_id=1 AND phone=13800112999;
#===========
