#!/usr/bin/env python
# -*- coding: utf-8 -*-


from example_method import *
from plantuml import *

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
