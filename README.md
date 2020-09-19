## Django unit test

I created this to study about unit test with django.
In directory **core/tests** contains the unit test that was created

### Requirements
- Pip
- Virtual env

### How to run the project?
- Create a virtual env to the project, you can use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- run in home of project: `pip install -r requirements/common.txt` to install the dependencies

### How to run the unit test?
```
python manage.py test
# or
python manage.py test core.tests
# or 
python manage.py test core.tests.especific_file   Example: python manage.py test core.tests.test_api
# or
python manage.py test core.tests.especific_file.especific_class   Example: python manage.py test core.tests.test_api.TestApi
```
