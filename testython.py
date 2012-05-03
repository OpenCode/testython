#!/usr/bin/python
# -*- encoding: utf-8 -*-

#####################################################################################
#
#    Realizzata da Francesco OpenCode Apruzzese
#    Copyright (C) 2012 Francesco Apruzzese. All Rights Reserved. Under GPL 3 Licence
#    Email: cescoap@gmail.com
#    Web site: http://www.e-ware.org
#
#####################################################################################

from datetime import datetime
from sys import getsizeof

# ------------------
# GENERIC UTILITY
# ------------------

def print_log_line(message):
	print  '[%s] %s' % (datetime.today(), message)


# ------------------
# TEST TIME
# ------------------

class test_time():

	start_time = False
	end_time = False

	def set_start_time(self):
		"""Set start time to count elapsed time"""
		self.start_time = datetime.today()
		return self.start_time

	def get_start_time(self):
		"""Get start time to count elapsed time"""
		return self.start_time

	def set_end_time(self):
		"""Set end time to count elapsed time"""
		self.end_time = datetime.today()
		return self.end_time

	def get_end_time(self):
		"""Get end time to count elapsed time"""
		return self.end_time

	def elapsed_time(self, extended=False):
		"""Return elapsed time from start time to end time"""
		if self.start_time and self.end_time:
			if extended:
				return self.get_end_time() - self.get_start_time()
			return (self.get_end_time() - self.get_start_time()).seconds


# ------------------
# TEST TIME
# ------------------

class test_memory():

	DIM_GIGA_BYTE = 'G'
	DIM_MEGA_BYTE = 'M'
	DIM_KILO_BYTE = 'K'
	DIM_BYTE = 'B'
	DIM_BIT = 'b'

	def get_object_size(self, object, dimension_type=DIM_BYTE):
		"""Return size of an object"""
		if dimension_type == self.DIM_BYTE:
			return getsizeof(object)
		elif dimension_type == self.DIM_BIT:
			return getsizeof(object) * 8
		elif dimension_type == self.DIM_KILO_BYTE:
			size = getsizeof(object)
			if size:
				size = size / 1024.00
			return size
		elif dimension_type == self.DIM_MEGA_BYTE:
			size = getsizeof(object)
			if size:
				size = size / 1048576.00
			return size
		elif dimension_type == self.DIM_GIGA_BYTE:
			size = getsizeof(object)
			if size:
				size = size / 1073741824.00
			return size

	def biggest_var(self, variables_list):
		"""Return a tupla with name (if exist) and value of biggest (size measure) variable in a list"""
		actual_biggest_var = 0
		for var in variables_list:
			if self.get_object_size(var) > actual_biggest_var:
				actual_biggest_var = var
		variables_list = globals()
		for val in variables_list:
			if variables_list[val] == actual_biggest_var:
				return (val, variables_list[val])
		return (False, actual_biggest_var)
