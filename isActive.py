#!/usr/bin/python3

import signal, sys, requests, urllib3, time
from colorama import init, Fore

init(autoreset=True) # Reset colors

if len(sys.argv) != 2:
	print(f"Usage: python3 {sys.argv[0]} <email>")
	sys.exit(1)

info_url = "https://es.infobyip.com/verifyemailaccount.php"
email = sys.argv[1]
# burp = {"https" : "http://127.0.0.1:8080"}
# Colors
lgred, lgyll, green, lgcyn = Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.GREEN, Fore.LIGHTCYAN_EX

def def_handler(sig, frame):
	print("\n\n[*] Exiting...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def makeRequest(email):
	urllib3.disable_warnings()
	headers = {
		"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
		"Origin" : "https://es.infobyip.com",
		"Referer": "https://es.infobyip.com/verifyemailaccount.php"
	}
	post_data = {
			"email" : email,
			"_p1" : "2240"
		}
	print(lgyll + "[" + green + "*" + lgyll + "]" + lgcyn + " Searching...", end="\r")
	time.sleep(1)
	r = requests.post(info_url, data=post_data, headers=headers, verify=False)
	if "Existe la cuenta de correo electrónico" in r.text:
		print(lgyll + "[" + green + "*" + lgyll + "]" + green + " Valid Email!")
		sys.exit()

	print(lgyll + "[" + lgred + "!" + lgyll + "]" + lgred + " No email Found!")

if __name__ == '__main__':
	makeRequest(email)