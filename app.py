from flask import Flask, render_template, redirect, url_for, request, session
from program import is_running, start_pgm, stop_pgm
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['HC_secret']


@app.route('/', methods=['GET', 'POST'])
def index():
    programs = ('netflix', 'spotify', 'thunderbird', 'ryver', 'xed')
    for program in programs:
        if is_running(program):
            session[program] = True
        else:
            session[program] = False
    return render_template('main.html')


@app.route('/start/<string:pgm>/')
def start(pgm):
    start_pgm(pgm)
    session[pgm] = True
    return redirect(url_for('index'))


@app.route('/stop/<string:pgm>/')
def stop(pgm):
    session[pgm] = False
    pgm = 'chrome' if pgm == 'netflix' else pgm
    stop_pgm(pgm)
    # Make sure the application is closed before redirecting
    time.sleep(0.5)
    return redirect(url_for('index'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
