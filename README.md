REMOTE SYSTEM AGENT

A Python-based client-server system monitoring tool.

FEATURES

~Monitor CPU, RAM, and disk usage
~Health checks with threshold detection
~System information endpoint 
~Top processes viewer
~HTTP API architecture
~Client dashboard with formatted tables

ENDPOINTS

/
/status
/health
/info
/processes

REQUIREMENTS

~Python 3
~psutil
~requests
~tabulate

INSTALLATION

git clone <repository-url>
cd remote-system-agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

USAGE

Start the server:
python server.py

In another terminal:
python client.py

FUTURE IMPORVEMENTS

~Authentication
~Logging
~Remote multi-host monitoring
~Web dashboard
~Encryption
~Alerts and Notification

AUTHOR 

ninjanu315
