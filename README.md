# The way to become Silk-ish!


The idea is to get the symptoms from the patients, MD students or doctors and present them the probable results. The workflow consisted of three parts; Front-end, Machine learning and Back-end part.



### Front-end ###
**Maryam Abbasi**



For this part and restyling the html pages Bootstrap v4.4 was used. Since it is a free and open-source CSS framework directed at responsive and contains HTML, CSS and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.


- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -

### Machine learning ###
**Parsa Hariri**


**Introduction**


This code is a machine learning model for diagnosing diseases based on patient symptoms. The data for training the model is a CSV file stored on Google Drive, and the model uses the Decision Tree algorithm from the scikit-learn library.


**How it Works**

The model uses two functions: makeTheTree and findDesesFromSymptom.

  * MakeTheTree: This function loads the training data from Google Drive, prepares it for the model, trains the model using Decision Tree, and returns the trained model.

  * FindDesesFromSymptom: This function takes user input of symptoms as a comma-separated string, prepares it for prediction, and returns the predicted disease.


**Dependencies**

This code uses the following libraries:

* logging

* pandas

* numpy

* scikit-learn

* graphviz (commented out in the code)

* Usage

To use the code, call the findDesesFromSymptom function with the symptoms input and it will return the predicted disease.


**Note**

The code has some commented-out lines for logging and graph visualization. It also has some TODO comments indicating possible changes in the future.

- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - -- - - 
### Back-end ###
**Amirreza Aleyasin**

* Tasks done:
Handling django project backend and coding all required files including:
Models.py: user profiles, resports and inputs.
managers.py: custom management to handle custom user model.
test.py: testing usermodel.
forms.py: required to maniupulate Data Base from FrontEnd
urls.py: web urls to handle pages and to initiate functions from views.py.
views.py: initiating the functions and passing objects from database to the front end.
settings.py: required settings for django-apps.


#### Installing

Step by step commands on how to run this project on your computer

1)- Install Virtualenv

```
pip install virtualenv
```

2)- Create Virtualenv

```
virtualenv venv
```

3)- Activate virtual env

```
venv/Scripts/activate
```

4)- Install requirements

```
pip install -r requirements.txt
```
Note: Above lines are required for first time installation

5)- Execute below commands

```
python manage.py makemigrations
python manage.py migrate
```
Note: Above commands should be executed if there is any db level changes

6)- Create superuser for admin access and follow instruction, if not created one

```
python manage.py createsuperuser
```

<br>

#### Running the tests

```
python manage.py runserver
```
And the project is ready for use on your computer!

<br>
