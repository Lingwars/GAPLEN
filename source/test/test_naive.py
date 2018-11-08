#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
import nltk
nltk.usage(nltk.classify.ClassifierI)

train = [
     (dict(a=1,b=1,c=1), 'y'),
     (dict(a=1,b=1,c=1), 'x'),
     (dict(a=1,b=1,c=0), 'y'),
     (dict(a=0,b=1,c=1), 'x'),
     (dict(a=0,b=1,c=1), 'y'),
     (dict(a=0,b=0,c=1), 'y'),
     (dict(a=0,b=1,c=0), 'x'),
     (dict(a=0,b=0,c=0), 'x'),
     (dict(a=0,b=1,c=1), 'y'),
     ]
test = [
     (dict(a=1,b=0,c=1)), # unseen
     (dict(a=1,b=0,c=0)), # unseen
     (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
     (dict(a=0,b=1,c=0)), # seen 1 time, label=x
     ]
