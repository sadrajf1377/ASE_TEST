import json
import math
from decimal import Decimal

from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class test_sin(TestCase):
    def setUp(self):
        value = 30
        radian = (3.14 / 180) * value
        self.sin= math.sin(radian)

    def test(self):
        value = 30
        sin=json.loads(self.client.get(reverse('get_sin',args=[value])).content)['result']
        self.assertEqual(self.sin,sin,msg='sin function failed')

class test_cos(TestCase):
    def setUp(self):
        rad=(3.14/180)*30
        self.cos=math.cos(rad)
    def test(self):
        value=30
        response=json.loads(self.client.get(reverse('get_cos',args=[value])).content)
        self.assertEqual(response['result'],self.cos,msg='cos function failed')

class test_cot(TestCase):
    def setUp(self):
        rad=(3.14/180)*30
        self.cot=math.tan(rad)**-1
    def test(self):
        value=30
        response=json.loads(self.client.get(reverse('get_cot',args=[value])).content)
        self.assertEqual(response['result'],self.cot,msg='cot function failed')

class test_tan(TestCase):
    def setUp(self):
        rad=(3.14/180)*30
        self.tan=math.tan(rad)
    def test(self):
        value=30
        response=json.loads(self.client.get(reverse('get_tan',args=[value])).content)
        self.assertEqual(response['result'],self.tan,msg='tan function failed')