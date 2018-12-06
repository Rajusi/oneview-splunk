# Oneview-Splunk integration

## Getting Started

System requirements - 

We have tested with Centos running 7.3 and it should work with other machines as well:
	1. Centos7.3 or above. 
	2. python 3.6 or above
	
Steps to configure above machine for running the script:
	1. Clone the project folder to suitable location. 
	2. Extract the folder and navigate to it
	3. Run the following command to install the required modules. 
		$ pip3 install -r requirements.txt
	
	4. Configure the splunk forwarder to forward the logs from the folder "oneview_splunk_logs" from the project folder


### Prerequisites and Installing the components of test environment

We assume that the Splunk enterprise server is configured to receive data from splunk forwarders and the port numbers are known
```	
	Configure folder for log monitoring:
	$ <SPLUNK_FORWARDER_HOME>./splunk add monitor <log folder to be monitored>
	Eg: $ <SPLUNK_FORWARDER_HOME>./splunk add monitor /home/path/to/project/folder/oneview_splunk_logs
	
	Configure splunk server with port info for monitoring:
	$ <SPLUNK_FORWARDER_HOME>./splunk add forward-server <IP Address>:<PortNo>
	Eg: <SPLUNK_FORWARDER_HOME>./splunk add forward-server 10.10.1.1:9997
	
```

### Files to be modified - ***input_config_splunk.json***.

Edit the following information:
```
1. OneView details - ipaddress, username, password, alert type and alert hardware category.
2. Logging level
```



### To run as standalone script

Ensure the following:
1. Splunk server up and running. 
2. Splunk server configured to receive data on a specific port. 
3. Splunk forwarder configured with splunk server, port and the folder with log data to be forwarded. 

Once the above are checked, execute as follows:-

```
$ python3.6 main.py -i input_config_splunk.json
```

### To see alert data which is sent to Splunk server. Check the same being received on Splunk enterprise server

`$ tail -f oneview_splunk_logs/oneview_alerts_splunk.log`

	
## Built With

* Splunk enterprise - The monitoring tool used.
* OneView - Appliance which is used to configure and manage the servers
* Python3.6 - Scripting language used


## Versioning

We use [GitHub](http://github.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **GSE Team, Bangalore** 

See also the list of [contributors](https://github.hpe.com/GSE/oneview-nagios/graphs/contributors) who participated in this project.

## License

(C) Copyright (2018) Hewlett Packard Enterprise Development LP

## Acknowledgments

