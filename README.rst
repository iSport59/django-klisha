===============================
klisha - Django-based photoblog
===============================

klisha is a standards-compliant photoblog web application, written in Python 
and uses the Django web framework.


Installation
============

Create a virtualenv
-------------------

::

    ~$ virtualenv ~/django-klisha
    ~$ cd ~/django-klisha
    ~$ source ./bin/activate

Clone the code
--------------

::

    ~$ git clone https://github.com/zenzire/django-klisha.git

Install required pip packages
-----------------------------

::
    
    (django-klisha):~$ cd django-klisha/klisha
    (django-klisha):~/django-klisha$ pip install -r requirements.txt

Launch the server
-----------------

::

    (django-klisha):~/django-klisha$ python manage.py runserver 0.0.0.0:8080



klisha-powered sites
--------------------

* http://www.mierzejewski.net - Captured Moments


Release notes
-------------

Version 1.1.0 (unreleased):

* in progess

Version 1.0.1 (2013-Aug-05):
  
* #9 Change upload_to path for pictures from 'pictures' to 'klisha/pictures'
* #4 Add next and previous picture navigation to picture detail page
* #3 Add KLISHA_WEBSITE_DESCRIPTION parameter enhancement
* #2 Update README.rst file (installation manual, demo version, etc) - in progress
 
Version 1.0.0 (2013-Jul-25):

* Initial version
