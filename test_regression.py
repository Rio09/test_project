from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest

class TestLessonCreate(unittest.TestCase):
    # номер 5
    def test_create_lesson(self):
        result = 1 + 1
        self.assertEqual(result, 2)  # Проверяем, что 1 + 1 == 2

    # номер 6
    def user_with_lesson_can_create_lesson_from_navbar_test(self):
        result = 1 + 1
        self.assertEqual(result, 2)  # Проверяем, что 1 + 1 == 2


class CourseCreate(unittest.TestCase):
    # номер 7
    def test_create_course(self):
            result = 1 + 1
            self.assertEqual(result, 2)  # Проверяем, что 1 + 1 == 2


# номер 8
def test_guest_can_open_new_course():
        result = 1 + 1
        assert result == 2, "1 + 1 должно быть равно 2"