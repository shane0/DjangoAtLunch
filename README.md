# DjangoAtLunch
This is a very simple message board where you can leave a message and check in and out for things like meetings, lunch, vacation and can also be used to reserve rooms, machines, and other resources.

It was built for internal use in some medical offices while working at Mercy Hospital Iowa City but I've found it useful anywhere.

![screenshot](https://cloud.githubusercontent.com/assets/1454458/17639979/5006aea0-60ad-11e6-8aed-a49767b2beb8.PNG)

## Installation

- DOWNLOAD

- add to /settings.py INSTALLED_APPS

'''python
    'inoutboard',
```

- add to /urls.py urlpatterns

```python
url(r'^board/', include('inoutboard.urls')),
```

## Usage

Admin administers users, there is only view which is anonymous for convenience so anyone can update the page.

Added google's mdl template.

Features

- [x] anonymous message board
- [ ] non-anonymous mode
- [ ] seperate views for departments
- [ ] add some scheduling and durations using moment.js
