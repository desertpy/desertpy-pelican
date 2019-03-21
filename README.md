# desertpy-pelican

[![CircleCI](https://circleci.com/gh/desertpy/desertpy-pelican/tree/master.svg?style=svg)](https://circleci.com/gh/desertpy/desertpy-pelican/tree/master)

DesertPy Webpage Source - Pelican

This is the source to the DesertPy web page ( http://desertpy.com ).

Fork it, improve it, and send a pull request!

## Working on Site

* Clone repo
* Create python 3.7 virtualenv - ``mkvirtualenv desertpy-pelican``
* Install dependencies - ``pip install -r requirements.txt``
* Run development pelican server - ``make serve`` and visit http://localhost:8000
* Make changes

## Publishing

This uses CircleCI.

### Setup

Has to be done once.

* Create a SSH key specifically for use as a deploy key.
  * `ssh-keygen -t ed25519 -f $HOME/.ssh/id_ed25519_dpp_dpk -N ""`
* Add `$HOME/.ssh/id_ed25519_dpp_dpk.pub` as a deploy key *with write access*.
* In CircleCI Environment variables, set `GIT_DEPLOY_KEY_BASE64` to the base64'd
contents of `$HOME/.ssh/id_ed25519_dpp_dpk`
* Add site CNAME to GitHub settings.
* Add repository to CircleCI
* Push to master and check if the pages are deployed correctly.

### Ongoing Workflow

* Push to `master`
* Pages updated hourly from `master` to keep up with meetup.com content.
