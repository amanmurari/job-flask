from flask import Flask ,render_template,jsonify,request,session,redirect

from database import pagination,load_all,find_job,apply

import math

app = Flask(__name__)

app.secret_key = "aman><jo¢¢√×€π¶¥÷\÷•£¢π¶©]}¥¥°¥×π√¶{©=$+:::;;?&$/bbrr**+:;#()[]_?!$$|%^*+=singh"

data =  load_all()    


@app.route("/apply" ,methods=["POST"])
def apply_job():
    apply(request.form)
    return render_template('log.html',data=request.form)
 
                               
@app.route('/')
def index():
    return render_template('index.html',data=pagination(1))

        
@app.route('/data/<int:id>')
def page(id):
  data =  load_all()
  length =math.ceil(len(data)/5)
  page_num = pagination(id)
  return render_template('ama.html',user = length,data= page_num,page_id=id)


@app.route("/job/<int:id>")
def job(id):
    job_detail = find_job(id)
    return render_template("job.html",data=job_detail,page_id=id)
 
 
@app.route('/about')     
def about():
      return render_template('about.html')


@app.errorhandler(404)
def page_not_found(error):
      return render_template('page_not_found.html', error= error)      
      
       
        
                       
                        
                          
if (__name__=="__main__"):
  app.run(host='0.0.0.0',debug=True)