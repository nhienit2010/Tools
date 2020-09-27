import requests, getopt, sys

def Usage():
	print("Usage:")
	print("\tpython3 sub_scan.py -h <host>")
	print("Options:")
	print("\t--help: For help")
	return

with open('subdomains-top1million-110000.txt', 'r') as f:
	wordlists = [x.strip() for x in f.read().split('\n')]

def scan(host):
	for word in wordlists:
		try:
			url = 'https://'+ word + '.' + host
			r =	requests.get(url)
			if r.status_code >= 200 and r.status_code <= 403:
				print(url)
		except:
			pass
	return

if __name__ == '__main__':
	name = """
          __    _            _ __ 
   ____  / /_  (_)__  ____  (_) /_
  / __ \/ __ \/ / _ \/ __ \/ / __/
 / / / / / / / /  __/ / / / / /_  
/_/ /_/_/ /_/_/\___/_/ /_/_/\__/  
	"""
	print(name)
	try:
		if (len(sys.argv) < 2):
			Usage()
			sys.exit(2)
		
		opts, args = getopt.getopt(sys.argv[1:], "h:", ["help"])

		for opt, arg in opts:
			if opt == "--help":
				Usage()
				sys.exit(2)
			if opt == "-h":
				scan(arg)
	except:
		print("Error")