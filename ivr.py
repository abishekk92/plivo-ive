import os

from flask import Flask, render_template, request, redirect, url_for, session

ivr = Flask(__name__)
ivr.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



@ivr.route('/', methods=['GET', 'POST'])
def index():
	error_1 = None
	error_2 = None
	if request.method == 'POST':
		try:
			session['levels'] = int(request.form['levels'])
		except ValueError, e:
			error_1 = 'Please enter a numeric value'
		if error_1:	
			return render_template('index.html', 
								   error_1=error_1)
		return redirect(url_for('menu'))
		
	return render_template('index.html')

@ivr.route('/menu', methods=['GET', 'POST'])
def menu():
	errors = None
	if request.method == 'POST':
		try:
			actions =  [(i, range(1, 1+int(j))) for i, j in sorted(request.form.items())]
		except ValueError, e:
			levels = range(1, 1+session['levels'])
			errors = 'Please specify only numeric integer values'
			return render_template('sub_menus.html', 
									levels=levels,
									errors=errors)
		
		session['actions'] = actions
		session['count'] = 0
		return redirect(url_for('num_of_action'))

	levels = range(1, 1+session['levels'])

	return render_template('sub_menus.html', levels=levels, errors=errors)

@ivr.route('/num_of_action', methods=['GET', 'POST'])
def num_of_action():
	if request.method == 'POST':
		print request.form
	return render_template('actions.html')



if __name__ == '__main__':

	ivr.run(debug=True)