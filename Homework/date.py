'''
Created on 11/25/2020
@author:   Robert Brandl
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day

    def tomorrow(self):
        '''increases the calendar date by 1'''
        days = 28 + self.isLeapYear()
        DAYS_IN_MONTH = (0,31,days,31,30,31,30,31,31,30,31,30,31)
        if self.day == DAYS_IN_MONTH[self.month]:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.day = 1
                self.month += 1
        else: self.day = self.day + 1

    def yesterday(self):
        '''decreases the calendar date by 1'''
        days = 28 + self.isLeapYear()
        DAYS_IN_MONTH = (0,31,days,31,30,31,30,31,31,30,31,30,31)
        if self.day == 1:
            if self.month == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            else:
                self.month -=1
                self.day = DAYS_IN_MONTH[self.month] 
        else: self.day = self.day - 1

    def addNDays(self, N):
        '''adds N days to the calendar date'''
        print(self)
        for x in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        '''subtracts N days to the calendar date'''
        print(self)
        for x in range(N):
            self.yesterday()
            print(self)

    def isBefore(self,d2):
        '''checks if the date of self is before d2'''
        if self.year < d2.year:return True
        elif self.year == d2.year:
            if self.month < d2.month: return True
            elif self.month == d2.month:
                if self.day < d2.day: return True
        return False

    def isAfter(self,d2):
        '''checks if the date of self is after d2'''
        if self.year > d2.year:return True
        elif self.year == d2.year:
            if self.month > d2.month: return True
            elif self.month == d2.month:
                if self.day > d2.day: return True
        return False

    def diff(self,d2):
        '''returns the number of days between self and d2'''
        d1 = self.copy()
        d2 = d2.copy()
        count = 0
        while d1.isBefore(d2):
            count += -1
            d1.tomorrow()
        while d1.isAfter(d2):
            count += 1
            d1.yesterday()
        return count

    def dow(self):
        '''returns the day of the week of the object'''
        d = Date(12, 7, 1941)
        DaysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
        return DaysOfWeek[self.diff(d)%7] 
