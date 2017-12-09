import subprocess

class conlinux:
	def __init__(self, args):
		self.host = args.host
		self.user = args.user
		self.cmd = args.cmd

	def run(self):
		per = str(self.user+'@'+self.host)
		ssh = subprocess.Popen(['ssh', per, self.cmd],
								shell=False,
								stdout=subprocess.PIPE,
								stderr=subprocess.PIPE)
		result = ssh.stdout.readlines()
		if result == []:
			# error
			return ssh.stderr.readlines()
		else:
			return result