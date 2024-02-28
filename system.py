from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

users = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            return "Username already taken! Please choose another one."
        users[username] = 0
        users['robot'] = 0
        return redirect(url_for('game', username=username))
    return render_template('index.html')


@app.route('/game/<username>')
def game(username):
    return render_template('game.html', username=username, users=users)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/roll_dice/<username>')
def roll_dice(username):
    user_roll = random.randint(1, 6)
    if users[username]<25:
        users[username] += user_roll
    if users[username] == 25:
        return f"{username} wins!"
    robot_roll = random.randint(1, 6)
    if users['robot'] < 25:
        users['robot'] += robot_roll
    if users['robot'] == 25:
        return "Robot wins!"
    return redirect(url_for('game', username=username))


if __name__ == '__main__':
    app.run(debug=True)
