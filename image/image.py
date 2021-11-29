from flask import Flask,render_template,Response
import os
import face_recognition as fr

app=Flask(__name__)

# image
picFolder = 'static'
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'daun2.jpg')
    return render_template('tes.html', gambar1=pic1)

if __name__=="__main__":
    app.run(debug=True)
