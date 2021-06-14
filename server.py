from flask import Flask, redirect, request, session, render_template
import random
import datetime
app=Flask(__name__)
app.secret_key=("keykey")
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'textlog' not in session:
        session['textlog']=[]
    return render_template ('index.html', gold=session['gold'])
@app.route('/process_money', methods=['POST'])
def process():
    now =('({:%Y-%m-%d %H:%M:%S})'.format(datetime.datetime.now()))
    if request.form['place']=="farm":
        num=random.randint(10,20)
        session['gold']+=num
        session['textlog'].append("You earned {} gold from the farm! {}".format(num, now))
    if request.form['place']=="cave":
        num=random.randint(5,10)
        session['gold']+=num
        session['textlog'].append("You earned {} gold from the cave! {}".format(num, now))
    if request.form['place']=="house":
        num=random.randint(2,5)
        session['gold']+=num
        session['textlog'].append("You earned {} gold from the house! {}".format(num, now))
    if request.form['place']=="casino":
        num=random.randint(-50,50)
        session['gold']+=num
        if num <0:
            session['textlog'].append("Entered a casino and lost {} gold...ouch. {}".format(abs(num), now)) 
        else:
            session['textlog'].append("You won {} gold from the casino!!! {}".format(num, now))
    return redirect('/')
@app.route('/reset')
def reset():
    session['gold']=0
    session['textlog']=[]
    return redirect('/')
    
app.run(debug=True)