def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

# client = boto3.client('s3')
def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)

