#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Introduction
============
PlantUML is an Open Source project that allows to quickly write: • Sequence diagram,

 * Usecase diagram,
 * Class diagram,
 * Activity diagram,
 * Component diagram, • State diagram,
 * Object diagram.

Diagrams are defined using a simple and intuitive language, see `PlantUML Language Reference Guide
<http://plantuml.sourceforge.net/PlantUML_Language_Reference_Guide.pdf>`_ .

Example
=======
A sequence diagram:

.. figure:: ../../python/_plantUML/simple_seq_example.png
    :align: center

    Figure 2: Simple sequence diagram example

is written in PlanUML as: ::

    @startuml
    Alice -> Bob: A
    Bob --> Alice: B
    Alice -> Bob: C
    Bob --> Alice: D
    @enduml

and in DOREF as: ::

    PlantUML("UML Example","""
             Alice -> Bob: A
             Bob --> Alice: B
             Alice -> Bob: C
             Bob --> Alice: D
             """, "Example: plantUML Seq-Diagramm")

The PlantUML-Object needs:

 * a name
 * a PlanUML diagram definition without the @-Markup
 * an optional description

'''

from ref import *

class PlantUML(Model):
    mnemonic = 'UML'

    def getLabel(self):
        """


        :return:
        """
        return self.mnemonic

    def __init__(self, caption, plantUMLCode, text="", properties=None, pNode=None):
        if properties is None:
            properties = {}
        Model.__init__(self, caption, text, properties, pNode)
        self.plantUMLCode = plantUMLCode

    def genTeX(self, texAry, level, index, number):
        """

        :param self:
        :param texAry:
        :param level:
        :param index:
        :param number:
        """
        number = self.buildNumber(index, number)
        texAry.append(self.headTeX(level, number))
        texAry.append(self.bodyTeX())
        texAry.append(self.tailTeX())

    def bodyTeX(self):
        """

        :param self:
        :return:
        """
        self.genImage(show=False)
        return Figure.bodyTeX(self)

    def genImage(self, overwrite=True, show=False):
        """

        :param self:
        :param overwrite:
        :param show:
        """

        vDir = Document.path
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        vDir = Document.imgPath
        filename = self.name
        filename = filename.replace(' ', '_')
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        if overwrite is False:
            n = 0
            tmpfilename = filename + "_" + str(n) + '.txt'
            while os.path.isfile(vDir + tmpfilename) is True:
                n += 1
                tmpfilename = filename + "_" + str(n) + '.txt'
            filename = tmpfilename
            opfile = vDir + filename
        else:
            filename += '.txt'
            opfile = vDir + filename
        outfile = open(opfile, 'w', encoding='utf-8')

        texout = [r'@startuml',
                  self.plantUMLCode + '\n',
                  r'@enduml' + '\n\n']
        for i in texout:
            if not isinstance(i, str):
                i = "\n".join(i)
            i = parseString(i)
            outfile.writelines(i)
        outfile.close()
        print(opfile)
        os.system('java -jar ./_plantUML/plantuml.jar ' + opfile)
        self.figure = filename[:-3] + "png"

