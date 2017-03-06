# coding=utf-8
import unittest
import requests

class AddGuestTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_guest/"

    def test_add_guest_all_null(self):
        ''' 参数为空 '''
        payload = {'eid':'','realname':'','phone':''}
        r = requests.get(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_add_guest_eid_null(self):
        ''' eid=901 查询为空 '''
        payload = {'eid':901,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'event id null')

    def test_add_guest_status_close(self):
        ''' eid=2 状态未开启 '''
        payload = {'eid':2,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10023)
        self.assertEqual(result['message'], 'event status is not available')

    def test_add_guest_limit_full(self):
        ''' eid=3 发布会人数已满 '''
        payload = {'eid':3,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        self.assertEqual(result['message'], 'event number is full')

    def test_add_guest_time_start(self):
        ''' eid=4 发布会已开始 '''
        payload = {'eid':4,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10025)
        self.assertEqual(result['message'], 'event has started')

    def test_add_guest_phone_repeat(self):
        ''' phone=13800113001 手机号重复 '''
        payload = {'eid':3,'realname':'tom','phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10026)
        self.assertEqual(result['message'], 'the event guest phone number repeat')

    def test_add_guest_success(self):
        ''' 添加成功 '''
        payload = {'eid':3,'realname':'David','phone':13711001101}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'add guest success')

if __name__ == '__main__':
    unittest.main()


#===========
#部分用例数据还原
#DELETE FROM `sign_event` WHERE id = 11;
#DELETE FROM `sign_guest` WHERE event_id=1 AND phone=13711001100;
#UPDATE `sign_guest` SET SIGN=0   WHERE event_id=1 AND phone=13800112999;
#===========
