from flask import Flask, render_template, request
import os
import unittest
from collections import defaultdict
from io import StringIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_tests = request.form.getlist("tests")
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        for test in selected_tests:
            suite.addTest(loader.loadTestsFromName(test))

        # Erfassen des Outputs
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)
        test_output = stream.getvalue()

        return render_template("results.html", result=result, output=test_output)

    else:
        # Dynamic loading of all tests
        test_methods = get_test_methods()
        return render_template("index.html", test_methods=test_methods)


def get_test_methods():
    tests_dir = "tests"
    all_tests = defaultdict(list)


    for root, _, files in os.walk(tests_dir):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                module_name = f"{tests_dir}.{file[:-3]}"
                try:
                    module = __import__(module_name, fromlist=[""])
                    # Search for Unittest classes
                    for name in dir(module):
                        obj = getattr(module, name)
                        if isinstance(obj, type) and issubclass(obj, unittest.TestCase):

                            for method_name in dir(obj):
                                if method_name.startswith("test_"):
                                    test_name = f"{module_name}.{name}.{method_name}"
                                    all_tests[file].append(test_name)
                except Exception as e:
                    print(f"Fehler beim Laden von {module_name}: {e}")
    return dict(sorted(all_tests.items()))


if __name__ == "__main__":
    app.run(debug=True)
