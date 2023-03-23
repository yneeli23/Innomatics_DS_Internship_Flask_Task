from flask import Flask, request, render_template
import re


app = Flask(__name__)

'''-------------------------------------------------------------'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regex', methods=['POST'])
def regex():
    if request.method == 'POST':
        test_str = request.form['test_str']
        pattern = request.form['pattern']

        if not test_str or not pattern:
            return render_template('failure.html')

        matched = re.findall(pattern, test_str)

        return render_template('success.html', matched = matched)
    
'''------------------------------------------------------------------'''

if __name__ == '__main__':
    app.run(debug=True)