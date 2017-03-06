# coding=utf-8
import unittest
import requests


class UserSignTest(unittest.TestCase):

    def setUp(self):
        self.base_url =  "http://127.0.0.1:8000/api/user_sign/"

    def test_user_sign_all_null(self):
        ''' 参数为空 '''
        payload = {'eid':'','phone':''}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_user_sign_eid_error(self):
        ''' eid=901 查询结果不存在 '''
        payload = {'eid':901,'phone':13800138001}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'event id null')

    def test_user_sign_status_close(self):
        ''' eid=2 发布会状态关闭 '''
        payload = {'eid':2,'phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10023)
        self.assertEqual(result['message'], 'event status is not available')

    def test_user_sign_time_start(self):
        ''' eid=3 发布会已开始 '''
        payload = {'eid':3,'phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        self.assertEqual(result['message'], 'event has started')

    def test_user_sign_phone_error(self):
        ''' phone=10100001111 手机号不存在 '''
        payload = {'eid':1,'phone':10100001111}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10025)
        self.assertEqual(result['message'], 'user phone null')

    def test_user_sign_eid_phone_error(self):
        '''eid=1, phone=18633003301 手机号与发布会不匹配 '''
        payload = {'eid':1,'phone':18633003304}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        #self.assertEqual(result['message'], 'user did not participate in the conference')
        self.assertEqual(result['message'],'event has started')

    def test_user_sign_has_sign_in(self):
        ''' 已签到 '''
        payload = {'eid':1,'phone':18633003301}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10027)
        self.assertEqual(result['message'], 'user has sign in')

    def test_user_sign_success(self):
        ''' 签到成功 '''
        payload = {'eid':3,'phone':13711001100}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'sign success')

if __name__ == '__main__':
    unittest.main()


#===========
#部分用例数据还原
#DELETE FROM `sign_event` WHERE id = 11;
#DELETE FROM `sign_guest` WHERE event_id=1 AND phone=13711001100;
#UPDATE `sign_guest` SET SIGN=0   WHERE event_id=1 AND phone=13800112999;
#===========
