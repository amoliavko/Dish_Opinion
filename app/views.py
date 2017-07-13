from flask import render_template, request, stream_with_context, Response
from app import app, db
from app.model import Table


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method =='POST':

        def generate():
            # yield request.args['name']
            yield render_template('thanks.html')

        if request.form['submit'] == 'good':
            # Table.query.filter_by(level='good').update({'value':0})
            Table.query.filter_by(level='good').first().value += 1
            db.session.commit()

            return Response(stream_with_context(generate()))
        elif request.form['submit'] == 'normal':
            Table.query.filter_by(level='normal').first().value += 1
            db.session.commit()
            return Response(stream_with_context(generate()))
        elif request.form['submit'] == 'bad':
            Table.query.filter_by(level='bad').first().value += 1
            db.session.commit()
            return Response(stream_with_context(generate()))

    return render_template('index.html')


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html')


@app.route('/result', methods=['GET', 'POST'])
def result():

    out = [0, 0, 0]
    out[0] = Table.query.filter_by(level='good').first().value
    out[1] = Table.query.filter_by(level='normal').first().value
    out[2] = Table.query.filter_by(level='bad').first().value

    return render_template('result.html', result=out)
