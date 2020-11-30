import requests
from random import randint

class creat_email():
	def __init__(self):
		self.ses = requests.session()
		self.list_ip = []
		self.list_mail_old = []
		self.cout = 1

	def save_email(self, email):
		f = open('list_email.txt', 'a')
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

	# def check_yahoo(self, email):
	# 	url = 'https://mmo69.com/_check_live_email/api.php?email='+email
	# 	res = self.ses.get(url)
	# 	data = res.text
	# 	kq = data.split('|')
	# 	if kq[2] == 'DIE': return True
	# 	else: return False

	def check_mail(self, email):
		url = "https://ssfy.sh/amaurymartiny/reacher@2d2ce35c/check_email"
		payload = {"to_email": email}
		res = self.ses.post(url, json=payload)
		data = res.json()
		if 'is_reachable' in data:
			gt = data['is_reachable']
			if gt == 'invalid': return 1
			else: return 0
		else: return 2

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
		while self.cout <= sl:
			num = randint(1, 999)
			email = f'{name_email}{num}@yahoo.com'
			if email in self.list_mail_old: continue
			print('-')
			self.list_mail_old.append(email)

			check = self.check_mail(email)
			if check == 0: continue
			elif check == 2: self.dk()
			elif check == 1:
				print(f'{self.cout}|{email}')	
				self.cout+=1			
				self.save_email(email)
		
	def run(self):
		open('list_email.txt', 'w').close()
		name_email = input("Name: ")
		sl = int(input('soluong: '))
		print('[START]')
		self.process(name_email, sl)
		print('Success!!!')

if __name__ == '__main__':
	print("TOOL GET MAIL YAHOO")
	tool = creat_email()
	tool.run()