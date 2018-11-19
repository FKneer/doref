#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This modules provides concepts for datamodeling:
     * DataItem describes a entity/class and its attributes
     * DataModel aggregates the entities/classes and attributes of the DataItems in a UML class diagram. The aggregation is limited to the current parent node.
     * DReq is a textual requirement which highlights words defined in the DataItems

"""
from ref import *
from plantuml import *

class DataItem(Chapter):
    def bodyTeX(self):
        self.addReferenceToReq()
        return super().bodyTeX()

    def getReference(self):
        return r" \textit{\hyperref["+self.name + str(self.id) + "]{" + self.name + "}} "

    def __init__(self, name, desc=None, expl=None, attr=None, properties=None, pNode=None):
        if properties is None:
            properties = {}
        if desc:
            Chapter.__init__(self, name, desc, properties, pNode)
        else:
            Chapter.__init__(self, name, '', properties, pNode)

        if expl:
            inf = ['Examples:', '']
            for ex in expl:
                inf.append('* ' + ex)
            Inf('\n'.join(inf), pNode=self)

        self.attributes = attr
        if attr:
            i = 0
            for at in self.attributes:
                if isinstance(at, str) is True:
                    self.attributes[i] = [at, '', '']
                i += 1
                while len(at) < 3:
                    at.append("")
            Table('Attributes', [['Name', 'Type', 'Description']] + self.attributes, '', {'position':'fixed'}, pNode=self)
#        # TODO: BUG in table: name == caption but they are not equal

    def addReferenceToReq(self):
        node = self
        while node.parent is not None:
            node = node.parent
        self.addReferenceToReqR(node, self.name, "`/*/" + self.name + "`_")

    def addReferenceToReqR(self, pNode, text, ref):
        if len(pNode.nodes) > 0:
            for n in pNode.nodes:
                if isinstance(n, Req) is True:
                    n.text = n.getText().replace(text, ref)
                if len(n.nodes) > 0:
                    self.addReferenceToReqR(n, text, ref)



class DataModel(Chapter):
    def __init__(self, title, relationships, text="", properties=None, pNode=None):
        if properties is None:
            properties = {}
        Chapter.__init__(self, title, text, properties, pNode)
        DataModelBase(title, relationships, pNode=self)


class DataModelBase(PlantUML):
    def __init__(self, title, relationships, text="", properties=None, pNode=None):
        self.relationships = relationships
        if properties is None:
            PlantUML.__init__(self, title, '', text, properties, pNode)

    def genTeX(self, texAry, level, index, number):
        classes = []
        for i in self.getParent().getParent().nodes:
            if i.getType() == 'DataItem':
                classes.append('class ' + i.getName() + ' {')
                for j in i.attributes:
                    classes.append('   ' + j[0])
                classes.append('}')
        self.plantUMLCode = '\n'.join(classes) + self.relationships
        PlantUML.genTeX(self, texAry, level, index, number)



class DReq(TextElement):
    def __init__(self, shortName, text, properties=None, pNode=None):
        if properties is None:
            properties = {}
        properties['Type'] = 'Requirement'
        TextElement.__init__(self, shortName, text, properties, pNode)

    def bodyTeX(self):
        texOut = []
        texOut.append(getUnicodeStr(self.getText().replace('Guest', '**Guest**')))
        texOut.append('\n')
        return texOut
