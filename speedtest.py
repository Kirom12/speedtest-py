import os
import sys
import getopt
import time
import subprocess
import time
import signal
import matplotlib.pyplot as plt

log_folder = "log"
pid_file = "run.pid"

# Default values
speedtest_interval = 60 # in minutes
speedtest_duration = 60*24 # in minutes

exec_in_background = False

def usage():
	print("Speedtest-py")
	print("")
	print("Arguments: ")
	print("")
	print("Examples: ")

def remove_pid_file():
	if os.path.isfile(pid_file):
		os.remove(pid_file)
	else:
		print('[WARNING]PID file doesn\'t exist, try to stop the process manualy')

def speed_test():

	timer = 0

	current_time = time.strftime("%d/%m/%Y %H:%M:%S")
	log_file = log_folder+"/"+str(time.strftime("%d-%m-%Y_%H-%M-%S"))+".log"

	if not os.path.isdir(log_folder):
		try:
			os.mkdir(log_folder)
		except:
			print("can't create log folder")
			sys.exit(0)

	subprocess.run("echo 'Scan "+str(current_time)+"' > "+log_file, shell=True)

	while True:

		output = subprocess.run(["speedtest-cli", "--simple"], stdout=subprocess.PIPE)

		subprocess.run("echo '["+time.strftime("%d/%m/%Y %H:%M:%S")+"]' >> " +log_file, shell=True)
		subprocess.run("echo '"+output.stdout.decode("utf-8")+"' >> " +log_file, shell=True)

		timer += speedtest_interval

		if timer > speedtest_duration:
			break;
		
		time.sleep(speedtest_interval)

	remove_pid_file()


def launch_background():
	# Check if process is running
	if os.path.isfile(pid_file):
		print('PID file exist ! A process is running. If the process is not running, delete run.pid')
		sys.exit(0)

	proc = subprocess.Popen("nohup python3 speedtest.py -i " +str(speedtest_interval)+ " -d "+str(speedtest_duration)+ " -b &>/dev/null &", shell=True)

	subprocess.run("echo "+str(proc.pid+2)+" > "+pid_file+"", shell=True)
	# proc.id+2 ??? why?

def kill_process():

	try:
		file = open(pid_file, 'r')
		pid = file.read()
		file.close()
		remove_pid_file()
		os.kill(int(pid), signal.SIGKILL)
	except:
		print('Nothing to kill !')

def main():

	global speedtest_duration
	global speedtest_interval
	global exec_in_background

	try:
		opts, args = getopt.getopt(sys.argv[1:], "i:d:b", ["kill"])
	except getopt.GetoptError as err:
		print(str(err))
		sys.exit(0)

	for o, a in opts:
		if o == '-i':
			speedtest_interval = int(a)
		elif o == '-d':
			speedtest_duration = int(a)
		elif o == '-b':
			exec_in_background = True
		elif o == '--kill':
			kill_process()
			return

	if not exec_in_background:
		launch_background()
	else:
		speed_test()

main()