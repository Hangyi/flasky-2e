import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing') # 创建一个测试环境，类似于运行中的程序。使用测试配置创建程序
        self.app_context = self.app.app_context() 
        self.app_context.push() # 激活上下文，确保能在测试中使用current_app
        db.create_all() # 创建一个新的数据库

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        """测试确保程序实例存在"""
        self.assertFalse(current_app is None) 

    def test_app_is_testing(self):
        """测试确保程序在测试配置中运行"""
        self.assertTrue(current_app.config['TESTING']) 