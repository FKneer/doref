#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _test_project.structur import *
#------------------------------------------------------------
# example_project.py
# Smart vacuum cleaner
# A fragmentary project documentation
#------------------------------------------------------------

node("/").dump()

node("/").genPDF()
node("/").genHTML(["ref", "ieee830"])
