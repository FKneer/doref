#!/usr/bin/env python
# -*- coding: utf-8 -*-


from example_method import *
from plantuml import *

w = World("My Smart Home")
cd("./-")
s = System("Vacuum Cleaner")
cd("./-")
p = Project("Adaptive Control")

cd("/*/Adaptive Control")
Folder("Protocols")
Folder("Specifications")
cd("./-")

IEEE830SRS("Software Requirements for Adaptive Control of Vacuum Cleaner",
           [["Erik Kamsties and Fabian Kneer", "RE Research Group", "FH Dortmund"]],
           {'language': 'english', 'paper': 'a4', 'font': '11pt'})

cd("/*/Specific Requirements")

Chapter("Customer Requirements")
Chapter("Models")


from _test_project.chapter1 import *
from _test_project.chapter2 import *



