#!/usr/bin/python

import pexpect
import sys
import pwn

hosts = sys.argv[1]

def anonymous_login(host,port=21):
    ftp = pexpect.spawn("ftp "+host)
    ftp.expect_exact("Name")
    ftp.sendline("anonymous")
    ftp.expect_exact("Password")
    ftp.sendline("anonymous")
    ftp.expect_exact("ftp>")
    if "Login authentication failed" not in ftp.before:
        pwn.log.success(host.rstrip("\r\n") + " is Vulnerable to Anonymous Login")
    else:
       pwn.log.failure(host.rstrip("\r\n") + " is NOT Vulnerable")

subdomains = open(hosts,"r")

for host in subdomains:
    anonymous_login(host,21)

    


