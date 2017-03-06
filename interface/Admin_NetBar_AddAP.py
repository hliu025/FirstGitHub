#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import AdminLogin
import unittest
import HTMLTestRunner
import logging
import requests
import json
import os,sys
from db_fixture import test_data_netbar
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class AddAP(unittest.TestCase):
    '''无线设备组添加接口'''
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        AdminLogin.login(self.driver)
        driver=self.driver
        self.verificationErrors=[]
        self.url_test='http://172.16.1.12/admin/ap/group/add'
        cookies=driver.get_cookies()
        self.JSESSIONID=cookies[1]['value']
    def test_AddAP_01_Success(self):
        '''添加成功'''
        payload={'name':'InterfaceAP','ssid':'hliuSSID','remarks':'add successfully!','portalId':1,
                 'merchantId':102,'storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        result=requests.post(self.url_test,data=payload,headers=headers).json()
        #print(result)
        self.assertEqual(result['code'],200)
        #self.assertEqual(result['desc'],'操作成功')
        self.assertEqual(result['desc'],'operation.success')
        #print(result)
    def test_AddAP_02_Name_Null(self):
        '''name为空'''
        payload={'name':'','ssid':'hliuSSID','remarks':'add successfully!','portalId':1,
                 'merchantId':102,'storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            print(result)
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_03_Name_LongStr(self):
        '''name长度超过规定'''
        payload={'name':'hliuSSIDhliuSSIDhliuSSIDhliuSSIDhliu','ssid':'hliuSSID','remarks':'add successfully!','portalId':1,
                 'merchantId':102,'storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_04_Name_LessStr(self):
        '''name长度小于规定'''
        payload={'name':'h','ssid':'hliuSSID','remarks':'add successfully!','portalId':1,
                 'merchantId':102,'storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_05_PortalId_Null(self):
        '''portalId为空'''
        payload={'name':'testAP1','ssid':'hliuSSID','remarks':'add successfully!','portalId':'',
                 'merchantId':102,'storeId':''}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_06_StoreId_Null(self):
        '''storeId为空'''
        payload={'name':'testAP2','ssid':'hliuSSID','remarks':'add successfully!','portalId':'',
                 'merchantId':102,'storeId':''}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_07_StoreId_NotExist(self):
        '''storeId不存在'''
        payload={'name':'testAP3','ssid':'hliuSSID','remarks':'add successfully!','portalId':1,
                 'merchantId':102,'storeId':1000000}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_08_PortalId_NotExist(self):
        '''portalId不存在'''
        payload={'name':'testAP4','ssid':'hliuSSID','remarks':'add successfully!','portalId':10000,
                 'merchantId':102,'storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_09_MerchantId_NotExist(self):
        '''merchantId不存在'''
        payload={'name':'testAP5','ssid':'hliuSSID','remarks':'add successfully!','portalId':1,
                 'merchantId':100000,'storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_10_MerchantId_Null(self):
        '''merchantId为空'''
        payload={'name':'testAP6','ssid':'hliuSSID','remarks':'add successfully!','portalId':1,
                 'merchantId':'','storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        try:
            result=requests.post(self.url_test,data=payload,headers=headers).json()
            self.assertEqual(result['code'],422)
            self.assertEqual(result['desc'],'错误的参数')
            print(result)
        except ValueError as e:
            print(e)
            self.verificationErrors.append(e)
    def test_AddAP_11_Name_Exist(self):
        '''name已经存在'''
        payload={'name':'InterfaceAP','ssid':'hliuSSID','remarks':'add successfully!!','portalId':1,
                 'merchantId':102,'storeId':103}
        headers={'Cookie':'MYSERVERID=init; JSESSIONID='+self.JSESSIONID}
        result=requests.post(self.url_test,data=payload,headers=headers).json()
        #print(result)
        self.assertEqual(result['code'],400)
        self.assertEqual(result['desc'],'已存在同名设备组')
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    test_data_netbar.init_data()
    unittest.main()

