# IPRelay

This script is designed to power cycle a device, like a modem upon a failed network connection. Ethernet is the preferred interface, but you could use a Raspberry Pi Zero W over wifi with a smaller relay and with minimal code changes. 

1. Manually run the script with _python3 iprelay.py_ and enter the targets IPv4 address, or the gateway IP if you want to trigger the relay for the modem.

2. The script will do a test ping to see if the IP is responsive.

3. You can manually change the json IP value or you can remove the “target.json” file and rerun the script to enter a new IP.

4. To edit the address, relay, and delay of the relay board, you will need open the script and edit the variables listed at the top. You can also change the json file name if you wish.

	* see https://pi-plates.com/relayplate2-users-guide/ for further details of the relay board

5. For the script to execute automatically you will need to create a cron job. You can copy paste the command into the terminal. Jsut make sure to replace the home path with your username. pi for defualt 

_{ crontab -l; echo "15 * * * * cd /home/pi/IPRelay && /usr/bin/python iprelay.py > tmp/iprelay.log 2>&1"; } | crontab -_ 

The “15” will cause it to run every 15 minutes, every hour, of every day. You can check and make changes to the timing by entering crontab -e in the terminal

The cron job stores a log the tmp/iprelay.log 
