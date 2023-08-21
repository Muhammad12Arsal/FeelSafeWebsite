from flask import Flask , render_template,request ,redirect
import csv
app = Flask(__name__)
app=Flask(__name__,template_folder='templates')


@app.route("/")
def my_home():
    return render_template('index.html')


# def write_to_file(data):
#     with open('database.txt',mode = 'a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file=database.write(f'\n{email},{subject},{message}')
        
def write_to_csv(data):
    with open('database2.csv', newline='' ,mode = 'a') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer=csv.writer(database2,delimiter= ',' , quotechar='"',quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data =request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return my_home1()
        except:
            return 'Did not save to database'
       
    else:
        return 'Something went wrong '

@app.route("/thankyou.html")
def my_home1():
    return render_template('thankyou.html')
