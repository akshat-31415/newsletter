from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def save_email_to_db(email):
    conn = sqlite3.connect('email.db')
    c=conn.cursor()
    try:
        c.execute('INSERT INTO subscribers (email) VALUES (?)',(email,))
        conn.commit()
        print(f"[INFO] Saved email: {email}")
    except sqlite3.IntegrityError:
        print("Email already subscribed.")
    finally:
        conn.close()
        print(":( :( ")

def get_all_subscribers():
    conn = sqlite3.connect('email.db')
    c = conn.cursor()
    c.execute('SELECT id, email FROM subscribers')
    subscribers = c.fetchall()
    conn.close()
    return subscribers

def delete_subscriber(email_id):
    conn = sqlite3.connect('email.db')
    c = conn.cursor()
    c.execute('DELETE FROM subscribers WHERE id = ?', (email_id,))
    conn.commit()
    conn.close()

@app.route('/')
def subscribe():
    return render_template('subscribe.html')

@app.route('/submit',methods=['POST'])
def submit():
    email = request.form.get('email')
    if email:
        save_email_to_db(email)
        return render_template('success.html',email=email)
    return redirect(url_for('subscribe'))

@app.route('/admin')
def admin():
    subscribers = get_all_subscribers()
    return render_template('admin.html',subscribers=subscribers)

@app.route('/delete/<int:email_id>')
def delete(email_id):
    delete_subscriber(email_id)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)