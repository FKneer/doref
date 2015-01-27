#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This modules provides a class IEEE830SRS, which implements
    the IEEE830-1998 standard
"""
from ref import *

class IEEE830SRS(Document):
    chapterStructure = ["Introduction",
                        ["Purpose",
                         "Definitions",
                         "System Overview",
                         "References"],
                        "Overall Description",
                        ["Product Perspective",
                         ["System Interfaces",
                          "User Interfaces",
                          "Hardware Interfaces",
                          "Software Interfaces",
                          "Communication Interfaces",
                          "Memory Constraints",
                          "Operations",
                          "Site Adaptation Requirements"],
                         "Product Functions",
                         "User Characteristics",
                         "Constraints, Assumptions and Dependencies"],
                        "Specific Requirements",
                        ["External Interface Requirements",
                         "Functional Requirements",
                         "Performance Requirements",
                         "Design Constraints",
                         ["Standards Compliance"],
                         "Logical Database Requirement",
                         "Software System Attributes",
                         ["Reliability",
                          "Availability",
                          "Security",
                          "Maintainability",
                          "Portability"],
                         "Other Requirements"]]

    def __init__(self, name, authors, properties=None, folder=None):
        if properties is None:
            properties = {}
        Document.__init__(self, name,
                          "IEEE 830-1998 Software Requirements Specification", "SRS",
                          authors, properties, folder)
