#!/bin/sh
iptables -t nat -D PREROUTING -p tcp -j SHADOWSOCKS
iptables -t mangle -D PREROUTING -j SHADOWSOCKS
iptables -t nat -F SHADOWSOCKS
iptables -t nat -X SHADOWSOCKS
iptables -t mangle -F SHADOWSOCKS
iptables -t mangle -X SHADOWSOCKS