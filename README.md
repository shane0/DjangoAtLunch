# DjangoAtLunch
This is a very simple message board where you can leave a message and check in and out for things like meetings, lunch, vacation and can also be used to reserve rooms, machines, and other resources.

You can also leave a message like "I'm tentatively out tue-wed" so others can plan accordingly.

It was built for internal use in some medical offices while working at Mercy Hospital Iowa City but I've found it useful anywhere.

![screenshot](https://cloud.githubusercontent.com/assets/1454458/17640339/53507c30-60b2-11e6-9f20-17f679ab3def.PNG)

## Installation

- download to your existing django site

- add to /settings.py INSTALLED_APPS

```python
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
- [ ] seperate boards for departments
- [ ] moment.js with days until / days since
- [ ] calendar with scheduling
