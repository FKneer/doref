#!/usr/bin/env python
# -*- coding: utf-8 -*-

from example_method import *
from plantuml import *
#------------------------------------------------------------
# example_project.py
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


cd("/*/Specific Requirements")

Chapter("Customer Requirements")
cd("./-")

Req("Clean at night",
    "The robot shall clean the appartment at night.",
    {'Priority': 1,
     'Effort': 20,
     'Optional': 1})

Req("Power",
    "The suction power must not exceed a given threshold.",
    {'Priority': 1})


Req("Silence", "The operation of the vacuum cleaner should be as silent as possible.",
    {'Priority': 2,
     'Trace': [node("./*/Power"), node("./*/Clean")]})
cd("./-")
Inf("The vacuum cleaner should not disturb the persons living in the apartment.")
cd("..")

Figure("RE - World, Documents, and Workflows", './_example_project/model.png',
       "This figure shows the main corner stones of RE.",
       {'size': 'fit'})


Table("Characteristics of good requirements",
      [
          ['Characteristic', 'Explanation'],
          ['Complete', 'The requirement is fully stated in one place with no missing information.',
           'Consistent', 'The requirement does not contradict any other requirement and is fully consistent with '
                         'all authoritative external documentation.']
      ], "The characteristics of good requirements are variously stated by different writers, with each writer "
         "generally emphasizing the characteristics most appropriate to their general discussion or the specific "
         "technology domain being addressed. However, the following characteristics are generally acknowledged")


cd("/*/Specific Requirements")

Chapter("Models")
cd("./-")

PlantUML("UML Example","""
Alice -> Bob: A
Bob --> Alice: B
Alice -> Bob: C
Bob --> Alice: D
""", "Example: plantUML Seq-Diagramm")


GenericModel("States of a Traffic Light", "This model shows the states of a traffic light in Germany.")
cd('./-')
Circle("Red")
Circle("Red-yellow")
Circle("Green")
Circle("Yellow")

Arrow(node('./*/Red'), node('./*/Red-yellow'))
Arrow(node('./*/Red-yellow'), node('./*/Green'))
Arrow(node('./*/Green'), node('./*/Yellow'))
Arrow(node('./*/Yellow'), node('./*/Red'))

node("/").dump()

node("/").genPDF()
node("/").genHTML(["ref", "ieee830"])














