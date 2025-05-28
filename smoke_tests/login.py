from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest

# номер 3
def test_guest_can_login():
    result = 1 + 1
    assert result == 3, "1 + 1 должно быть равно 2"

# номер 4
class TestLogin(unittest.TestCase):
    def test_guest_should_see_login_link(self):
        result = 1 + 1
        self.assertEqual(result, 3)  # Проверяем, что 1 + 1 == 2
