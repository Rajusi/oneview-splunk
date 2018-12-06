# Oneview-Splunk integration

**Problem Statement**

Some of our Synergy customers in EMEA were looking for hardware monitoring solution through OneView and Splunk. We have developed solutions for Nagios XI, Icinga Web2 and custom monitoring solutions. Integrating OneView with Splunk for HPE customer's specific request. 

**Solution design**

To address their needs, we developed a plugin using Python which collects health status and utilization statistics for physical infrastructure including servers and shared resources like enclosures and virtual connects. Plugin does necessary processing of collected data before posting to Splunk.

This solution seamlessly sends configured type of alerts to Splunk.


**End outcome**

Once the data is posted to Splunk, user can view the same and send northbound for consumption. The solution we developed is more generic monitoring solution and doesn't limit to any particular customer. The plugin can be deployed on any Linux based server or a docker container.


## Getting Started

System requirements - Centos7 machine for plugin deployment, Splunk server and OneView appliance.

### Prerequisites and Installing the components of test environment

Setting up the Splunk server
```
1. Create an account in Splunk - https://www.splunk.com/
2. Download Splunk for enterprise from official website after logging in. Link is something like this:- wget -O splunk-7.2.1-be11b2c46e23-Linux-x86_64.tgz 'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=7.2.1&product=splunk&filename=splunk-7.2.1-be11b2c46e23-Linux-x86_64.tgz&wget=true'

3. Create user and group for Splunk (All as root user if not mentioned otherwise). Follow the commands. 
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
	
4. Forwarders and receivers:
	Forwarders are the ones which forwards the data to splunk setup. Receivers will receive the data for post processing. In order for data transfer to be successful, both the forwarder and receiver need to be configured. 
	
	Splunk universal forwarder setup:
	$ tar xvzf splunkforwarder-<…>-Linux-x86_64.tgz -C /opt
	Configure folder for monitoring:
	$ /opt/splunkforwarder/bin/splunk add monitor <log folder to be monitored>
	Configure splunk server with port info for monitoring:
	$ /opt/splunkforwarder/bin/splunk add forward-server <IP Address>:<PortNo>
	
	Splunk receiver setup (on splunk enterprise UI)
	Follow this link to configure receiver. - http://docs.splunk.com/Documentation/Forwarder/7.2.1/Forwarder/Enableareceiver 



```

Setting up the Linux  machine with python3.6 and relevant packages. 
```
1. To setup python3.6
	Step 1: Open a Terminal and add the repository to your Yum install.
	$ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
	
	Step 2: Update Yum to finish adding the repository.
	$ sudo yum update
	
	Step 3: Download and install Python.		
	$ sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
	
	Step 4: Once these commands are executed, simply check if the correct version of Python has been installed by executing the following command:
	$ python3.6 -V
	
	
2. To setup relevant python3.6 modules. 
	Step1: The required python3.6 modules and their versions are mentioned in the file requirements.txt; Install them using the below command.
	$ pip3 install -r requirements.txt
```
Setting up the OneView appliance. 
```
1. Download and install the latest version of OneView appliance from the source link - https://www.hpe.com/in/en/resources/integrated-systems/oneview-trial.html
2. Add a server hardware via enclosure or iLO.
```

### Files to be modified - ***config/input_config_splunk.json***.

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
$ python3.6 main.py -i config/input_config_splunk.json
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

