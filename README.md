# flask-demo-app
Flask based application that uses FinnKino and Leffatykki API

[![Build Status](https://travis-ci.org/Atihinen/flask-demo-app.svg?branch=master)](https://travis-ci.org/Atihinen/flask-demo-app)

# Requirements

* python 3
* pip for python 3
* chrome or firefox
  * chromedriver for chrome
  * geckodriver for firefox

# Installation

* `git clone <this repo>`
* `pip install -r requierments.txt`

# Running unittests
* `nosetests unittests`

# Running acceptance tests
* Install firefox with working geckodriver https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu
* Run command `cd acceptance_tests ; robot api.robot`

# Starting the server

* `python app.py`
