from flask import Flask, redirect, url_for, request
from genqr import genQr
from flask import send_file
from io import BytesIO 

app = Flask(__name__)

@app.route('/genqr',methods = ['POST'])
def generateqrcode():
    content = request.json
    pil_img = genQr(content["url"])
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
   app.run(debug = True)