import pytesseract
from PIL import Image 
import re
from gtts import gTTS 
import os
import datefinder
import PIL.Image as PILimage
from PIL import ImageDraw, ImageFont, ImageEnhance
from PIL.ExifTags import TAGS, GPSTAGS

# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 


# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class Hello(Resource): 

	# corresponds to the GET request. 
	# this function is called whenever there 
	# is a GET request for this resource 
    def get(self): 
        pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        img=Image.open('WAPP_4.jpeg')
        text=pytesseract.image_to_string(img)
        print(text)
        matches = datefinder.find_dates(text)
        matches = str(matches)
        print("Matches : " + matches)
        # a = re.findall('EXP.(.+)', text, re.IGNORECASE)
        # print(a[0])
        return(matches) 

	# Corresponds to POST request 
    def post(self): 
		
        data = request.get_json()	 # status code 
        return jsonify({'data': data}), 201


# another resource to calculate the square of a number 
class Square(Resource): 

    def get(self, num): 
        pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        num = str(num)
        image_name = num + ".jpeg"
        #img=Image.open(image_name)
        img = PILimage.open(image_name)

        class Worker(object):
            def __init__(self, img):
                self.img = img
                self.get_exif_data()
                self.date =self.get_date_time()
                super(Worker, self).__init__()

            def get_exif_data(self):
                exif_data = {}
                info = self.img._getexif()
                if info:
                    for tag, value in info.items():
                        decoded = TAGS.get(tag, tag)
                        if decoded == "GPSInfo":
                            gps_data = {}
                            for t in value:
                                sub_decoded = GPSTAGS.get(t, t)
                                gps_data[sub_decoded] = value[t]

                            exif_data[decoded] = gps_data
                        else:
                            exif_data[decoded] = value
                self.exif_data = exif_data
            # return exif_data

        image = Worker(img)
        date = image.date

        
        return date


        # a = re.findall('EXP.(.+)', text, re.IGNORECASE)
        
        
        #a = re.findall('EXP.(.+)', text, re.IGNORECASE)
        
        # return(matches) 
        #return jsonify({'square_new': num**2}) 



# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(Square, '/<num>') 


def main():
    app.run(debug = True) 
   

if __name__ == "__main__":
    main()
     











