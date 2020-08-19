import unittest

from Learning_from_python_crash_course_book.city_functions import city_info

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        santiago_chile = city_info('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        santiago_chile = city_info('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':

    unittest.main()
