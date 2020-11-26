import requests
import random

class creat_email():
	def __init__(self):
		self.ses = requests.session()

	def save_email(self, email):
		f = open('list_email.txt', 'a')
		f.write(email+'\n')
		f.close()

	def check_yahoo(self, email):
		url = 'https://mmo69.com/_check_live_email/api.php?email='+email
		res = self.ses.get(url)
		data = res.text
		kq = data.split('|')
		if kq[2] == 'DIE': return True
		else: return False

	def get_list_email(self, name_email, sl):
		open('list_email.txt', 'w').close()
		cout = 0
		while cout <= sl:
			num = random.randint(1, 999)
			email = f'{name_email}{num}@yahoo.com'
			check = self.check_yahoo(email)
			if check==True:
				cout+=1
				self.save_email(email)
				print(f"{cout}|{email}")
		
	def run(self):
		name_email = input("Name: ")
		sl = int(input('soluong: '))
		print('[START]')
		self.get_list_email(name_email, sl)
		print('Success!!!')

if __name__ == '__main__':
	print("TOOL GET MAIL YAHOO")
	tool = creat_email()
	tool.run()