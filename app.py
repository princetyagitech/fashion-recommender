from flask import Flask, render_template, redirect, request

from predict import Predict
app = Flask(__name__)
p=Predict()
@app.route('/')
def hello():
    return render_template("index.html")



@app.route('/home')
def home():
    return redirect('/')

@app.route('/', methods = ['POST'])
def marks():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        caption = p.get_recs(path)
    
        dic = {'image' : path ,
               'caption' : caption}
    return render_template("index.html",cap=dic)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run("0.0.0.0", 5000, threaded=False)
