#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://huongnhdh.github.io/blog/'

RELATIVE_URLS = False

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-131511951-1"
STATIC_PATHS = ['extra', 'images']
# STATIC_PATHS = ['extra/favicon.ico']
# EXTRA_PATH_METADATA = {
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }