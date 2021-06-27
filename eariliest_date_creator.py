from calendar import monthrange
import datetime


class EarliestDateCreator:
    def __init__(self, string):
        self.numbers = string
        self.min = 0
        self.mid = 0
        self.max = 0

    def convert_str_to_list(self):
        self.numbers = self.numbers.split('/')

    def change_strings_to_numbers(self):
        self.numbers = [int(number) for number in self.numbers]
        return self.numbers

    def sort_numbers(self):
        self.numbers.sort()

    def set_min_max_and_mid(self):
        self.min = self.numbers[0]
        self.mid = self.numbers[1]
        self.max = self.numbers[2]

    def numbers_are_correct(self):
        if self.min_number_is_correct() and \
                self.mid_number_is_correct() and \
                self.max_number_is_correct():

            return True

        else:
            return False

    def min_number_is_correct(self):
        if 0 < self.min <= 12 or (self.min == 0 and self.max <= 31):
            return True
        else:
            return False

    def mid_number_is_correct(self):
        if 1 <= self.mid <= 31:
            return True
        else:
            return False

    def max_number_is_correct(self):
        if 2 <= self.max <= 999 or \
                2000 < self.max <= 2999 or \
                (self.max == 2000 and self.min != 0):
            return True
        else:
            return False

    def set_date(self):
        if self.numbers_are_correct():

            if not self.max_greater_than_num_of_days_in_month(num_of_days=28):

                if not self.mid_greater_than_num_of_months():

                    return self.format_date(year=self.min, month=self.mid, day=self.max)

                else:

                    return self.format_date(year=self.mid, month=self.min, day=self.max)

            if self.max_greater_than_num_of_days_in_month(num_of_days=28):

                possible_year = self.mid + 2000 if self.mid < 2000 else self.mid

                num_days_in_month = monthrange(year=possible_year, month=self.min)[1]

                if not self.max_greater_than_num_of_days_in_month(num_days_in_month):
                    if not self.mid_greater_than_num_of_months():

                        return self.format_date(year=self.min, month=self.mid, day=self.max)

                    else:

                        return self.format_date(year=self.mid, month=self.min, day=self.max)

                if self.max_greater_than_num_of_days_in_month(num_days_in_month):

                    if self.mid_less_than_num_of_days_in_month(num_days_in_month) or \
                            (self.min == 2 and self.mid == 29 and self.year_is_leap_year(self.max)):
                        return self.format_date(year=self.max, month=self.min, day=self.mid)

        return 'is illegal'

    def max_greater_than_num_of_days_in_month(self, num_of_days):
        if self.max > num_of_days:
            return True
        else:
            return False

    def mid_greater_than_num_of_months(self):
        if self.mid > 12:
            return True
        else:
            return False

    def mid_less_than_num_of_days_in_month(self, num_of_days):
        if self.mid <= num_of_days:
            return True
        else:
            return False

    def year_is_leap_year(self, year):
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            return True
        else:
            return False

    def format_date(self, year, month, day):
        year = year + 2000 if year < 2000 else year
        date = datetime.date(year, month, day)

        return date

    def get_earliest_date(self):
        self.convert_str_to_list()
        self.change_strings_to_numbers()
        self.sort_numbers()
        self.set_min_max_and_mid()
        return self.set_date()
