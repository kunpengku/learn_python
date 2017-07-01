#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import mock

import client


class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(client.visit_ustack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(client.visit_ustack(), '404')
