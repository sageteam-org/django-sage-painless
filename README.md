# Django Sage Painless

The [django-sage-painless](https://github.com/sageteam-org/django-sage-painless) is a valuable package based on Django Web Framework & Django Rest Framework for high-level and rapid web development. The introduced package generates Django applications. After completing many projects, we concluded that any basic project and essential part is its database structure. You can give the database schema in this package and get some parts of the Django application, such as API, models, admin, signals, model cache, setting configuration, mixins, etc. All of these capabilities come with a unit test. So you no longer have to worry about the simple parts of Django, and now you can write your advanced services in Django. The django-sage-painless dramatically speeds up the initial development of your projects. Documentation of this package is available in [readthedocs](https://django-sage-painless.readthedocs.io/).

## Vision

However, we intend to make it possible to use it in projects that are in-progress.

## Why Painless

We used the name painless instead of the Django code generator because this package allows you to reach your goals with less effort.

&nbsp;

![SageTeam](https://github.com/sageteam-org/django-sage-painless/blob/develop/docs/images/tag_sage.png?raw=true "SageTeam")

![PyPI release](https://img.shields.io/pypi/v/django-sage-painless "django-sage-painless")
![Supported Python versions](https://img.shields.io/pypi/pyversions/django-sage-painless "django-sage-painless")
![Supported Django versions](https://img.shields.io/pypi/djversions/django-sage-painless "django-sage-painless")
![Documentation](https://img.shields.io/readthedocs/django-sage-painless "django-sage-painless")

- [Project Detail](#project-detail)
- [Git Rules](#git-rules)
- [Get Started](#getting-started)
- [Usage](#usage)
- [Contribute](#contribute)

## Project Detail

- Version: 0.3.2
- Language: Python > 3.6
- Framework: Django > 3.1

## Git Rules

S.A.G.E. team Git Rules Policy is available here:

- [S.A.G.E. Git Policy](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## Getting Started

Before creating Djagno project you must first create virtualenv.

``` shell
$ python3.9 -m pip install virtualenv
$ python3.9 -m virtualenv venv
```

To activate virtualenvironment in ubuntu:

```shell
$ source venv/bin/activate
```

To deactive vritualenvironment use:

``` shell
$ deactivate
```

## Start Project

First create a Django project

```shell
$ mkdir GeneratorTutorials
$ cd GeneratorTutorials
$ django-admin startproject kernel .
```

## Install Generator

First install package

```shell
$ pip install django-sage-painless
```

Then add 'sage_painless' to INSTALLED_APPS in settings.py

**TIP:** You do not need to install the following packages unless you request to automatically generate an API or API documentation.

However, you can add following apps in your INSTALLED_APPS:

- 'rest_framework'
- 'drf_yasg'
- 'django_seed'

```python
INSTALLED_APPS = [
  'sage_painless',
  'rest_framework',
  'drf_yasg',
  'django_seed',
]
```

## Usage

To generate a Django app you just need a diagram in JSON format. diagram is a json file that contains information about database tables.

[Diagram examples](sage_painless/docs/diagrams)

start to generate
(it is required for development. you will run tests on this app)

```shell
$ python manage.py generate --diagram <path to diagram>
```

Here system will ask you what you want to generate for your app.

If you generated api you have to add app urls to urls.py:

```python
urlpatterns = [
  path('api/', include('products.api.urls')),
]
```

- You have to migrate your new models

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

- You can run tests for your app

```shell
$ python manage.py test products
```

- Django run server

```shell
$ python manage.py runserver
```

- Rest API documentation is available at `localhost:8000/api/doc/`
  
- For support Rest API doc add this part to your urls.py

```python
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Rest API Doc",
        default_version='v1',
        description="Auto Generated API Docs",
        license=openapi.License(name="S.A.G.E License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('api/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
]
```

- Rest API documentation is available at `localhost:8000/api/doc/`

## How to Contribute

Run project tests before starting to develop

- `products` app is required for running tests

```shell
$ python manage.py startapp products
```

```python
INSTALLED_APPS = [
  'products',
]
```

- you have to generate everything for this app
  
- diagram file is available here: [Diagram](sage_painless/tests/diagrams/product_diagram.json)

```shell
$ python manage.py generate --diagram sage_painless/tests/diagrams/product_diagram.json
```

- run tests

```shell
$ python manage.py test sage_painless
```

## Team
| [<img src="https://github.com/sageteam-org/django-sage-painless/blob/develop/docs/images/sepehr.jpeg?raw=true" width="230px" height="230px" alt="Sepehr Akbarzadeh">](https://github.com/sepehr-akbarzadeh) | [<img src="https://github.com/sageteam-org/django-sage-painless/blob/develop/docs/images/mehran.png?raw=true" width="225px" height="340px" alt="Mehran Rahmanzadeh">](https://github.com/mrhnz) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Sepehr Akbarazadeh Maintainer](https://github.com/sepehr-akbarzadeh)                                                                                                             | [Mehran Rahmanzadeh Maintainer](https://github.com/mrhnz)                                                                                                       |