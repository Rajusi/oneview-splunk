# Oneview-Splunk integration

## Getting Started

Prerequisites - 

```
Machine to run the python script:
	Centos 7.3 
	python 3.6
	pip3 latest to install the following modules (including HPE oneview python module)
		amqplib==1.0.2
		future==0.16.0
		requests==2.10.0
		setuptools==39.0.1
		six==1.11.0
		hponeview==4.7.0
		
	Steps to follow the splunk heavy forwarder is out of the scope of this document. Please refer to literature on splunk website.

```

Steps to configure above machine for running the script:
```
1. Clone the project folder to suitable location and navigate to it. 
2. Run the following command to install the required modules. 	
	$ pip3 install -r requirements.txt

```
### Installing the components of test environment

We assume that the Splunk enterprise server is configured to receive data from splunk forwarders and the port numbers are known
```	
Configure folder for log monitoring:
$ <SPLUNK_FORWARDER_HOME>./splunk add monitor <log folder to be monitored>
Eg: $ <SPLUNK_FORWARDER_HOME>./splunk add monitor /home/path/to/project/folder/oneview_splunk_logs
	
Configure the machine to forward logs to splunk server with port info:
$ <SPLUNK_FORWARDER_HOME>./splunk add forward-server <Splunk server IP>:<PortNo>
Eg: <SPLUNK_FORWARDER_HOME>./splunk add forward-server 10.10.1.1:9997
	
``



### To run as standalone script

Ensure the following:
1. Splunk server up and running. 
2. Splunk server configured to receive data on a specific port. 
3. Splunk forwarder configured with splunk server, port and the folder with log data to be forwarded. 


Once the above are checked, follow the steps below:-
1. Edit the input config file.
```
	"host": IP Address of the host
	"alias": Alias name for the OneView instance
	"user": OneView username
	"passwd": Encrypted password
	"action": "start" ; (The action to be performed. Don't modify for now.)
	"route": "scmb.alerts.#" ; (SCMB route. Don't modify for now.)
	"alert_type": "Critical:Warning:Ok", (Alert types. You can remove some if not required.)
	"alert_hardware_category": "server-hardware:enclosures:interconnects:logical-interconnects:sas-interconnects" (List of all hardware types. You can remove some if now required)
```
2. Start the script
```
Command to run the script:
$ <Project_Home>python3.6 main.py -i input.json
Eg: $ /home/user1/oneview_splunk python3.6 main.py -i config.json

```

### To see alert data which is sent to Splunk server. Check the same being received on Splunk enterprise server
Generate alerts from oneview and ensure that the alerts are captured by the script. 
Monitor the log folder using tail command. "tail -f <LOG_FILE>"
Eg:
`$ tail -f oneview_splunk_logs/oneview_alerts_splunk.log`

	
## Built With

* Splunk enterprise - The monitoring tool used.
* OneView - Appliance which is used to configure and manage the servers
* Python3.6 - Scripting language used


## Versioning

We use [GitHub](http://github.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **GSE Team, Bangalore** 

## License

(C) Copyright (2018) Hewlett Packard Enterprise Development LP

