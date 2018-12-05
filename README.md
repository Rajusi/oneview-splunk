# Oneview-Splunk integration
Splunk installation and setup
Create an account in Splunk - https://www.splunk.com/
Download Splunk for enterprise from official website after logging in. 
Link is something like this:- wget -O splunk-7.2.1-be11b2c46e23-Linux-x86_64.tgz 'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=7.2.1&product=splunk&filename=splunk-7.2.1-be11b2c46e23-Linux-x86_64.tgz&wget=true'

Create user and group for Splunk (All as root user if not mentioned otherwise)
$ groupadd splunk
$ useradd -d /opt/splunk -m -g splunk splunk  (/opt/splunk will be the home directory for user splunk added to group splunk)
$ tar -xvzf splunk-7.2.1-be11b2c46e23-Linux-x86_64.tgz
$ cp -rp splunk/* /opt/splunk/  (Copy to splunk user home dir)
$ chown -R splunk: /opt/splunk/ (Change the ownership to splunk user)
$ su - splunk (Change to user - splunk)
$ pwd
$ cd bin
$ ll
$ ./splunk start --accept-license (Start installation by accepting the license) (Enter the splunk administrator username and password - splunk/splunk@123)

<Splunk administrator - splunk>
Create a password for it - passwd splunk (When asked for, enter a password and enter it again)

Open a browser as follows: http://127.0.0.1:8000 and proceed 


Forwarders and receivers:
Forwarders are the ones which forwards the data to splunk setup. Receivers will receive the data for post processing. In order for data transfer to be successful, both the forwarder and receiver need to be configured. 

Splunk universal forwarder setup
tar xvzf splunkforwarder-<…>-Linux-x86_64.tgz -C /opt
Configure folder for monitoring
$ /opt/splunkforwarder/bin/splunk add monitor /home/karthikvr/GSE_GitHub/OVN_master/oneview-nagios/splunk_logs
Configure splunk server with port info for monitoring
$ /opt/splunkforwarder/bin/splunk add forward-server 10.188.239.16:9997

splunk receiver setup (on splunk enterprise UI)
Follow this link to configure receiver. - http://docs.splunk.com/Documentation/Forwarder/7.2.1/Forwarder/Enableareceiver 
