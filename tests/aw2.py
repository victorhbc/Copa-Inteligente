import boto3

client = boto3.client('rekognition')

photo = './images/dylan.jpg'

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image={'Bytes': source_bytes})

a = response['Labels']

i = 0

while i < len(a):
    if a[i]['Name'] == 'Person':
        x = a[i]
    i += 1
    pass

print(x)

print(str(x).count("BoundingBox"))
