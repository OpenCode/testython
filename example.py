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

import sys
sys.path.append('.')
import testython as testython

if __name__ == '__main__':

	clog = testython.log()
	# ----- If you want you can set log path, too!
	#clog.set_path('/home/USER/FOLDER')
	clog.set_name('try_log')

	clog.print_line('Welcome to Testython! This is a simple log line!')
	clog.print_line('Use it for your debug on python code!')
	clog.print_line('For the script, use the file log line. It\'s better!!!')

	clog.append('Start sample test!')

	# ---------
	# TIME TEST
	# ---------

	clog.append('Start TIME test!')

	tt = testython.test_time()
	tt.set_start_time()
	inc_var = 0
	for x in range(10000000):
		inc_var += 1
	tt.set_end_time()
	print inc_var
	print 'Extended:', tt.elapsed_time(True)
	print 'Seconds:', tt.elapsed_time()

	# --------
	# MEM TEST
	# --------

	clog.append('Start MEMORY test!')

	tm = testython.test_memory()
	print tm.get_object_size(inc_var, tm.DIM_BIT), 'bit'
	print tm.get_object_size(inc_var), 'bytes'
	print tm.get_object_size(inc_var, tm.DIM_KILO_BYTE), 'KB'
	print tm.get_object_size(inc_var, tm.DIM_MEGA_BYTE), 'MB'
	print tm.get_object_size(inc_var, tm.DIM_GIGA_BYTE), 'GB'

	a = 10; b = 30; c = 20
	print 'Biggest variable:', tm.biggest_var([a, b, c,])
	print 'Biggest variable:', tm.biggest_var([100, 400, 350,])

	clog.append('Stop sample test!')
