import pytesseract
import cv2
import requests
import json


string=str(input('enter the word that you want to search the meaning for!!'))
url=f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{string}'
response = requests.get(url)
dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)


response_json=response.json()

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
fil=input("enter the name of the file")
img=cv2.imread(f'images/{fil}.png')



img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
a=pytesseract.image_to_string(img)


hImg,wImg,_=img.shape
boxes=pytesseract.image_to_data(img)

A=''
B=''

try:
    response_json[0]['meanings'][0]['definitions'][1]['definition']
    print(response_json[0]['meanings'][0]['definitions'][1]['definition'])
    # print(response_json[0]['meanings'][0]['definitions'][0]['definition'])
    
    A=response_json[0]['meanings'][0]['definitions'][1]['definition']
    
except IndexError:
    # print(response_json[0]['meanings'][0]['definitions'][0]['definition'])
    B=response_json[0]['meanings'][0]['definitions'][0]['definition']
    
    
x=0
y=0
w=0
h=0


for a,b in enumerate(boxes.splitlines()):
    if a!=0:
        b=b.split()
        # print(b)
        if(b[-1]==string or b[-1]==string.upper() or b[-1]==string.lower() or b[-1]==string.capitalize()):
            x=int(b[6])
            y=int(b[7])
            w=int(b[8])
            h=int(b[9])
    

        if len(b)==12:
            cv2.rectangle(img,(x,y),(w+x,y+h),(0,0,255),3)
            # cv2.putText(img,string,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
            cv2.putText(img,B,(20,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(50,50,255),1)
            cv2.putText(img,A,(20,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(30,50,255),1)
            



cv2.imshow('result',img)
cv2.waitKey(0)
 



