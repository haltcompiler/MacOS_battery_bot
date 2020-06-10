import subprocess
import time
import requests
from pync import Notifier

def run_zombie():
	subprocess.Popen(['caffeinate','-s'])
 
def get_out(c):
	command = c
	p = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	output = p.stdout.read().decode('ASCII').split(';')[0]
	return output

command = "pmset -g batt | grep present | awk {'print $3'}"
run_zombie()
while True:
	
	print(get_out(command))
	url="https://api.telegram.org/[botid]:[bot_secret]/sendmessage?chat_id=[chat_id]&text="
	url+=get_out(command)
	requests.get(url)
	time.sleep(1)
	if get_out(command)=='100%':
		Notifier.notify('Battery is Fully Chargred!', title='Battery')
		exit()


