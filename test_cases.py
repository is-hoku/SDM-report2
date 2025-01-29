#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

    # def test_sample1(self):
    #     self.assertEqual(21, calc(3, 7))

    # def test_sample2(self):
    #     self.assertEqual(-1, calc(0, 150))

    # def test_sample3(self):
    #     self.assertEqual(-1, calc('a', 'b'))

    # def test_sample4(self):
    #     self.assertEqual(-1, calc(0.1, 999))

    # 正常な入力
    def test_valid_cases(self):
        self.assertEqual(1, calc(1, 1))  # 最小境界
        self.assertEqual(200, calc(10, 20))  # 有効値
        self.assertEqual(998001, calc(999, 999))  # 最大境界

    # 異常な入力 (整数)
    def test_out_of_range(self):
        self.assertEqual(-1, calc(0, 100))  # 最小境界の直前
        self.assertEqual(-1, calc(1000, 5))  # 最大境界の直後
        self.assertEqual(-1, calc(-5, 500))  # 負の数
        self.assertEqual(-1, calc(500, 1001))  # 一方が範囲外

    # 異常な入力 (整数以外)
    def test_invalid_types(self):
        self.assertEqual(-1, calc(1.5, 2))  # 小数
        self.assertEqual(-1, calc('10', 5))  # 数字の文字列
        self.assertEqual(-1, calc('a', 100))  # 文字列
        self.assertEqual(-1, calc(5, 'y'))  # 文字列
        self.assertEqual(-1, calc('a', 'b'))  # 両方が文字列
        self.assertEqual(-1, calc(None, 5))  # None
        self.assertEqual(-1, calc(10, None))  # None
        self.assertEqual(-1, calc([], 5))  # リスト
        self.assertEqual(-1, calc({}, 10))  # 辞書

    # 異常な入力 (その他)
    def test_both_invalid(self):
        self.assertEqual(-1, calc(-1, 'x'))
        self.assertEqual(-1, calc('x', None))
        self.assertEqual(-1, calc(1000, 0.5))
