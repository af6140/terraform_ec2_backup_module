# terraform_ec2_backup_module

https://stackoverflow.com/questions/43716360/aws-ec2-get-notified-when-a-tag-changes
http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/LogAPICall.html
## Example cloudtrail `CreateTags` event
```json
{
	"eventVersion": "1.04",
	"userIdentity": {
		"type": "Root",
		"principalId": "111122223333",
		"arn": "arn:aws:iam::111122223333:root",
		"accountId": "111122223333",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2017-03-01T18:02:37Z"
			}
		}
	},
	"eventTime": "2017-03-01T19:25:47Z",
	"eventSource": "elasticfilesystem.amazonaws.com",
	"eventName": "CreateTags",
	"awsRegion": "us-west-2",
	"sourceIPAddress": "192.0.2.0",
	"userAgent": "console.amazonaws.com",
	"requestParameters": {
		"fileSystemId": "fs-00112233",
		"tags": [{
				"key": "TagName",
				"value": "AnotherNewTag"
			}
		]
	},
	"responseElements": null,
	"requestID": "dEXAMPLE-feb4-11e6-85f0-736EXAMPLE75",
	"eventID": "eEXAMPLE-2d32-4619-bd00-657EXAMPLEe4",
	"eventType": "AwsApiCall",
	"apiVersion": "2015-02-01",
	"recipientAccountId": "111122223333"
}
```

## `DeleteTags` CloudTrail event

```json
{
	"eventVersion": "1.04",
	"userIdentity": {
		"type": "Root",
		"principalId": "111122223333",
		"arn": "arn:aws:iam::111122223333:root",
		"accountId": "111122223333",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"attributes": {
				"mfaAuthenticated": "false",
				"creationDate": "2017-03-01T18:02:37Z"
			}
		}
	},
	"eventTime": "2017-03-01T19:25:47Z",
	"eventSource": "elasticfilesystem.amazonaws.com",
	"eventName": "DeleteTags",
	"awsRegion": "us-west-2",
	"sourceIPAddress": "192.0.2.0",
	"userAgent": "console.amazonaws.com",
	"requestParameters": {
		"fileSystemId": "fs-00112233",
		"tagKeys": []
	},
	"responseElements": null,
	"requestID": "dEXAMPLE-feb4-11e6-85f0-736EXAMPLE75",
	"eventID": "eEXAMPLE-2d32-4619-bd00-657EXAMPLEe4",
	"eventType": "AwsApiCall",
	"apiVersion": "2015-02-01",
	"recipientAccountId": "111122223333"
}
```
