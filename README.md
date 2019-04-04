# zrl
URL Redirector

## Views
- Homepage (also receives POSTs of new redirects)
  -> Shows hot clicks (last 24 hours)
  -> Shows a list of last 15 created redirects

- /<slug> (redirects to target)
- URL Cloud (shows all slugs)
- /zrl_edit/<slug> (edit a slug)
- /zrl_view/<slug> (view a slug, and its stats)
  
## Features
- Public, unlisted, or private URLs
- Stores data using SQLAlchemy


## Models

URL
  - Scope (public/unlisted/private)
  - Slug (must be unique for public/unlisted)
  - Target
  - Created On
  - Delete On (null=True)
  
URLEdit
   - URL (Foreign Key)
   - EditedOn
   - Old Target
   - New Target
   - Edited By (Text Field)
   
Hit
   - URL (Foreign Key)
   - DateTime
   - SourceIP
   - 
Forms library for Flask
https://flask-wtf.readthedocs.io/en/stable/

SQLAlchemy library for Flask
http://flask-sqlalchemy.pocoo.org

Schedule tasks for deletion:
https://stackoverflow.com/questions/21214270/scheduling-a-function-to-run-every-hour-on-flask/38501429#38501429

Possible Caching for real-time stats? 
http://flask.pocoo.org/docs/1.0/patterns/caching/
