 Creating Interfaces - Tulcea Tool
=========================================

This Citizen Science data collection tool was developed within the <a target="_blank" href="https://creatinginterfaces.eifer.kit.edu/">Creating Interfaces</a> project and is running with [wq framework]. 

The project was initialized with
```
wq start TulceaTool . -d creatinginterfaces.demo.52north.org --with-gis
```  
which creates a completely new project based on the [wq standard template].  
Note that the command has changed to `wq create` (https://wq.io/wq.create/create) in a newer version of wq.

See [Getting Started] for general information on how to build/run a wq-based application.

### How to develop locally

* Clone the git repository: `git clone https://github.com/52North/tulcea-tool.git`.
* Go to project root: `cd tulcea-tool`
* Install Python libraries: `python -m pip install -r requirements.txt` (optionally activate virtual environment before this step)
* Change the file `db/TulceaTool/settings/dev.py` to:
  ```python
  import os
  import sys
  from .base import *
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = <my-secret-key>

  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = True

  # wq: Determine if we are running off django's testing server
  DEBUG_WITH_RUNSERVER = 'manage.py' in sys.argv[0]

  ALLOWED_HOSTS = ["localhost"]

  # Database
  # https://docs.djangoproject.com/en/2.0/ref/settings/#databases

  DATABASES = {
      'default': {
          'ENGINE': 'django.contrib.gis.db.backends.spatialite',
          'NAME': os.path.join(BASE_DIR, 'conf', 'TulceaTool.sqlite3'),
      }
  }

  SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'
  ```
* Change the base url in `app/js/TulceaTool/config.js` from `'base_url': '/tulcea-tool'` to `'base_url': ''`
* Change the base url in `db/TulceaTool/context_processors.py` from `return {'rt': '/tulcea-tool'}` to `return {'rt': ''}`
* Change the media url in `db/TulceaTool/settings/base.py` from `MEDIA_URL = '/tulcea-tool/media/'` to `MEDIA_URL = '/media/'`
* Run migrations (create data base tables and prepopulate some of them) and create superuser via   
  `cd db/`   
  `./manage.py migrate`  
  `./manage.py createsuperuser`  
  `cd ..`
* Generate htdocs folder via  
  `./deploy.sh 0.0.1`  
  Note: the part where templates are updated is commented as this would overwrite changes.
* Run tool on localhost:8000 via  
  `./db/manage.py runserver`
  
### Deployment on a public server

To deploy the tool on a public server visit wq`s official website ([wq pulic server]).

A setup using Apache HTTP Server, PostgreSQL and Docker/Docker Compose can be found here:  
https://github.com/52North/creating-interfaces

[wq framework]: http://wq.io/
[Getting Started]: https://wq.io/docs/setup
[wq standard template]: https://github.com/wq/wq-django-template
[wq public server]: https://wq.io/guides/setup-wq-with-apache-postgresql


Funding organizations/projects
-------

The development of tulcea-tool was supported by several organizations and projects. Among other we would like to thank the following organisations and project

| Project/Logo | Description |
| :-------------: | :------------- |
| <a target="_blank" href="https://creatinginterfaces.eifer.kit.edu/"><img alt="Creating Interfaces - capacity building for the urban food-water-energy (FWE) -nexus" align="middle" width="250" src="https://creatinginterfaces.eifer.kit.edu/wp-content/uploads/2018/06/logo_creating-interfaces_250x104.png"/></a><a target="_blank" href="https://ec.europa.eu/programmes/horizon2020/en/home"><img alt="This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 730254" align="middle" width="1000" src="https://creatinginterfaces.eifer.kit.edu/wp-content/uploads/2018/06/logo_eu-600x160.png"/></a> | The development of this version of tulcea-tool was supported by the <a target="_blank" href="https://ec.europa.eu/programmes/horizon2020/en/home">European Union's Horizon 2020 research and innovation programme</a> (grant agreement No 730254) within the research project <a target="_blank" href="https://creatinginterfaces.eifer.kit.edu/">Creating Interfaces</a>. |
