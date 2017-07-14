from flask import render_template, request, stream_with_context, Response
from app import app, db
from app.model import Table
from datetime import datetime


def db_filter(location, rating):
    db.session.add(Table(location=location, rating=rating, data=datetime.now()))
    # Table.query.filter_by(level='good').update({'value':0})


@app.route('/office', methods=['GET', 'POST'])
def office():
    if request.method =='POST':
        def generate():
            # yield request.args['name']
            yield render_template('thanks.html')

        if request.form['submit'] == 'good':
            db_filter('office', 'good')

        elif request.form['submit'] == 'normal':
            db_filter('office', 'normal')

        elif request.form['submit'] == 'bad':
            db_filter('office', 'bad')

        db.session.commit()
        return Response(stream_with_context(generate()))
    return render_template('office.html')


@app.route('/kitchen', methods=['GET', 'POST'])
def kitchen():
    if request.method =='POST':
        def generate():
            yield render_template('thanks.html')

        if request.form['submit'] == 'good':
            db_filter('kitchen', 'good')

        elif request.form['submit'] == 'normal':
            db_filter('kitchen', 'normal')

        elif request.form['submit'] == 'bad':
            db_filter('kitchen', 'bad')

        db.session.commit()
        return Response(stream_with_context(generate()))
    return render_template('kitchen.html')


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html')


@app.route('/result', methods=['GET', 'POST'])
def result():

    # out = Table.query.filter_by(rating='normal').first().data
    # out = Table.query.filter_by(rating='bad').count()
    # for i in Table.query.filter_by(rating='good'):
    #     out.append(i.data)
    # out = [r for r in db.session.query(Table.location)]
    out = []
    for i in db.session.query(Table).all():
        out.append(i.__dict__.values())

    return render_template('result.html', result=out)
