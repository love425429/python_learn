#!/usr/bin/env python2.7
# coding: utf-8
import unittest
class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

class mytest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testSingletonAddr(self):
        class b(Singleton):
            def __init__(self,s):
                self.s=s
            def getS(self):
                return self.s
        s1 = b(1)
        s2 = b(2)
        self.assertEqual(id(s1)==id(s2),True,"test addr is the same fail")
        self.assertEqual(s1.getS()==s2.getS(),True,"test value is the same fail")
        
if __name__ =="__main__":
    unittest.main()
