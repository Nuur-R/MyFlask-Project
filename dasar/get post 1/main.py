from flask import Flask,render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # buat GET request
    if request.method=='GET':
        if 'nama' in request.args:
            name = request.args['nama']
            print (name)
    # buat POST request
    if request.method=='POST':
        age = request.form['umur']
        print (age)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)