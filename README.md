# desertpy-pelican

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

This uses GitHub Actions and GitHub Pages.

### Setup

Has to be done once.

* Create a SSH key specifically for use as a deploy key.
  * `ssh-keygen -t ed25519 -f $HOME/.ssh/id_ed25519_dpp_dpk -N ""`
* Add `$HOME/.ssh/id_ed25519_dpp_dpk.pub` as a deploy key *with write access*.
* In the GitHub repository secrets, set `GIT_DEPLOY_KEY` to the contents of
  `$HOME/.ssh/id_ed25519_dpp_dpk`
* Add site CNAME to GitHub settings.
* Push to master and check if the pages are deployed correctly.

### Ongoing Workflow

* Push to `master`
