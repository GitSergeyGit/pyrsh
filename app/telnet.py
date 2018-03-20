import telnetlib
import time
from contextlib import contextmanager

from args import Arguments
from shell import Shell

class ClTelnet(Arguments, Shell):
    def __init__(self, args, password):
        Arguments.__init__(self, args, password)

    @contextmanager
    def tn_connect(self):
        tn = telnetlib.Telnet(self.host, self.port)
        tn.read_until("login: ")
        tn.write(self.user + "\r\n")
        tn.read_until("password: ")
        tn.write(self.password + "\r\n")
        yield tn
        tn.close()

    def run(self):
        with self.tn_connect() as connect:          
            tn.write(self.cmd + "\r\n")
            time.sleep(1)
            return tn.read_all()
