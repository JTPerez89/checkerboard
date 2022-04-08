from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def basic():
    return render_template('index.html', across=8, down=8, color1='red', color2='black')


@app.route('/<down>')

def one_dimension(down):
    down = int(down)
    return render_template('index.html', across=8, down=down, color1='red', color2='black')


@app.route('/<down>/<across>')

def two_dimension(down, across):
    down = int(down)
    across = int(across)
    return render_template('index.html', across=across, down=down, color1='red', color2='black')


@app.route('/<down>/<across>/<color1>/<color2>')

def two_dimension_color(down, across, color1, color2):
    down = int(down)
    across = int(across)
    return render_template('index.html', across=across, down=down, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)