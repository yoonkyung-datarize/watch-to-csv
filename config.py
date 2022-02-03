
# 로그 그룹명을 입력한다
LOG_GROUP_NAME=""
# 로그 스트림명을 입력한다
LOG_STREAM_NAME=""

#----------------------------------------
# 하루를 기준으로 하고자 할 때 예시
# START_TIME = "2022-05-08 00:00:00"
# END_TIME = "2022-05-08 23:59:59"
# 로 설정하면 된다.
#----------------------------------------
START_TIME="2022-01-10 00:00:00"
END_TIME="2022-01-10 11:59:59"

#----------------------------------------
# filter pattern은 다음을 참고한다
# https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html
#----------------------------------------
FILTER_PATTERN="{$.log=\"[10048]*\"}"

# 저장 할 파일명을 입력한다
FILE_NAME="onsite-test"

