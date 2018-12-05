# -*- coding: utf-8 -*-
###
# (C) Copyright (2018) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

import logging

# Nagios service status permitted as follows: OK = 0, Warning = 1, Critical = 2, Unknown = 3; 
# For ports, status DISABLED = Warning
#
serviceStatusMap = {'OK':0, 'WARNING':1, 'CRITICAL':2, 'UNKNOWN':3, 'DISABLED':1}

# Nagios statuses permitted : UP = 0, DOWN = 1, UNREACHABLE = 2; 
# Mapping Host statuses from Oneview onto Nagios as follows: 
# OK - UP, WARNING = UP, CRITICAL = DOWN, UNKNOWN = UNREACHABLE, DISABLED = DOWN.
#
nodeStatusMap = {'OK':0, 'WARNING':0, 'CRITICAL':1, 'UNKNOWN':2, 'DISABLED':1}
##################################################################
# Function to append the service tag to the end of service name. 
##################################################################
def get_required_service_name(service_name, uri):
	
	temp = uri.split('/')
	if temp:
		id = temp[-1]
		service_name += '_' + str(id)
		service_name = service_name.replace(" ", "_")
		logging.info("Service name :- " + service_name)
	else:
		logging.error('No service id: URI - ' + str(uri))
			
	return service_name

##################################################################
# Map oneview alert status of service to nagios status
##################################################################
def map_service_Status(status):
	
	# Nagios service status : OK = 0, Warning = 1, Critical = 2, Unknown = 3
	# {'OK':0, 'WARNING':1, 'CRITICAL':2, 'UNKNOWN':3}
	
	if status.upper() in serviceStatusMap:
		id = serviceStatusMap[status.upper()]
	else:
		logging.error("Alert status received :" + str(status) + ". Cannot find service status. Assigning to unknown.")
		id = 3
		logging.error("Alert status received : " + str(status) + ". Mapped to id = %d (Unknown) ", id)
		
	return id


##################################################################
# Map oneview alert status of node to nagios status
##################################################################
def map_node_status(status):
	# Nagios host status - {'OK':0, 'WARNING':0, 'CRITICAL':1, 'UNKNOWN':2, 'DISABLED':1}
		
	if status.upper() in nodeStatusMap:
		id = nodeStatusMap[status]
	else:
		id = 2
		logging.error("Cannot find node status - Received : " + str(status) + ". Mapped to id = %d (Unreachable) ", id)
	
	return id
	
	
