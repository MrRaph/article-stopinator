from datetime import datetime, time
import boto3, json
import time as t

ec2 = boto3.resource('ec2')

def doStop(event, context):

    response = "doStop"

    for instance in filterInstances(event['ENV'], 'running'):
        if instance.tags :
          for tag in instance.tags:
            if tag['Key'] == "Name" :
              response += "Name: " + tag['Value']
              print "Stopping instance : " + tag['Value']
            elif tag['Key'] == "Environment":
                response += "Environment: " + tag['Value']
        instance.stop()

    return response

def filterInstances(env, state):
    filters = [
            {'Name':'tag:Environment', 'Values':[ env ]},
            {'Name': 'instance-state-name', 'Values': [ state ]}
        ]
    allInstances = ec2.instances.filter(Filters=filters)

    return allInstances
