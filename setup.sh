if [ $(id -u) -ne 0 ]; then
	echo "This script must be ran as root!"
	exit 1
fi
pip3 install pynput