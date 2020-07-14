import json
import cv2

def lambda_handler(event, context):
    print(json.dumps(event))
    print('OpenCV', cv2.__version__)
    # No error
    return {
        'statusCode': 200
    }
