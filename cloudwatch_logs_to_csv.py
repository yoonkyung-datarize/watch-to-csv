# ----------------------------------------------------------------------------------
# REFERENCE
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.filter_log_events 
# ----------------------------------------------------------------------------------

from datetime import datetime
from config import *

import boto3
import csv

# ----------------------------------------------------------------------------------
# CONFIG SETTINGS
# ----------------------------------------------------------------------------------
log_group_name=LOG_GROUP_NAME
log_stream_name=LOG_STREAM_NAME

start_time=int(datetime.strptime(START_TIME, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
end_time=int(datetime.strptime(END_TIME, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)

filter_pattern=FILTER_PATTERN

# ----------------------------------------------------------------------------------
# GET LOGS FROM CLOUDWATCH
# ----------------------------------------------------------------------------------
client = boto3.client(
    service_name="logs",
    region_name="ap-northeast-2",
)

response = client.filter_log_events(
    logGroupName=log_group_name,
    logStreamNames=[log_stream_name],
    startTime=start_time,
    endTime=end_time,
    filterPattern=filter_pattern
)

first_events = response.get("events")

# ----------------------------------------------------------------------------------
# WRITE CSV
# ----------------------------------------------------------------------------------
fields = ["timestamp", "message"]
row_num = 1
with open(f"{FILE_NAME}.csv", "w", newline='') as f:
    
    write = csv.writer(f)
    write.writerow(fields)
    print(f"WRITING CSV IS STARTED...")
    
    for event in first_events:
        
        if row_num % 10 == 1:
            print(f"1번째 response에 대한 {row_num}...")
            
        write.writerow([event.get("timestamp"), event.get("message")])
        row_num += 1
            
    # 다음 토큰이 존재하면 계속 반복
    cnt = 2
    while 'nextToken' in response.keys():
        currentToken = response.get("nextToken")
        
        response = client.filter_log_events(
            logGroupName=log_group_name,
            logStreamNames=[log_stream_name],
            startTime=start_time,
            endTime=end_time,
            filterPattern=filter_pattern,
            nextToken=currentToken
        )
        
        next_events = response.get("events")
        if len(next_events) == 0:
            break

        for event in next_events:
            
            if row_num % 10 == 1:
                print(f"{cnt}번째 response에 대한 {row_num} row...")
                
            write.writerow([event.get("timestamp"), event.get("message")])
            row_num += 1

        cnt += 1
        
    
    print(f"WRITING CSV IS FINISHED...")