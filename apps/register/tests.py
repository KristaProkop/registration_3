# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TmobileTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(TmobileTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TmobileTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/tmobile/')
        #find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        email = selenium.find_element_by_id('id_email')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_name('register')

        first_name.send_keys('Krista')
        last_name.send_keys('Prokopczyk')
        email.send_keys('krista@gmail.com')
        password.send_keys('password')

        submit.send_keys(Keys.RETURN)
        
