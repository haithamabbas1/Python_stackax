from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route("/")
def function():
    return render_template("index.html")

@app.route("/result",methods=['POST', 'GET'])
def result():
    name=request.form["name"]
    location=request.form["location"]
    language=request.form["language"]
    textarea=request.form["textarea"]
    return render_template("result.html",name=name,location=location,language=language,textarea=textarea)


if __name__=="__main__":
    app.run(debug=True)