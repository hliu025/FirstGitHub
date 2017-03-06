# coding=utf-8
import unittest
import requests


class GetEventListTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_list_eid_null(self):
        ''' eid 参数为空 '''
        r = requests.get(self.base_url, params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_list_eid_error(self):
        ''' eid=901 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':901})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':1})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['name'],u'xx产品发布会')
        self.assertEqual(result['data']['address'],u'北京林匹克公园水立方')

    def test_get_event_list_nam_result_null(self):
        ''' 关键字‘abc’查询 '''
        r = requests.get(self.base_url, params={'name':'abc'})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_list_name_find(self):
        ''' 关键字‘发布会’模糊查询 '''
        r = requests.get(self.base_url, params={'name':'mx6'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data'][0]['name'],u'mx6发布会')
        self.assertEqual(result['data'][0]['address'],u'北京国家会议中心')

if __name__ == '__main__':
    unittest.main()


#===========
#部分用例数据还原
#DELETE FROM `sign_event` WHERE id = 11;
#DELETE FROM `sign_guest` WHERE event_id=1 AND phone=13711001100;
#UPDATE `sign_guest` SET SIGN=0   WHERE event_id=1 AND phone=13800112999;
#===========
