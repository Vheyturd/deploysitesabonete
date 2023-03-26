from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

# Obter o endereço de e-mail do destinatário da variável de ambiente
app = Flask(__name__)
app.secret_key = '1fbfb34e40e89ba87fbe58d813dcffe9'

# Configurações do Flask-Mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'emaildeteste439@gmail.com'
app.config['MAIL_PASSWORD'] = 'wmjvoxwejdslxenj'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    msg = Message('Novo contato', sender='emaildeteste439@gmail.com', recipients=[email])
    msg.body = f'Nome: {name}\nEmail: {email}'
    try:
        mail.send(msg)
        flash('Mensagem enviada com sucesso!', 'success')
    except:
        flash('Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde.', 'error')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)