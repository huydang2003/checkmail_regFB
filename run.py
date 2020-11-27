import os
import requests
import json
import re
from bs4 import BeautifulSoup
from random import randint

class check_mail():
	def __init__(self):
		self.ses = requests.session()
		self.list_ip = []
		self.list_mail_valid = []
		self.cout = 0

	def save_email(self, email):
		f = open('success.txt', 'a')
		f.write(email+'\n')
		f.close()

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
		payload = {'lsd': '','jazoest': '','email': None,'did_submit': 'Tìm kiếm'}
		soup = BeautifulSoup(res.content, 'html.parser')
		form = soup.find(id='identify_yourself_flow')
		list_in = form.find_all('input')
		for x in list_in:
			if x.get('name') == 'lsd': payload['lsd'] = x.get('value')
			if x.get('name') == 'jazoest': payload['jazoest'] = x.get('value')
		return payload

	def check_mail(self, email):
		url = "https://ssfy.sh/amaurymartiny/reacher@2d2ce35c/check_email"
		payload = {"to_email": email}
		res = self.ses.post(url, json=payload)
		data = res.json()
		# print(data)
		if 'is_reachable' in data:
			gt = data['is_reachable']
			if gt == 'invalid': return 1
			else: return 0
		else: return 2

	def check_live(self, payload, email):
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
			ip = self.check_ip()
			if ip == '': print('ip đểu rồi!!!')
			else:
				if ip not in self.list_ip:
					self.list_ip.append(ip)
					print(ip)
					break
				else: 
					print('\nip chưa thay đổi!!!')
			input('Change ip!!!(Enter)')

	def process(self, name_email, sl):
		self.dk()
		payload = self.get_payload()
		while self.cout < sl:
			num = randint(1, 999)
			email = f'{name_email}{num}@yahoo.com'
			check = self.check_mail(email)
			if check == 0: continue
			elif check == 2:
				self.dk()
				# payload = self.get_payload()
			elif check == 1:
				print(f'{self.cout}|{email}', end=' +> ')
				try:
					check = self.check_live(payload, email)
					if check == True:
						if email not in self.list_mail_valid:
							print('(>.<)(>.<)(>.<)')
							self.cout+=1
							self.list_mail_valid.append(email)
							self.save_email(email)
					else:
						print(':(:(:(')
				except:
					self.dk()

	def run(self):
		open('success.txt', 'w').close()
		name_email = input("Name: ")
		sl = int(input("Soluong: "))
		print('[START]')
		self.process(name_email, sl)
		print('Success!!!')
			

if __name__ == '__main__':
	print("\n[TOOL GET & CHECK MAIL YAHOO]")
	tool = check_mail()
	tool.run()

