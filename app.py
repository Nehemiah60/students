from flask import Flask, render_template, url_for, request, redirect, flash, session
from models import *
from forms import *

#Logging Information about the response
@app.after_request
def responseLogs(response):
    app.logger.info(
        "path: %s | method: %s | status: %s | size: %s",
        request.path,
        request.method,
        response.status,
        response.content_length
    )
    return response
#Home Page
@app.route('/')
def index():
    app.logger.info('User visited the home page')
    return render_template('index.html')
#Add student
@app.route('/students/add', methods=['GET','POST'])
def add_student():
    app.logger.info('Received add student request: %s', request.form)
    form        = StudentForm()
    if form.validate():
        try:
            student = Students(
                first_name  = form.first_name.data,
                second_name = form.second_name.data,
                email       = form.email.data,
                fee_paid    = form.fee_paid.data
            )
            db.session.add(student)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return redirect(url_for('student_list'))
    return render_template('add_student_form.html', form=form)

#List of students
@app.route('/students')
def student_list():
    form    = StudentForm(request.form)
    student = Students.query.all()
    return render_template('add_student_form.html', student=student, form=form)

#Student Details
@app.route('/students/<int:id>')
def student_detail(id):
    student   = db.session.query(Students, Fees).join(Fees, Students.id==Fees.id).filter(Students.id==id).all()
    return render_template('student_detail.html', student=student)

#Update Students
@app.route('/students/<int:id>/update', methods=['GET','POST'])
def update_student(id):
    form = StudentForm(request.form)
    student = Students.query.get_or_404(id)
    if form.validate() and 'image' in request.files:
        student.first_name  = form.first_name.data,
        student.second_name = form.second_name.data,
        student.email       = form.email.data,
        student.fee_paid    += form.fee_paid.data
        student.image       =  request.files['image']

        image  = request.files['image']

        if image:
            try: 
                filename    = image.filename
                image.save(os.path.join('static/images', filename))
                student.image = f'images/{filename}'
                db.session.commit()
            except:
                db.session.rollback()
            finally:
                db.session.close()
            return redirect(url_for('student_list'))
    return render_template('update_student.html',student=student, form=form)

#Delete Students
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
        try:
            student = Students.query.get_or_404(id)
            db.session.delete(student)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return redirect(url_for('student_list'))

if __name__ == '__main__':
    app.run(debug=True)