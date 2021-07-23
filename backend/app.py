from flask import Flask, request, Response
import datetime
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
app = Flask(__name__)

my_config = Config(
    region_name = 'eu-north-1'
)

@app.route('/backend', methods = ['POST'])
def backend():
    message = request.form['message']
    file_name = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time())
    s3 = boto3.client('s3', config=my_config)
    with open(file_name, "w") as fo:
        fo.write(message)
    s3.upload_file(file_name, "php-project",file_name)    
    return message
    

@app.route('/index', methods = ['GET'])
def index():
    return Response(status=200)