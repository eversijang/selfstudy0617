from env import *
import boto3
import json


s3_client = boto3.client("s3")
rds_client = boto3.client('rds')
dynamodb = boto3.resource("dynamodb")
# dynamodb_client = boto3.client('dynamodb')
table = dynamodb.Table('RDS-EOS')


def get_session(A_KEY, S_KEY, REGION):
    session = boto3.Session(
        aws_access_key_id=A_KEY,
        aws_secret_access_key=S_KEY,
        region_name=REGION
    )
    return session


if __name__ == "__main__":
    session = get_session(A_KEY, S_KEY, REGION)
    # rds_response = rds_client.describe_db_engine_versions(Engine='mysql')
    rds_response = rds_client.describe_db_engine_versions(Engine='aurora-mysql',
                                                          Filters=[{'Name': 'status', 'Values': ['available']}])
    # Filters=[{'Name': 'status', 'Values': ['available']}])
    #   Filters=[{'Name': 'status', 'Values': ['deprecated']}])

    # ENGINE 종류
    # aurora        (for MySQL 5.6-compatible Aurora)
    # aurora-mysql  (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)
    # aurora-postgresql
    # mariadb
    # mysql
    # oracle-ee
    # oracle-ee-cdb
    # oracle-se2
    # oracle-se2-cdb
    # postgres
    # sqlserver-ee
    # sqlserver-se
    # sqlserver-ex
    # sqlserver-web

# print(len(rds_response['DBEngineVersions']))
# print(rds_response['DBEngineVersions'])
res = rds_response['DBEngineVersions']

# out = json.dumps(res, indent=4, default=str)
# print(out)
for i in range(len(res)):
    print("{} : {}".format(res[i]['Engine'], res[i]['EngineVersion']))

    # EOS 대상
    # aws rds describe-db-engine-versions --engine mysql
    #  --query "DBEngineVersions[*].{Engine:Engine, EngineVersion:EngineVersion}"
    #  --filters "Name=status,Values=deprecated"

    # Support 대상
    #  aws rds describe-db-engine-versions --engine mysql
    #  --query "DBEngineVersions[*].{Engine:Engine, EngineVersion:EngineVersion}"
    #  --filters "Name=status,Values=available"
