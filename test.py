# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File  : test.py
@Author: White Gui
@Date  : 2024/8/16
@Desc :
"""
import unittest

from main import get_final_index


class TestTemplate(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_final(self):
        first = get_final_index(6, 1, 6)
        self.assertEqual(first, "小吉")
        second = get_final_index(3, 5, 1)
        self.assertEqual(second, "大安")
        third = get_final_index(4, 10, 11)
        self.assertEqual(third, "小吉")


if __name__ == '__main__':
    unittest.main()
