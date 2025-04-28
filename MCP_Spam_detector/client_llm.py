import requests

BASE_URL="http://127.0.0.1:8000"

def GetModel():
    response=requests.get(f"{BASE_URL}/mcp/model")
    print(response.json())

def UpdateContext(version, accuracy=None):
    if version or accuracy:
        data={"version":version,"accuracy":accuracy}
        response=requests.post(f"{BASE_URL}/model/update",json=data)
        print(response.json())
    else:
        print("Hi, Please provide the Update Context to update!")
    
   


def Predict(text):
    data={"text":text}
    response=requests.post(f"{BASE_URL}/model/predict",json=data)
    print(response.json())

if __name__ == "__main__":
    GetModel()
    # UpdateContext("v1.1", 0.92)
    # Predict(" hyperlink hyperlink hyperlink let mortgage lenders compete for your business did you receive an email advertisement in error our goal is to only target individuals who would like to take advantage of our offers if you d like to be removed from our mailing list please click on the link below you will be removed immediately and automatically from all of our future mailings we protect all email addresses from other third parties thank you hyperlink please remove me")