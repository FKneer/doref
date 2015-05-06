#!/usr/bin/env python
# -*- coding: utf-8 -*-

from example_method import *
from gui import *
from plantuml import *
#------------------------------------------------------------
# example_project.py
# Smart vacuum cleaner
# A fragmentary project documentation
#------------------------------------------------------------

# Example RE Sceanrio: Stakeholder have conflicts

w = World("My Smart Home")
a = System("A", w)
b = System("B", w)
c = System("C", w)
A1 = System("A1",a)
A2 = System("A2",a)
B1 = System("Vacuum Cleaner", b)
B11 = System("B11",B1)
C1 = System("C1",c)

p1 = Project("Adaptive Control", B1)
p2 = Project("Project Test",p1)

cd("/*/Adaptive Control")
Folder("Protocols")
Folder("Specifications")
cd("./-")
IEEE830SRS("Software Requirements for Adaptive Control of Vacuum Cleaner",
           [["Erik Kamsties and Fabian Kneer", "RE Research Group", "FH Dortmund"]],
           {'language': 'german', 'paper': 'a4', 'font': '11pt'})

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

Inf("Porto (port. Aussprache ['poɾtu]) ist die "
    "Hauptstadt des gleichnamigen Distriktes in "
    "Portugal und liegt am Douro vor dessen Mündung "
    "in den Atlantischen Ozean. Mit circa 237.000 Einwohnern "
    "(port. portuenses; dt. Portuenser genannt) ist sie "
    "nach Lissabon und ihrer Nachbarstadt Vila Nova de Gaia "
    "die drittgrößte Stadt des Landes. ")

Inf('''Der rund 1,29 Millionen[3]
    Einwohner zählende Ballungsraum Grande Porto rangiert
    landesweit jedoch an zweiter Stelle. Porto ist eine der ältesten
    europäischen Städte, sie wird gern als die „Hauptstadt
    des Nordens“ bezeichnet.''')

Figure("RE - World, Documents, and Workflows", './_example_project/model.png',
       "This figure shows the main corner stones of RE.",
       {'size': 'fit'})
Table("Actor Description",
      [
          ['Term', 'Description'],
          ['Customer-Relationship-Management',
           'Customer-Relationship-Management, kurz CRM (dt. Kundenbeziehungsmanagement) '
           'oder Kundenpflege, bezeichnet die konsequente Ausrichtung einer '
           'Unternehmung auf ihre Kunden und die systematische Gestaltung der '
           'Kundenbeziehungsprozesse. Die dazugehörende Dokumentation und Verwaltung '
           'von Kundenbeziehungen ist ein wichtiger Baustein und ermöglicht ein '
           'vertieftes Beziehungsmarketing.  ']
      ], "This table defines some terms.")

cd("/*/Specific Requirements")
Chapter("Models")
cd("./-")
GenericModel("States of a Traffic Light ä ü ö ß", "This model shows the states of a traffic light in Germany.")
cd('./-')
Circle("Red")
Circle("Red-yellow")
Circle("Green")
Circle("Yellow")

Arrow(node('./*/Red'), node('./*/Red-yellow'))
Arrow(node('./*/Red-yellow'), node('./*/Green'))
Arrow(node('./*/Green'), node('./*/Yellow'))
Arrow(node('./*/Yellow'), node('./*/Red'))


#TODO delete Test REQ
cd("/*/Customer Requirements")
Req("Test: Bold Italic Itemize", '''

**bold**

(**bold**)
[**bold**]
{**bold**}

**bold**.
**bold**,
**bold**:
**bold**;
**bold**!
**bold**?

A**bold**
**bold**B
A**bold**B

** bold**
**bold **
** bold **

**bold over
-----------
-----------
-----------
-----------
-----------
-----------
-----------
two lines**



*italic*

(*italic*)
[*italic*]
{*italic*}

*italic*.
*italic*,
*italic*:
*italic*;
*italic*!
*italic*?

A*italic*
*italic*B
A*italic*B

*italic *
* italic*
* italic *

*italic over
-----------
-----------
-----------
-----------
-----------
-----------
-----------
two lines*



**bold and italic**

** bold and italic**
**bold and italic **
** bold and italic **

**bold and italic
-----------
-----------
-----------
-----------
-----------
-----------
-----------
over tow lines**



* *italic*
* **bold**
* A * B + C * F = 12

* 1
 * 2
  * 3
   * 4
* 1
 * 2
  * 3
 * 2
  * 3
   * 4

Implicit Hyperlink Targets -> Reference to a Chapter, see `/*/Customer Requirements`_
Implicit Hyperlink Targets -> Reference to a Node, see `/*/Power`_


External hyperlinks -> `Python <http://www.python.org/>`_
External hyperlinks -> `www.python.org/  <http://www.python.org/>`_
''', {"test": "Test 1",
      "bla": 2,
      "blub": [3, 4, 5, 6],
      "Trace": [r"/*/Power", r"/*/Test", r"/*/Test/*/Test", r"/*/Test/*/Test/*/3. Test"]})
cd("./-")
Req("Test", "Test 1: Find same name in tree")
#Req("Test", "Duplicate Name Test")
cd("./-")
Req("Test", "Test: 2 Find same name in tree")
cd("./-")
Req("3. Test", "Test 3: Find a node after tow nodes with the same name")
Req("Whitespace Test", '''
This
Section dewscrubes       the platformas on which the system should run

''')
Req("[KAF03] Dorobo-Board: CAN-Message Erzeugung",
    "Die Software des Dorobo-Boards erzeugt CAN-Messages",
    {'Priority': 1})

Req("[KAF04] Dorobo-Board: Antwort CAN-Message versenden",
    "Die Software des Dorobo-Board antwortet dem Android-Gerät mit erzeugter CAN-Message, wenn Nachricht von Android-Gerät empfangen wurde [Link auf 1 und 3]",
    {'Priority': 1,
     'Trace': ["./*/[KAF03] Dorobo-Board: CAN-Message Erzeugung", "./*/[KAF05] Dorobo-Board: Empfang von CAN-Messages"]})


Req("[KAF05] Dorobo-Board: Empfang von CAN-Messages",
    "Die Software Des Dorobo-Board empfängt CAN-Messages vom Android-Gerät",
    {'Priority': """

 * item
 * item
 * item

 """})

Table("Test Table Ref",
      [
          ['Req', 'Ref'],
          ['Customer-Relationship-Management', """

           * item
           * item
           * item

           *bold*
           **italic**

            `/*/Customer Requirements`_
           """]
      ], "This table test Ref.")

PlantUML("UML Test","""
Alice -> Bob: A
Bob --> Alice: B
Alice -> Bob: C
Bob --> Alice: D
""", "Dies ist ein Test von plantUML Seq-Diagramm")

print("-------------------------------")
print(node("/*/Test").id, node("/*/Test/*/Test").id, node("/*/Test/*/3").id)
print("-------------------------------")


#w.dump()

node("/").genPDF()
node("/*/Vacuum Cleaner").genHTML(["ref", "istar", "ieee830"])


ShowTree(node("/*/Software Requirements"))
