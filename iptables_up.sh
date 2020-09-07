#!/bin/sh
iptables -t nat -N SHADOWSOCKS
iptables -t mangle -N SHADOWSOCKS
iptables -t nat -A SHADOWSOCKS -d 13.112.172.114 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 0.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 10.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 127.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 169.254.0.0/16 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 172.16.0.0/12 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 192.168.0.0/16 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 224.0.0.0/4 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 240.0.0.0/4 -j RETURN

#iptables -t nat -A SHADOWSOCKS -d 103.252.115.153/32 -p tcp -j REDIRECT --to-ports 2090
#iptables -t nat -A SHADOWSOCKS -d 108.160.170.45/32 -p tcp -j REDIRECT --to-ports 2090
#iptables -t nat -A SHADOWSOCKS -d 157.240.12.36/32 -p tcp -j REDIRECT --to-ports 2090
#iptables -t nat -A SHADOWSOCKS -d 108.160.169.171/32 -p tcp -j REDIRECT --to-ports 2090
#iptables -t nat -A SHADOWSOCKS -d 108.160.169.171/32 -p tcp -j REDIRECT --to-ports 2090
iptables -t nat -A SHADOWSOCKS -p tcp -j REDIRECT --to-ports 2090


iptables -t nat -A PREROUTING -p tcp -j SHADOWSOCKS
iptables -t mangle -A PREROUTING -j SHADOWSOCKS
