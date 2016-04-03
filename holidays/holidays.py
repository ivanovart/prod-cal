#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calendar import weekday
from service import check_locale, get_prodcals, cast, cast_single_date
from config import DEFAULT_LOCALE
from datetime import timedelta
from calendar import Calendar

class ProdCal(Calendar):
    def __init__(self, **kwargs):
        Calendar.__init__(self)
        self.locale = check_locale(kwargs['locale']) if 'locale' in kwargs else DEFAULT_LOCALE
        self.non_work_days, self.work_days = get_prodcals(self.locale)

    def is_work_day(self, *args):
        """Проверяем рабочий ли сегодня день"""
        args = cast_single_date(args)
        if self.work_days.is_value(args):
            return True
        if self.non_work_days.is_value(args) or weekday(args.year, args.month, args.day) in [5, 6]:
            return False
        return True

    def count_work_days(self, start_date, end_date):
        """Подсчёт количества рабочих дней в интервале"""
        start_date, end_date = cast(start_date, end_date)
        tm_delta = end_date - start_date
        work_days = 0
        for day in range(tm_delta.days+1):
            curr_date = start_date+timedelta(days=day)
            work_days += 1 if self.is_work_day(curr_date) else 0
        return work_days

    def count_holidays(self, start_date, end_date):
        """Подсчёт количества выходных дней в интервале"""
        tm_delta = 0
        if isinstance(end_date, int):
            tm_delta = end_date
        start_date, end_date = cast(start_date, end_date)

        if not tm_delta:
            tm_delta = (end_date - start_date).days + 1

        holidays = 0
        for day in range(tm_delta):
            curr_date = start_date+timedelta(days=day)
            holidays += 1 if not self.is_work_day(curr_date) else 0
        return holidays

    def get_date_by_work_days(self, start_date, work_days):
        """Вычисляем конечную дату по количеству рабочих дней"""
        start_date = cast_single_date(start_date)
        days_counter = 0
        work_days_counter = 0
        curr_date = ''
        while work_days_counter != work_days:
            curr_date = start_date + timedelta(days=days_counter)
            if self.is_work_day(curr_date):
                work_days_counter += 1
            days_counter += 1
        return curr_date
