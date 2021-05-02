from flask import Flask,request,jsonify,render_template
import test_model
import functions
import loan

app=Flask(__name__)

@app.route('/') #default
def home_page():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        data=request.form
        loan_amnt=int(data['loan_amnt'])
        int_rate=float(data['int_rate'])
        term=int(data['term'])
        annual_inc=float(data['annual_inc'])
        dti=float(data['dti'])
        revol_util=float(data['revol_util'])
        balance_annual_inc=test_model.si(loan_amnt, int_rate, term, annual_inc)
        prediction=test_model.make_prediction(dti, balance_annual_inc, revol_util, annual_inc)
        return prediction
    return render_template('Individual.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004)