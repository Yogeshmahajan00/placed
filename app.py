# from flask import Flask,render_template,request
# import numpy as np
# import pickle
# model=pickle.load(open("model.pkl","rb"))
# app=Flask(__name__)
# @app.route("/n")
# def index():
#     render_template("html.index")
# @app.route("/pred",methods=["POST"])
# def placement():
#     cgpa=float(request.form.get("cgpa"))
#     iq=float(request.form.get("iq"))
#     profile_score=float(request.form.get("profile_score"))

#     result=model.predict(np.array([[cgpa,iq,profile_score]]))
#     if result[0]==1:
#        return "<h1 style='color:green'>PLACED</h1>"
#     else:
#         return "<h1 style='color:red'>NOT PLACED</h1>"
    

# app.run(debug=True)
    
    
#     # if result[0]==1:
#     #     return "<h1 style='color:green'>PLACED</h1>"
#     # else:
#     #     return "<h1 style='color:red'>NOT PLACED</h1>"



from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_placement():
    cgpa=float(request.form.get("cgpa"))
    iq=float(request.form.get("iq"))
    profile_score=float(request.form.get("profile_score"))
    
    result=model.predict(np.array([[cgpa,iq,profile_score]]))
    
    if result[0]==1:
        return "<h1 style='color:green'>PLACED</h1>"
    else:
        return "<h1 style='color:red'>NOT PLACED</h1>"
    
app.run(debug=True,port=5001)
    
    
# @app.route("/predict",methods=["GET"])
# def predict_placement():
#     cgpa=float(request.args.get("cgpa"))
#     iq=float(request.args.get("iq"))
#     profile_score=float(request.args.get("profile_score"))
    
    
#     result=model.predict(np.array([[cgpa,iq,profile_score]]))
    
#     if result[0]==1:
#         return "<h1 style='color:green'>PLACED</h1>"
#     else:
#         return "<h1 style='color:red'>NOT PLACED</h1>"   

# app.run(debug=True,port=5001)

