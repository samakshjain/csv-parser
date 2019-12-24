# CSV Parser written in Django

### Installation

Ensure that you are using Python 3.x.y

Setup a virtualenv and install the dependencies from `requirements.txt`


### Run

Run migrations before running the app:
```bash
$ python manage.py migrate

$ python manage.py runserver
```

To populate the data run:

```bash
$ python manage.py gen <path-to-csv-file>
```

Navigate to `http://localhost:8000/data/` to see the data in action


### Screens


![Demo](demo.gif)
