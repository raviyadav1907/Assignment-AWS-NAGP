from flask import Flask, render_template, request, jsonify
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    s3 = boto3.client('s3')
    bucket_name = 'Assignment-AWS-S3'
    s3.upload_fileobj(file, bucket_name, file.filename)
    return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
