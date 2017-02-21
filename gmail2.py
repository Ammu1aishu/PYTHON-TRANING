import pexpect
m_p = pexpect.spawn(python gmail_prg.py)
m_p.pexpect('gmail')
m_p.sendline(' ')
