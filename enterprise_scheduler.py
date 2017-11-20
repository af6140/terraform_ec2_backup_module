from __future__ import print_function # Python 2/3 compatibility
import boto3
import datetime
import sys

def lambda_handler(event, context):
    backup_tag = 'backup_enabled'
    schedule_tag = 'backup_schedule'
    max_delta = 12
    now = datetime.datetime.now()
    ec2 = boto3.resource('ec2')
    events = boto3.resource('events')
    client = boto3.client('ec2')
    scheduled_instances = []
    processed_instances = []
    #filter for instances with the correct tag
    instances = ec2.instances.filter(Filters=[{'Name': 'tag-key', 'Values':[schedule_tag]}])
    #grab the scheduler string
    for instance in instances:
        for tag in instance.tags:
            if tag['Key'] == schedule_tag:
                scheduled_instances.append({'instance':instance, 'schedule':tag['Value']})

    events.list_rule({
     NamePrefix='backup_event_rule'
    })
