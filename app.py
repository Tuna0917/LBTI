from flask import Flask, render_template, request
from questions import *
from alignments import alignment

app = Flask(__name__)
line_page = 1
@app.route("/")
def home():

    return render_template("home.html")

@app.route("/<int:page>/")
def line_question(page:int):
    if page>line_page:
        return render_template('404.html')
    return render_template(
        "question.html", 
        template_page = page, 
        template_line = False,
        template_question=question_list[page], 
        template_answers = line_list,
        )

@app.route("/<int:page>/<line>/")
def champ_question(page:int, line:str):
    que = []
    if line == 'top':
        que = top_list
    elif line == 'jg':
        que = jung_list
    elif line == 'mid':
        que = mid_list
    elif line == 'adc':
        que = adc_list
    elif line == 'sup':
        que = sup_list
    else:
        return render_template('404.html')
    return render_template('question.html', template_page = page, template_line = line, template_question=question_list[page], template_answers = que)

@app.route("/result/<champ>/")
def result(champ:str):
    if champ in alignment:
        return render_template("result.html", alignment = alignment[champ])
    else:
        return render_template('404.html')

app.run()