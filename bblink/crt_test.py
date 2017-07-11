# $language = "Python"
# $interface = "1.0"


def get_lag(ip_addr):
    crt.Screen.Send('\r')
    # crt.Sleep(50)
    lagComm = 'ping ' + ip_addr + \
        ' -c 5 | grep \'min/avg/max/mdev\'|awk -F \"\/\" \'{print $5}\''
    # comm(lagComm)
    crt.Screen.Send(lagComm+'\r')
    crt.Sleep(50)
    crt.Screen.WaitForString(']#', 10)
    crt.Sleep(50)
    r = crt.Screen.CurrentRow
    lag = str.strip(crt.Screen.Get(r-1, 1, r-1, 20).encode())
    comm('#'+lag)
    return int(float(lag))


def comm(command, waitS=[']#'], waitT=10, sleepT=100):
    crt.Screen.Send(command+'\r')
    crt.Screen.WaitForStrings(waitS, waitT)
    crt.Sleep(sleepT)


def login_hc(ip_addr):
    lag = get_lag(ip_addr)
    keyTime = 2*lag
    waitTime = 10*lag
    loginComm = 'ssh root@' + ip_addr + ' -i /mnt/Identity-WF-Linux '
    comm('', sleepT=waitTime)
    comm(loginComm,waitS=["Enter passphrase"])
    for k in 'WF-ieee802.11':
        crt.Screen.Send(k)
        crt.Sleep(keyTime)
    crt.Screen.Send('\r')
    crt.Screen.WaitForStrings([":"], 10)
    crt.Sleep(waitTime)
    for k in 'GW-ieee802.11':
        crt.Screen.Send(k)
        crt.Sleep(keyTime)
    comm('', waitS=[']#'])


errcode = 0
ip_addr = '123.159.197.157'

try:
    crt.Session.Connect(
        "/SSH2 /PASSWORD LErebUFewCkJdShec98x root@120.26.98.211", True)

except ScriptError:
    errcode = crt.GetLastError()

if errcode != 0:
    crt.Dialog.MessageBox("Connection Failed")
else:
    login_hc(ip_addr)
