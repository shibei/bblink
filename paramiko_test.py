#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-07 11:18:40
# @Author  : mx (shibei1988@foxmail.com)
# @Link    : 
# @Version : $Id$

import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='112.65.205.74',port=22,username='admin',password='P@ssw0rd123')
stdin,stdout,stderr = ssh.exec_command('enable')
print(stdout.read().decode())
ssh.close()


