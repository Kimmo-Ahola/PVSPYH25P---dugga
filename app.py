from flask import Flask, render_template, request

app = Flask(__name__)

# exercise 2.1, do not touch before
@app.route('/user/<int:user_id>')
def user_detail(int: id):
    users: list["Customer"] = get_random_users()
    user: Customer = None
    for u in users:
        if u.id == user_id:
            user = u
            break
    return render_template('user_detail.html', user=user)
