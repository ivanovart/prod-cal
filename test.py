#!/usr/bin/env python
# -*- coding: utf-8 -*-

from holidays import ProdCal
from datetime import date
from holidays.service import get_date_today
import unittest


class BasicTestCaseRU(unittest.TestCase):
	my_first_prod_cal = ProdCal(locale='RU')

	def test_is_work_day(self):
		# Проверяем праздничный день 1 мая
		self.assertEqual(self.my_first_prod_cal.is_work_day(2016, 5, 1), False)
		# Проверяем рабочий день
		self.assertEqual(self.my_first_prod_cal.is_work_day(2016, 4, 1), True)
		# Проверяем выходной день
		self.assertEqual(self.my_first_prod_cal.is_work_day(2016, 4, 2), False)
		# Проверяем перенос празничного дня (рабочий день)
		self.assertEqual(self.my_first_prod_cal.is_work_day(2016, 2, 20), True)
		# Передаём сразу объект даты
		self.assertEqual(self.my_first_prod_cal.is_work_day(date(2016, 5, 1)), False)
		# Передаём в качестве аргумента строку (today - сегодня)
		self.assertEqual(self.my_first_prod_cal.is_work_day('today'),
		                 self.my_first_prod_cal.is_work_day(get_date_today('today')))
		# Передаём в качестве аргумента строку (yesterday - вчера)
		self.assertEqual(self.my_first_prod_cal.is_work_day('yesterday'),
		                 self.my_first_prod_cal.is_work_day(get_date_today('yesterday')))
		# Передаём в качестве аргумента строку (tomorrow - завтра)
		self.assertEqual(self.my_first_prod_cal.is_work_day('tomorrow'),
		                 self.my_first_prod_cal.is_work_day(get_date_today('tomorrow')))

	def test_count_work_days(self):
		# Проверяем количество рабочих дней в различных месяцах
		self.assertEqual(self.my_first_prod_cal.count_work_days([2016, 4, 1], [2016, 4, 30]), 21)
		self.assertEqual(self.my_first_prod_cal.count_work_days([2016, 5, 1], [2016, 5, 31]), 19)
		self.assertEqual(self.my_first_prod_cal.count_work_days([2016, 6, 1], [2016, 6, 30]), 21)
		# Передаём сразу в формате даты и времени
		self.assertEqual(self.my_first_prod_cal.count_work_days(date(2016, 4, 1), date(2016, 4, 30)), 21)
		self.assertEqual(self.my_first_prod_cal.count_work_days(date(2016, 5, 1), date(2016, 5, 31)), 19)
		self.assertEqual(self.my_first_prod_cal.count_work_days(date(2016, 6, 1), date(2016, 6, 30)), 21)
		# Передаём дату начала ввиде текста (today, yesterday, tomorrow)
		self.assertEqual(self.my_first_prod_cal.count_work_days('today', date(2016, 4, 30)),
		                 self.my_first_prod_cal.count_work_days(get_date_today('today'), date(2016, 4, 30)))
		self.assertEqual(self.my_first_prod_cal.count_work_days('yesterday', date(2016, 4, 30)),
		                 self.my_first_prod_cal.count_work_days(get_date_today('yesterday'), date(2016, 4, 30)))
		self.assertEqual(self.my_first_prod_cal.count_work_days('tomorrow', date(2016, 4, 30)),
		                 self.my_first_prod_cal.count_work_days(get_date_today('tomorrow'), date(2016, 4, 30)))
		# Передаём в качестве конечной даты количество дней от даты начала (включительно)
		self.assertEqual(self.my_first_prod_cal.count_work_days([2016, 4, 1], 30), 21)
		self.assertEqual(self.my_first_prod_cal.count_work_days('today', 30),
		                 self.my_first_prod_cal.count_work_days(get_date_today('today'), 30))

	def test_count_holidays(self):
		# Проверяем количество выходных дней в различных месяцах
		self.assertEqual(self.my_first_prod_cal.count_holidays([2016, 4, 1], [2016, 4, 30]), 9)
		self.assertEqual(self.my_first_prod_cal.count_holidays([2016, 5, 1], [2016, 5, 31]), 12)
		self.assertEqual(self.my_first_prod_cal.count_holidays([2016, 6, 1], [2016, 6, 30]), 9)
		# Передаём сразу в формате даты и времени
		self.assertEqual(self.my_first_prod_cal.count_holidays(date(2016, 4, 1), date(2016, 4, 30)), 9)
		self.assertEqual(self.my_first_prod_cal.count_holidays(date(2016, 5, 1), date(2016, 5, 31)), 12)
		self.assertEqual(self.my_first_prod_cal.count_holidays(date(2016, 6, 1), date(2016, 6, 30)), 9)
		# Передаём дату начала ввиде текста (today, yesterday, tomorrow)
		self.assertEqual(self.my_first_prod_cal.count_holidays('today', date(2016, 4, 30)),
		                 self.my_first_prod_cal.count_holidays(get_date_today('today'), date(2016, 4, 30)))
		self.assertEqual(self.my_first_prod_cal.count_holidays('yesterday', date(2016, 4, 30)),
		                 self.my_first_prod_cal.count_holidays(get_date_today('yesterday'), date(2016, 4, 30)))
		self.assertEqual(self.my_first_prod_cal.count_holidays('tomorrow', date(2016, 4, 30)),
		                 self.my_first_prod_cal.count_holidays(get_date_today('tomorrow'), date(2016, 4, 30)))
		# Передаём в качестве конечной даты количество дней от даты начала (включительно)
		self.assertEqual(self.my_first_prod_cal.count_holidays([2016, 4, 1], 30), 9)
		self.assertEqual(self.my_first_prod_cal.count_holidays('today', 30),
		                 self.my_first_prod_cal.count_holidays(get_date_today('today'), 30))

	def test_get_date_by_work_days(self):
		# Рассчитываем конечную дату по рабочим дням
		self.assertEqual(self.my_first_prod_cal.get_date_by_work_days([2016, 4, 1], 21), date(2016, 4, 29))
		self.assertEqual(self.my_first_prod_cal.get_date_by_work_days('today', 21),
		                 self.my_first_prod_cal.get_date_by_work_days(get_date_today('today'), 21))


if __name__ == '__main__':
	unittest.main()
