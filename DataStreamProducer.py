import boto3
import random
from time import sleep
client = boto3.client('kinesis')
ip_addresses = ['5.109.13.203', '125.234.34.72', '84.129.116.158', '204.202.149.165', '92.30.228.217', '125.247.125.250', '47.127.56.124', '201.119.188.182', '157.155.128.80', '156.163.24.9']
event_types = [1,2,3,4,5]

def random_event():
	# print(event_types[random.randint(0,len(event_types)-1)])
	return event_types[random.randint(0,len(event_types)-1)]

def random_ip():
	# print(ip_addresses[random.randint(0,len(ip_addresses)-1)])
	return ip_addresses[random.randint(0,len(ip_addresses)-1)]

# stream_description = client.describe_stream(
#     StreamName='test-bot',
#     Limit=123
# )
# print(stream_description)
sleep_seconds = int(input("enter sleep time (integer): "))
for x in range(5):
	ip = random_ip()
	event = str(random_event())
	data = '{"ip": '+ip+', "event": '+event+'}'
	print(data)
	response = client.put_record(
	    StreamName='test-bot',
	    Data=data,
	    PartitionKey=str(x)
	)
	print(response)
	sleep(sleep_seconds)
	

# # for ip in ip_addresses:
# # 	print(ip)
# 	random_event()
# 	pass