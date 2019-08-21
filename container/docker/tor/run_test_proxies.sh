#!/bin/sh

echo "set tor config..."
sed -i "s/#ControlPort 9051/ControlPort 9051/g" /etc/tor/torrc

echo "Starting Tor ..."
service tor start

echo "Starting Flask"
python test.py