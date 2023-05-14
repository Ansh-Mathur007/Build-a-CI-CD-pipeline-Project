from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    if request.method == 'POST':
        workout = request.form['workout']
        return render_template('workouts.html', workout=workout)
    else:
        return render_template('workouts.html')

if __name__ == '__main__':
    app.run()
