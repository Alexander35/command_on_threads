from threading import Thread
import argparse
import subprocess

def run_subprocess(command, args):
	try:
		splitted_args = args.split(',')
		sp = subprocess.Popen([command, splitted_args], stdout=subprocess.PIPE)
		output, err = sp.communicate()
		# print('{}'.format(output.decode('cp866')))
		print(output)
	except Exception as exc:
		print('cant run a subprocess with args {} : {}'.format(arguments, exc))	

def loop(command, list_of_parameters):

	for parameter in list_of_parameters:
		Thread(target=run_subprocess, args=(command, parameter,)).start()

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--command", dest="command", help="a command to execute")
	parser.add_argument("-l", "--list_of_parameters", action="append", dest="list_of_parameters", help="list of parameters (for loop)", default=[])
	
	args = parser.parse_args()
	
	try:
		loop(args.command, args.list_of_parameters)
	except Exception as exc:
		print('cant run main loop with params {} {}, beacuse of {}'.format(args.command, args.list_of_parameters, exc))	

if __name__ == '__main__':
	main()