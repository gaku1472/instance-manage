import os
import time
import googleapiclient.discovery
import json
import base64

def start_instance(compute, project, zone, instance_name):
    return compute.instances().start(
		project=project,
		zone=zone,
		instance=instance_name).execute()

def main(event, context):
	data = json.loads(base64.b64decode(event['data']).decode('utf8'))
	instance_name = data["instance_name"]
	zone = data["zone"]
	project = "INPUT PROJECT NAME"

	compute = googleapiclient.discovery.build('compute', 'v1')
	start_instance(compute, project, zone, instance_name)
