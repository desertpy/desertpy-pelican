#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://desertpy.com'

DELETE_OUTPUT_DIRECTORY = True

THEME = "themes/subtle"
RELATIVE_URLS = False
GOOGLE_ANALYTICS = 'UA-39513587-1'
DISQUS_SITENAME = "desertpy"

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
