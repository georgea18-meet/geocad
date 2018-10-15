from flask import render_template, request, redirect, url_for
from flask_login import login_required

from . import app
from project import db
from project.models import Project, Message

hebrew_letters = ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','ך','כ','ל','ם','מ','ן','נ','ס','ע','ף','פ','ץ','צ','ק','ר','ש','ת']

def get_hebrew_word(s):
	w = s.split(",")
	word = ""
	for l in w:
		if int(l) >= 128:
			print(str(int(l)-128))
			word+=hebrew_letters[int(l)-128]
		else:
			word+=chr(int(l))
		print(word)
	return word

def check_if_ascii(s):
	l = s.split(",")
	c = 0
	for n in l:
		if not n.isdigit:
			c+=1
	if c == 0:
		return True
	else:
		return False

def get_word(s):
	word=''
	for l in s:
		if l in hebrew_letters:
			word+=str(hebrew_letters.index(l)+128)+','
		else:
			word+=str(ord(l))+','
	word=word[0:-1]
	print(word)
	return word

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
	projects = Project.query.all()
	for p in projects:
		if check_if_ascii(p.name):
			p.name = get_hebrew_word(p.name)
		if check_if_ascii(p.month):
			p.month = get_hebrew_word(p.month)
		if check_if_ascii(p.description):
			p.description = get_hebrew_word(p.description)
	return render_template('projects.html', projects=projects)

@app.route('/contact-us')
def contact():
	return render_template('contact.html')

@app.route('/leave-message', methods=['GET','POST'])
def message():
	if request.method == 'POST':
		msg = Message()
		msg.email = request.form.get('email')
		msg.message = get_word(request.form.get('message'))
		db.session.add(msg)
		db.session.commit()
		return redirect(url_for('contact'))
	else:
		return render_template('leave_message.html')


@app.route('/private')
@login_required
def private_route():
    return render_template('private.html')
