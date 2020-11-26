import os
import requests
from bs4 import BeautifulSoup
import random
import json
import re

class Fb_reg_or_not():
	if not os.path.exists('list_email.txt'): open('list_email.txt', 'w').close()
	def __init__(self):
		self.ses = requests.session()
		self.list_ip = []

	def check_ip(self):
		try:
			res = requests.get('https://httpbin.org/ip', timeout=10)
			data = res.json()
			check = data["origin"]
			return check
		except:
			return ''

	def get_payload(self):
		url = 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1'
		res = self.ses.get(url)
		payload = {'lsd': '','jazoest': '','email': '','did_submit': 'Tìm kiếm'}
		soup = BeautifulSoup(res.content, 'html.parser')
		form = soup.find(id='identify_yourself_flow')
		list_in = form.find_all('input')
		for x in list_in:
			if x.get('name') == 'lsd': payload['lsd'] = x.get('value')
			if x.get('name') == 'jazoest': payload['jazoest'] = x.get('value')
		return payload

	def check_email(self, payload, email):
		url = 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1'
		payload['email'] = email
		res = self.ses.post(url, data=payload, timeout=15)
		data = res.text
		fill = re.findall('identify_yourself_flow', data)
		if len(fill)==0: return True
		else: return False

	def dk(self):
		while True:
			print('\nChecking ip...')
			temp = self.check_ip()
			if temp == '': print('ip đểu rồi!!!')
			else:
				if temp not in self.list_ip:
					self.list_ip.append(temp)
					print(temp)
					break
				else: print('\nip chưa thay đổi!!!')
			input('Change ip!!!(Enter)')

	def save_email(self, email):
		f = open('success.txt', 'a')
		f.write(email+'\n')
		f.close()

	def run(self):
		data = open('list_email.txt', 'r').read()
		list_email = data.split('\n')
		list_mail_valid = []
		cout = 0
		for email in list_email:
			if cout % 80 == 0:
				self.dk()
				payload = self.get_payload()
			cout+=1
			print(f'{cout}|{email}|', end='')
			try:
				check = self.check_email(payload, email)
				if check == True:
					print('(>.<)(>.<)(>.<)')
					if email not in list_mail_valid:
						list_mail_valid.append(email)
						self.save_email(email)
				else:
					print(':(:(:(')
			except:
				self.dk()
		print('Success!!!')

if __name__ == '__main__':
	tool = Fb_reg_or_not()
	tool.run()