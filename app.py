from flask import Flask, render_template, request, jsonify
import boto3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    s3 = boto3.client('s3')
    bucket_name = 'nagp-aws-assignment'
    s3.upload_fileobj(file, bucket_name, file.filename)
    return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

