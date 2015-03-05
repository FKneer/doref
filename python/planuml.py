#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ref import *

class PlantUML(Model):
    mnemonic = 'UML'

    def getLabel(self):
        """


        :return:
        """
        return self.mnemonic

    def __init__(self, caption,plantUMLCode, text="", properties=None, pNode=None):
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
        vDir += Document.imgPath
        filename = vDir + '/' + self.name
        filename = filename.replace(' ', '_')
        if not os.path.isdir(vDir):
            os.mkdir(vDir)

        if overwrite is False:
            n = 0
            while os.path.isfile(filename + '_' + str(n) + '.txt') is True:
                n += 1
            opfile = filename + '_' + str(n) + '.txt'
        else:
            opfile = filename + '.txt'
        outfile = open(opfile, 'w', encoding='utf-8')

        texout = [r'@plantuml',
                  self.plantUMLCode + '\n',
                  r'@enduml' + '\n\n']
        for i in texout:
            if not isinstance(i, str):
                i = "\n".join(i)
            i = parseString(i)
            outfile.writelines(i)
        outfile.close()

        os.system('java -jar ./planuml.jar ' + opfile)

