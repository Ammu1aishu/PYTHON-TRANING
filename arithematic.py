import pexpect
import sys
m = pexpect.spawn('python add.py')
m.expect("enter the first number:")
m.sendline("30")
m.expect("enter the second number:")
m.sendline("70")
m.expect("enter your operator")
m.sendline(" + ")
m.expect("the value of addition is:")
m.close
