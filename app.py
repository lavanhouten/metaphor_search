from metaphor_python import Metaphor
from flask import Flask, render_template, request
metaphor = Metaphor("59ae6ec8-0ba7-411b-90a4-da7d2e8f69bd")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mode = 'neural'
    if 'search' in request.form:
        search_term = request.form.get('search')
        mode = request.form.get('mode')
        if mode == 'neural':
            if search_term == '':
                return render_template('index.html', result='', mode=mode)
            else:
                return render_template('index.html', result=metaphor.search(type=mode, query=search_term), mode=mode)
        else:
            if search_term == '':
                return render_template('index.html', result='', mode=mode)
            else:
                return render_template('index.html', result=metaphor.search(type=mode, query=search_term), mode=mode)
    if 'toggle_mode' in request.form:
        mode = request.form.get('mode')
        mode = 'neural' if mode == 'keyword' else 'keyword' if mode == 'neural' else mode
    return render_template('index.html', result='', mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
