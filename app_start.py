from flask import Flask, render_template, request, url_for, redirect
from characters import champions
from quest import QnA, champ_list, texts
app = Flask(__name__)

@app.route("/")
def home():

    return render_template("home.html")

@app.route("/<int:q>/<int:page>/<int:answer>")
def question(page, q, answer):
    if 2**(q-1)> page or page >= 2**q:
        return redirect(url_for('home'))
    if q==5:
        
        return redirect(url_for('result', champ=champ_list[page - 16], answer = answer))
    if q>5 or q<0:
        return redirect(url_for('home'))
    return render_template(
        "question.html", 
        template_page = page, 
        template_question=QnA[q-1], 
        template_q = q+1,
        template_answer = answer
        )

@app.route("/result/<champ>/<int:answer>")
def result(champ,answer):
    if not answer in [0,1,10,11,100,101,110,111,1000,1001,1010,1011,1100,1101,1110,1111]:
        return redirect(url_for("home"))
    answer = '000'+str(answer)
    ans = ''
    for i,x in enumerate(reversed(answer)):
        ans += texts[i][int(x)]
        if i ==3:
            break
    return render_template("result.html", alignment = champions[champ],answer=ans)

if __name__ == '__main__':
    app.run(debug=True)

