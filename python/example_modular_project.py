#!/usr/bin/env python
# -*- coding: utf-8 -*-

from example_method import *
from ieee830 import *

#------------------------------------------------------------
# example_modular_project.py
# Smart vacuum cleaner
# A fragmentary project documentation
#------------------------------------------------------------


World("My Smart Home")
cd("./-")
System("Vacuum Cleaner")
cd("./-")
Project("Adaptive Control")

cd("/*/Adaptive Control")
Folder("Protocols")
Folder("Specifications")
cd("./-")

IEEE830SRS("Software Requirements for Adaptive Control of Vacuum Cleaner",
           [["Erik Kamsties and Fabian Kneer", "RE Research Group", "FH Dortmund"]],
           {'language': 'english', 'paper': 'a4', 'font': '11pt'})

from _example_modular_project.content.chapter1 import *
from _example_modular_project.content.chapter2 import *

node("/").dump()
node("/").genPDF()
node("/").genHTML(["ref", "ieee830", "plantuml", "istar"])
