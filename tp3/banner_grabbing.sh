#! /usr/bin/env bash
#
# $1: host to connect
# $2: port to connect to
#
# This works with webservers who put the whole info in the "Server:" header and
# respond to a "HEAD / HTTP/1.0" request

host=$1
port=$2

if [ "$host"x = "x" -o "$port"x = "x" ]; then
	echo "Usage: $0 <host> <port>"
	exit 1
fi

# Use printf so "\n" is what we except, and don't use unportable "echo -e"
response=$(printf "HEAD / HTTP/1.0\n\n" | nc $host $port)

server=$(echo "$response" | grep "^Server:")

if [ "$server"x = "x" ]; then
	echo "No server info found"
	exit 0
fi

echo "$server"
