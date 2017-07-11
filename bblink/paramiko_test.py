#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-07 11:18:40
# @Author  : mx (shibei1988@foxmail.com)
# @Link    : 
# @Version : $Id$

import paramiko
ssh=paramiko.SSHClient()
pkey_path="D:\\Work\\Identity"
key=paramiko.RSAKey.from_private_key_file(pkey_path)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='60.12.33.88',port=22,username='root',key_filename='D:\\Work\\Identity',compress='true',password='WF-ieee802.11')
stdin,stdout,stderr = ssh.exec_command('\r')
# stdin.write("en")
print(stdout.read().decode())
# print(stdin.read().decode())
print(stderr.read().decode())
ssh.close()


