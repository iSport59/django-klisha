
===============================
klisha - Django-based photoblog
===============================

klisha is a standards-compliant and responsive photoblog web application, 
written in Python and uses the Django web framework.

.. figure:: https://raw.github.com/zenzire/django-klisha/master/docs/images/responsive.png
   :alt: Responsive design


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

* Admin: Added vertical display of the tags' filter interface
* Updating Description, Screenshots and Installation paragraphs in README.rst file (`issue #2 <https://github.com/zenzire/django-klisha/issues/2/>`_) - in progress 

Version 1.0.1 (2013-Aug-05):
  
* Changed upload_to path ffrom 'pictures' to 'klisha/pictures' in Picture model (`issue #9 <https://github.com/zenzire/django-klisha/issues/9/>`_)
* Added links to the next and the previous picture on picture detail page (`issue #4 <https://github.com/zenzire/django-klisha/issues/4/>`_)
* Added KLISHA_WEBSITE_DESCRIPTION optional parameter to settings (`issue #3 <https://github.com/zenzire/django-klisha/issues/3/>`_)
* Added Installation and Release notes paragraphs in README.rst file (`issue #2 <https://github.com/zenzire/django-klisha/issues/2/>`_) - in progress 
 
Version 1.0.0 (2013-Jul-25):

* Initial version


