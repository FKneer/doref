#!/usr/bin/env python
# -*- coding: utf-8 -*-


from _test_project.structur import *

cd("/*/Customer Requirements")

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
