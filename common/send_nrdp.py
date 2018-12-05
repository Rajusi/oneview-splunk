#!/usr/bin/env python
#
# send_nrdp.py
#
# Copyright (c) 2010-2017 - Nagios Enterprises, LLC.
# Written by: Scott Wilkerson (nagios@nagios.org)
#

import optparse, sys, urllib, cgi
from xml.dom.minidom  import parseString
import urllib.request
import logging
def send_nrdp(url, token, hostname, service, state, output, delim, checktype):

	if not url:
		logging.error('You must specify a url.')
	if not token:
		logging.error('You must specify a token.')
	try:
		setup(url, token, hostname, service, state, output, delim, checktype)
	except Exception as e:
		sys.exit(e)

def getText(nodelist):
	rc = []
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc.append(node.data)
	return ''.join(rc)

def post_data(url, token, xml):
	params = urllib.parse.urlencode({'token': token.strip(),'cmd': 'submitcheck', 'XMLDATA': xml});
	opener = urllib.request.FancyURLopener()
	try:
		f = opener.open(url, params)
		result = parseString(f.read())
	except Exception as e:
		print ("Cannot connect to url.")
		sys.exit(e)
	if getText(result.getElementsByTagName("status")[0].childNodes) != "0":
		print ("ERROR - NRDP Returned: "+getText(result.getElementsByTagName("message")[0].childNodes))
		sys.exit(1)

def setup(url, token, hostname, service, state, output, delim, checktype):
	if not delim:
		delim = "\t"
	if not checktype:
		checktype = "1"
	xml="<?xml version='1.0'?>\n<checkresults>\n";

	if hostname and state:
		if service:
			xml += "<checkresult type='service' checktype='"+checktype+"'>"
			xml += "<hostname>"+cgi.escape(hostname,True)+"</hostname>"
			xml += "<servicename>"+cgi.escape(service,True)+"</servicename>"
			xml += "<state>"+state+"</state>"
			xml += "<output>"+cgi.escape(output,True)+"</output>"
			xml += "</checkresult>"
		else:
			xml += "<checkresult type='host'  checktype='"+checktype+"'>"
			xml += "<hostname>"+cgi.escape(hostname,True)+"</hostname>"
			xml += "<state>"+state+"</state>"
			xml += "<output>"+cgi.escape(output,True)+"</output>"
			xml += "</checkresult>"
		xml += "</checkresults>"

	post_data(url, token, xml)