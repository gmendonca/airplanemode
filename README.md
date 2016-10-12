# Airplane Mode [![Build Status](https://travis-ci.org/gmendonca/airplanemode.svg?branch=master)](https://travis-ci.org/gmendonca/airplanemode)


Right now you need [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed.
You can run like this:

```bash
$ pip install -r requirements.txt
$ export FLASK_APP=runserver.py
$ python -m flask run
```

And test like this:

```bash
$ python tests/views_test.py
```


To deploy on Heroku:

```bash
$ heroku login
$ heroku create
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open
```
