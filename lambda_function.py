import boto3
import pymysql

# Function to insert data into RDS database
def insert_data(content_type):
    rds_host = "your-rds-endpoint"
    db_username = "your-db-username"
    db_password = "your-db-password"
    db_name = "your-db-name"
    
    try:
        conn = pymysql.connect(rds_host, user=db_username, passwd=db_password, db=db_name, connect_timeout=5)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO table_name (content_type) VALUES (%s)", (content_type,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully")
    except Exception as e:
        print("Error inserting data:", e)

# Lambda handler
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        response = s3.head_object(Bucket=bucket_name, Key=object_key)
        content_type = response['ContentType']
        
        print("Content Type:", content_type)
        insert_data(content_type)
