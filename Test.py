from netmiko import ConnectHandler

import getpass

mge3_co_wlc1 = {
    'device_type': 'cisco_xe',
    'ip': '10.71.17.48',
    'username': 'username',
    'password': 'password'
}
mge3_co_wlc1['username']=input("Username: ")
mge3_co_wlc1['password']=getpass.getpass()

net_connect = ConnectHandler(**mge3_co_wlc1)
show_commands3 = ['show ap sum | i Number']
output = ''
for cmd3 in show_commands3:
    output += net_connect.send_command(cmd3, delay_factor=2)

print (output)

mge3_co_wlc_2 = {
    'device_type': 'cisco_xe',
    'ip': '10.71.17.49',
    'username': 'username',
    'password': 'password'
}
mge3_co_wlc_2['username']=input("Username: ")
mge3_co_wlc_2['password']=getpass.getpass()
show_commands2 = ['show ap sum']
net_connect = ConnectHandler(**mge3_co_wlc_2)
output = ''
for cmd2 in show_commands2:
    output += net_connect.send_command(cmd2, delay_factor=2)

print (output)

mge3_co_agg_r1 = {
    'device_type': 'cisco_xe',
    'ip': '10.71.16.35',
    'username': 'username',
    'password': 'password'
}
mge3_co_agg_r1['username']=input("Username: ")
mge3_co_agg_r1['password']=getpass.getpass()

net_connect = ConnectHandler(**mge3_co_agg_r1)
show_commands = ['show processes cpu history', 'show processes cpu | i Core 0|Core 1', 'sh processes memory sorted', 'sh process cpu sort 5sec | ex 0.00 +0.00 +0.00', 'show int | i line|packets/sec', 'show int status | exclude disabled|notconnect', 'show etherchannel summary', 'show cdp neighbors', 'show standby brief', 'show ip ospf neighbor', 'show ip bgp all summary', 'show int status | include err', 'sh int desc | i acc-sw', 'sh int desc | i dis-sw']
output = ''
for cmd in show_commands:
    output += net_connect.send_command(cmd, delay_factor=2)

print (output)

mge3_co_agg_r2 = {
    'device_type': 'cisco_xe',
    'ip': '10.71.16.36',
    'username': 'username',
    'password': 'password'
}
mge3_co_agg_r2['username']=input("Username: ")
mge3_co_agg_r2['password']=getpass.getpass()

net_connect = ConnectHandler(**mge3_co_agg_r2)
show_commands1 = ['show processes cpu history', 'show processes cpu | i Core 0|Core 1', 'sh processes memory sorted', 'sh process cpu sort 5sec | ex 0.00 +0.00 +0.00', 'show int | i line|packets/sec', 'show int status | exclude disabled|notconnect', 'show etherchannel summary', 'show cdp neighbors', 'show standby brief', 'show ip ospf neighbor', 'show ip bgp all summary', 'show int status | include err', 'sh int desc | i acc-sw', 'sh int desc | i dis-sw']
output = ''
for cmd1 in show_commands1:
    output += net_connect.send_command(cmd1, delay_factor=2)

print (output)
