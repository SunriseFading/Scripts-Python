import subprocess as sb
sb.call("ifconfig eth0 down", shell=True)
sb.call("ifconfig eth0 hw ether 08:00:27:50:4c:14", shell=True)
sb.call("ifconfig eth0 up", shell=True)