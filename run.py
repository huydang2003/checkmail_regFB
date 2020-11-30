import os
import requests
from bs4 import BeautifulSoup
import json
import re
from random import randint
from check import fb_reg_or_not
from get import creat_email

def start():
	os.system('clear')
	print('\t1.Get mail\n\t2.Check mail')
	check = input(">>>>Chọn: ")
	if check == '1':
		tool = creat_email()
		tool.run()
		print('Đã lấy xong mail!!!')
		yn = input(">>>có muốn check mail luôn không?(y/n): ")
		if yn == 'y': check = '2'
	if check == '2':
		tool = fb_reg_or_not()
		tool.run()

if __name__ == '__main__':
	start()
	