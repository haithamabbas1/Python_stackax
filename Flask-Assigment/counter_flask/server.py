from flask import Flask , render_template, request, redirect, session

app=Flask(__name__)
app.secret_key='lkjhfdfsdfs'

@app.route('/')
def function1():
    if 'x' not in session:
        session['x']=0
    else:
        session['x']=session['x']+1
    return render_template("couner.html")


@app.route("/reset", methods=["POST"])
def function2():
    session['x']=0
    return redirect('/')

@app.route("/addby2", methods=["POST"])
def function3():
    session['x']+=1
    return redirect('/')







if __name__=="__main__":
    
    app.run(debug=True) 