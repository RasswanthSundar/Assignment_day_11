import os
import time
from flask import Flask,render_template,request

app = Flask(__name__)  

# Default page uploading files
@app.route('/')  
def upload() :  
    return render_template("file_upload.html")  

# Choose page for choosing the options
@app.route('/choose',methods=['GET','POST'])  
def choose() : 
    if request.method == 'POST' :  
        fil = request.files['file']
        fil.save('upload_file.txt')
    return render_template('choose.html')

# On click of size button it will execute below and redirect to display
@app.route('/size')
def sizefn() :
    # sz is the size display string
    sz = 'Size :' + str(os.path.getsize('upload_file.txt')) + ' bytes'
    return render_template('display.html',text= sz)

# On click of last modified button it will execute below and redirect to display
@app.route('/last_modified')
def last_modified() :
    # lm is the last modified display string
    lm = 'Last Modified :' + str(time.ctime(os.path.getmtime('upload_file.txt')))
    return render_template('display.html',text= lm)

# On click of no of lines button it will execute below and redirect to display
@app.route('/no_of_lines')
def no_of_lines() :
    with open('upload_file.txt') as txtfile :
        # ln is the no of lines display string
        ln = 'No.of Lines :' + str(len(txtfile.readlines()))
    return render_template('display.html',text= ln)

# On click of all three button it will execute below and redirect to display
@app.route('/all_three')
def all_modified() :
    # lm is the last modified display string
    lm = 'Last Modified :' + str(time.ctime(os.path.getmtime('upload_file.txt')))
    with open('upload_file.txt') as txtfile :
        # ln is the no of lines display string
        ln = 'No.of Lines :' + str(len(txtfile.readlines()))
    # sz is the size display string    
    sz = 'Size :' + str(os.path.getsize('upload_file.txt')) + ' bytes'
    # am is the all three string attached display string
    am = ','.join([sz,lm,ln])
    return render_template('display.html',text=am)

# To stop the application on pressing to stop button
@app.route('/stop')  
def stopexe() :
    shut = request.environ.get('werkzeug.server.shutdown')
    shut()
    return ('The Application Has Stopped') 
    
# Main function to run the application on debug mode and set port to 9876
if __name__ == '__main__':  
    app.run(debug = True,port=9876)
    