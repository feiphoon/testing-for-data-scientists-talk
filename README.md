# Testing for Data Scientists: A quick start!

This is a repo containing all you need to set up a playground for `doctest` and `pytest`.

They are two separate approaches to writing unit tests, and you don't have to have 
both in your code. This is just for you to check out the limitations, possibilities 
and quirks of both, and for you to see how to set them up yourself.

I hope the examples are useful as a reference, and I've included plenty of cool commands
to run the tests in different ways. Because I want to demonstrate the evolution of these 
test functions, there are test functions with the same names in the files. If this is 
the case, `pytest` will only run the first one it finds based on the name.
So to run everything correctly, remember to comment out previous duplicate test functions.

You can examine a comparison of `pytest` and `unittest` modules here:
<https://github.com/renzon/pytest-vs-unittest>. The `pytest` examples in that repo 
come from this book: <https://www.oreilly.com/library/view/python-testing-with/9781680502848/>

To give feedback or ask questions, please open an issue on this repo.


## Setup

`git clone` this repo so you can run it locally.


### Virtualenv

Having a virtual environment gives you a self-contained space to reproduce your project with the right modules. `virtualenv` is the simplest way toward this, but if you already use something else like `pipenv`, `poetry` or Docker, you're probably a virtual environment pro and you can skip this entire section. 

#### Create your new virtual environment

```
pip install virtualenv
cd testing_talk # your project folder
python3 -m virtualenv venv # Where venv is the name of your new environment
```

#### Start your new environment

```
source venv/bin/activate
```

As it's a new environment, you want to install the packages you need in that environment:
```
pip install pytest
pip install jupyter

# OR

pip install pytest jupyter # multiple packages at once
```

#### Make sure your environment is reproducible

Record what was installed in your environment. View the packages installed in this environment `venv`:
```
pip list
```

You'll see your newly-installed packages, along with their dependency packages, and everything has a version. Now record what you installed in this environment:
```
pip freeze > requirements.text
```
This creates a `requirements.txt` file where you can view everything and recreate your environment easily next time. This is not an autosave process, so if you install a new package in this environment, make sure to run this again.

#### Exit your environment

```
deactivate
```

#### Recreating your environment elsewhere

Let's say your environment is broken or lost. You can emulate this by deleting the `venv` folder you created (it's in there!)

You can still recreate exactly the same environment (named horribly here as `new_venv`) by using your `requirements.txt` that you wisely made earlier:

```
python3 -m virtualenv new_venv
source new_venv/bin/activate
pip install -r requirements.txt
```

You can even pass this `.txt` file on to a friend and they can run these above commands to have the same environment you had. This means that if you pass on some code or a Jupyter notebook to them, you can ensure that they can replicate the same conditions you had, to run your project.


## Running tests

### `doctest`

Run `doctest` on the docstring tests in `math_functions.py`.
```
python -m doctest math_functions.py -v
```

### `pytest`

Run all tests:
```
py.test
# OR
pytest
```

Run tests for a specific file, where `test_math_functions.py` is named to match the file you want to test, `math_functions.py`.
```
pytest tests/test_math_functions.py
```

Verbose mode with `-v`, is always optional but gives you more information about test results.
```
pytest -v tests/test_math_functions.py 
```

Run a set of tests based on the test name (so you should always name your tests well!).
Here we want to only run tests whose names contain the keyword "error".
```
pytest -k error
# OR
pytest -v -k error
```

Run a group of tests. You need to have applied some Test Classes:
```
pytest tests/test_math_functions.py::TestDivision
```

You can run a specific method inside a Test Class too:
```
pytest tests/test_math_functions.py::TestDivision::test_division_zero_division_error
```

You can inspect how and in what order your fixtures are set up, by adding the `--setup-show` argument:
```
pytest -v --setup-show tests/test_dictionary_functions.py
```


## `pytest` AND `doctest`:

Run both together! The `-v` or verbosity option is not required, but makes it a lot more satisfying.
```
pytest -v --doctest-modules
```