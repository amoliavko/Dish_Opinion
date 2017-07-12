from flask import Flask, render_template, request, redirect, url_for, stream_with_context, Response
from app import app
import time

out = [0, 0, 0]


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method =='POST':

        def generate():
            # yield request.args['name']
            yield render_template('thanks.html')

        if request.form['submit'] == 'good':
            global out
            out[0] += 1
            return Response(stream_with_context(generate()))
        elif request.form['submit'] == 'normal':
            global out
            out[1] += 1
            return Response(stream_with_context(generate()))
        elif request.form['submit'] == 'bad':
            global out
            out[2] += 1
            return Response(stream_with_context(generate()))

    return render_template('index.html')


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html', result=out)
