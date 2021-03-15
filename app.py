from flask import Flask, render_template, request, url_for, redirect
from characters import champions
from quest import QnA, champ_list
app = Flask(__name__)

@app.route("/")
def home():

    return render_template("home.html")

@app.route("/<int:q>/<int:page>/")
def question(page:int, q:int):
    if 2**(q-1)> page or page >= 2**q:
        return redirect(url_for('home'))
    if q==5:
        return redirect(url_for('result', champ=champ_list[page - 16]))
    if q>5 or q<0:
        return redirect(url_for('home'))
    return render_template(
        "question.html", 
        template_page = page, 
        template_question=QnA[q], 
        template_q = q+1
        )

@app.route("/result/<champ>/")
def result(champ:str):
    return render_template("result.html", alignment = champions[champ])

if __name__ == '__main__':
    app.run(debug=True)

