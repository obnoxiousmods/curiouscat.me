import cfscrape
import random
import threading
import sys

class main():
	def __init__(self):
		self.threads = int(sys.argv[2])
		self.session = cfscrape.create_scraper()
		self.asks = 0
		for thread in range(self.threads):
			threading.Thread(target=self.ask).start()

	def ask(self):
		while True:
			try:
				self.getRequest = self.session.get('https://curiouscat.me/%s'%sys.argv[1])
				self.postRequest = self.session.post('https://api.curiouscat.me/post/create', 
					data={
						'username': sys.argv[1],
						'anon': 'on',
						'type': 'ask',
						'post': '%d ur gay lmao %d'%(random.randint(0, 999999999999999), random.randint(0, 999999999999999)),
						'sessionkey': 'null',
					})
				if self.postRequest.json()['success'] == True:
					self.asks += 1
					print('Sent: %d'%(self.asks))
				else:
					print(self.postRequest.json()['success'])
			except:
				continue
if __name__ == "__main__":
	main()
