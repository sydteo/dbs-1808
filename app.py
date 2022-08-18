#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib


# In[4]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1=r1, result2=r2))
    else:
        return(render_template("index.html", result1="waiting", result2="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




# from flask import Flask
# app = Flask(__name__)
# from flask import request, render_template
# import joblib

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         rates = request.form.get("rates")
#         model1 = joblib.load("DBSReg")
#         pred1 = model1.predict([[float(rates)]])
#         model2 = joblib.load("DBSDT")
#         pred2 = model2.predict([[float(rates)]])
#         model3 = joblib.load("DBSNN")
#         pred3 = model3.predict([[float(rates)]])
#         s1 = "The predicted DBS share price using Regression is " + str(pred1)
#         s2 = "The predicted DBS share price using Decision Tree is " + str(pred2)
#         s3 = "The predicted DBS share price using Neural Network is " + str(pred3)
#         return(render_template("index.html", result1 = s1, result2=s2, result3=s3))
#     else:
#         return(render_template("index.html", result1="2", result2="2", result3="2"))

# if __name__ == "__main__":
#     app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




