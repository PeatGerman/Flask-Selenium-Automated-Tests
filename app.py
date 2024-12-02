# app.py

from flask import Flask, render_template, request
import unittest
from io import StringIO
from tests.test_login import TestLogin

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_tests = request.form.getlist('tests')
        #  Dynamically create a TestSuite based on the selected tests
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        for test_name in selected_tests:
            suite.addTest(TestLogin(test_name))

        # Execute tests and record output
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)
        test_output = stream.getvalue()

        return render_template('results.html', result=result, output=test_output)
    else:
        # Retrieve all test methods from the TestLogin class
        test_methods = [method for method in dir(TestLogin) if method.startswith('test_')]
        return render_template('index.html', test_methods=test_methods)

if __name__ == '__main__':
    app.run(debug=True)
