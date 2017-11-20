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
    event_detail = event['detail']
    instance_id = detail['instance_id']
    event_name = detail['eventName']

    if event_name == 'CreateTags':
        
