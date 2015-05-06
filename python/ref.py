#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Introduction
============
This document is a quick start guide to the DO\ :sub:`RE`\ F (Dortmund Requirements Engineering Framework).
It explains the concepts and their application using the example files ``example_method.py`` and
``example_project.py``.

Concept
=======

DO\ :sub:`RE`\ F offers a language for requirements engineering combined with document generators (HTML, PDF, PNG).
The core idea of DO\ :sub:`RE`\ F is to let requirements engineers focus at the content and the semantics
of requirements documents rather than layout.


The language offers basic constructs described in this document. The language is

* comprehensive - it addresses *products* and *processes* in RE
* method-agnostic - it does not infer a particular RE approach
* extensible by modules  - using modules, the framework can be tailored to a particular RE approach
  (e.g., istar).

Look for further documentation at the modules.


Tree Structure
==============
All main elements (World, Documents, Workflows, …) are organized in a single tree called *RE tree*.
Figure 1 shows the general structure of the RE tree.

.. figure:: ../../python/_ref/retree.png
    :align: center
    :width: 50%

    Figure 1: RE Tree

The root of the tree is called *World*. The aggregation relationships (1-to-n)
between World and System and so forth eventually result in a large tree structure.

In order to build the RE tree, two ways are possible:

* Provide a reference to the parent object when creating a child. This is shown in the next section. However, this
  makes the code harder to read.
* Use the directory concept. Think of the RE tree as a directory structure for a file system. The framework maintains
  a *current directory*. When you create an object, it is inserted in the current directory.

Directories
-----------
You can change the current directory and you can search for elements (folder or files). The syntax for the ``cd``
command is ``cd(<path>)``.

Some of the commands, which are described later, require a node (e.g., to modify it). The command ``node(<path>)``
provides the required reference to a node. The path expression works as describe below. An absolute path is usually
used with the ``node`` command.

A ``pwd`` (print working directory) command is available to print the current directory.

Path Expressions
----------------

A path refers to the names of elements in the RE tree. A path can be provided in an *absolute* or *relative* way.

* Absolute: ``/*/<name>``  refers to an element called name in the tree, which is searched starting from root. The
  wildcard ``*`` indicates that the search is recursive, i.e., the node ``<name>`` is found at any position in the
  tree.
* Relative: ``./*/<name>`` the node ``<name>`` is searched in the current subtree.

A shorthand for the recently created node is ``./-``  This refers to the node which was recently created. This
comes handy as in ``cd('./-')``, because otherwise ``ch('./*/<name_of_recently_created_node>')`` has to be used.

Use ``..`` to refer to the parent directory. For example, ``ch('..')`` changes to the parent directory.

DO\ :sub:`RE`\ F enforces unique names only for the children of a single parent node. That is, two elements that do
**not** share the same parent may have the same names.  A path expression always refers the *first* match. In order
to provide a unique path expression, you must add unique *intermediate* elements in an expression. Let us assume two
elements named *bar* in the RE tree. ::

    / test / checking / foo / bar
                      / goo / bar

The expression ``/*/foo/*/bar`` refers to the *bar* element in the first line, ``/*/goo/*/bar`` the one in the
second line. Note that even if the specified names follow each other immediately in the tree, a ``*``  is
required in between (this makes path expressions more robust regarding changes in the RE tree).

The *name* in a path expression does not need to be fully specified. If the name of a node **starts with** the *name*
provided in the path expression, we have also a match. That is, ``/*/g/*/b`` is the same as ``/*/goo/*/bar``. Use
this feature with care, because changes in the RE tree might lead to unexpected results.

Note that there is *no* exception thrown if a path expression is not unique.

Initiate a Project
==================

The following lines illustrate how to initiate a project. First, the relevant subset of the real world
(“Universe of discourse”) is named. The world is the root object in the RE tree. ::

    w = World("My Smart Home")

Then, we create an element representing the system to be build. Note that we make a reference to the world w,
which serves as the parent object. ::

    s = System("Vacuum Cleaner", w)

In the following step, we define a project, for building the system. Now, we make a reference to the system s as
parent object. ::

    p = Project("Adaptive Control", s)

The project serves a container for the documentation of the project as it is usually done in an IDE. Think of a
folder structure and documents you want to place in the folders. Now, we make use of the directory concept mentioned
above. ::

    cd("/*/Adaptive Control")

We change the current directory to the project “directory” and create two folders. Note that we do not provide a
parent, nevertheless the folders are created under the project “Adaptive Control”. ::

    Folder("Protocols")
    Folder("Specifications")

Frequently, you want to change directory to the last element that we created in order to create subelements.
Instead of writing ::

    cd("/*/Specifications ")

you may use the following shorthand ::

    cd("./-")


Create Documents
================

This section describes how to create documents and how to add content to them.

Create Document Templates
-------------------------

An organization usually maintains document templates for various purposes. In order to allow reuse of templates
from one project to the next, document templates are defined in a separate file called ``example_method.py``.

Define for each document type that you want to use in your project a class that inherits from class Document
of DO\ :sub:`RE`\ F. Overwrite the static attribute chapterStructure with the chapter structure of your document
flattened as a list of lists as the following example illustrates. ::

    class IEEE830SRS(Document):
        chapterStructure = ["Introduction",
                        ["Scope",
                         ["sc1", "sc2",
                          ["z1", "z2"]],
                         "Definitions"],
                        "Overall Description",
                        "Specific Requirements",
                        ["User", "System"]]

It is recommended (but not necessary) to overwrite the constructor, in order to provide some useful defaults. ::

    def __init__(self, name, authors, properties=None, folder=None):
        if properties is None:
            properties = {}
        Document.__init__(self, name,
                       "IEEE 830-1998 Software Requirements Specification",
                       "SRS", authors, properties, folder)

An instance of the document type defined above can be derived as follows: ::

    IEEE830SRS("Software Requirements for Adaptive Control of Vacuum Cleaner",
           [["Erik Kamsties and Fabian Kneer",
              "RE Research Group", "FH Dortmund"]],
           {'language': 'german', 'paper': 'a4', 'font': '11pt'})

Add Project-specific Chapters
-----------------------------

Usually some project specific chapters are added to a document template. This is accomplished very easy by
creating the required chapters in the following way: ::

    cd("/*/Specific Requirements")
    Chapter("Customer Requirements", "This chapter describes [...].")
    cd("./-")

This sequence of commands changes to the “Specific Requirements” directory defined in the document template.
Then, a chapter “Customer Requirements” is added. That is, a heading is generated and an additional paragraph,
which contains the additional description. Finally, we change into this new directory.

Write a Requirement
-------------------

The following screenshot shows a requirement and an additional information in a PDF document generated from
DO\ :sub:`RE`\ F. Each entry has a head, a body, and a tail. The head is formed by a number, a short name
(“Information” in case of an information), and an ID of the element (e.g., SRS-21). The body is the description of the
requirement (or information) itself. The tail is a list of attributes concerning the requirement
(e.g., type characterizes an element as Requirement or Information).

.. figure:: ../../python/_ref/reqinf.png
    :align: center

    Figure 2: Snippet of generated requirements document

Requirements are added to the document very easy by the ``Req`` command. It requires a title,
a description of the requirement, and an optional list of attributes. ::

    Req("Clean at night",
        "The robot shall clean the apartment at night.",
        {'Priority': 1,
         'Effort': 20,
         'Optional': 1})

Additional attributes characterize a requirement and are provided as a list of names and values. The above
requirement has three attributes, *Priority*, *Effort*, and *Optional*. The type of the attributes does not need
to be defined; it is inferred from the provided values.

Add Traceability
----------------

DO\ :sub:`RE`\ F supports traceability in a flexible way. Links are added to an element, e.g., to a requirement,
as an additional attribute. An element  may link to several other elements at once. ::

    Req("Silence", "The operation of the vacuum cleaner should be as silent as possible.",
        {'Priority': 2,
         'Trace': ["./*/Power", "./*/Clean"]})

In the example above, the requirement refers to two other requirements called "Power" and "Clean", provided as
a list ``[ ...]``. A traceability link becomes a *hyperlink* in the generated documentation. Click on the link
and you jump to the target of the link. Note that only path expressions are used (not references to the target
nodes). Because the target might not exist when the source is created (in case of forward traces),
the path expression is evaluated when the RE tree is printed.

You may add several link attributes for different link types, e.g., 'refines', 'alternative', 'helps', 'hurts'.

Add Sub-elements
----------------

Additional information, for example a rationale, or sub-requirements refining a main requirement are added
to a requirement as the following example shows. ::

    Req("Silence",
        "The operation of the vacuum cleaner should be as silent as possible.",
        {'Priority': 2})
    cd("./-")
    Inf("The vacuum cleaner should not disturb the persons living in the apartment.")
    cd("..")

The additional information is added to the requirement as a sub-element.

Simple Markup
-------------

A simple markup for italic, bold, and lists can be used in a requirement or information. The markup
syntax follows `ReStructuredText (RST)
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ (which is commonly used in the Python community):

* *italic* = ``*italic*``
* **bold** = ``**bold**``

A bullet list:

* This
* is
* a list
* with a very long last item,
  that stretches over two lines

is written as: ::

    A bullet list:

    * This
    * is
    * a list
    * with a very long last item,
      that stretches over two lines

Note that a bullet list starts and ends with a blank line. If a long bullet item stretches over more than
one line, continue the indentation in the following lines.
Because of the generation with LateX the max deep for a bullet list is four level.

References
----------

An *external reference* points to a webpage. An *internal reference* points to a node in the RE tree. Both
types can be used in any text (e.g., requirement or information).

The markup syntax for references adapts the syntax of hyperlink targets in `ReStructuredText (RST)
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ (which is commonly used in the Python community):

* External reference: `Python <http://www.python.org/>`_ = ```Python <http://www.python.org/>`_``
* Internal reference: Reference to a node as "see Power (SRS-20) on page 6" = ``Reference to a Node, see `/*/Power`_``

Note that a reference starts with a grave accent **`** and ends with a grave accent followed by an underscore **`_**

Further RST markup for hyperlink targets is currently not supported.


Longer chunks of text
---------------------

A statement stretches sometimes over more than one line in the editor. In this case, choose one of the following
two ways at your convenience. ::

    Inf("Porto (port. Aussprache ['poɾtu]) ist die "
        "Hauptstadt des gleichnamigen Distriktes in "
        "Portugal und liegt am Douro vor dessen Mündung "
        "in den Atlantischen Ozean. Mit circa 237.000 Einwohnern "
        "(port. portuenses; dt. Portuenser genannt) ist sie "
        "nach Lissabon und ihrer Nachbarstadt Vila Nova de Gaia "
        "die drittgrößte Stadt des Landes.")

An IDE such as PyCharm supports you when writing such a statement. Each time you press ENTER, respective quotes on
the new line are added automatically. The second way is to use a so-called *multiline string* as the following
example shows. A multiline string is embraced by triple quotes. ::

    Inf(\'''
        Der rund 1,29 Millionen[3] Einwohner zählende Ballungsraum
        Grande Porto rangiert landesweit jedoch an zweiter Stelle.
        Porto ist eine der ältesten europäischen Städte, sie wird
        gern als die „Hauptstadt des Nordens“ bezeichnet.
        \''')

Quotes on each single line can be avoided this way.

Print the Tree
--------------

The whole RE tree can be represented as a set of HTML pages. Each document in the RE tree
is transformed into a PDF and the HTML pages link those PDFs. The function in charge is
called ``genHTML()``. It is recommended to provide a list of imported modules in order
to generate also documentation for them as the following example shows. ::

    node("/").genHTML(["ref","istar","ieee830"])

A single document can be transformed into a PDF. ::

    node("/*/Software Requirements for Meeting Scheduler").genPDF()

If ``genPDF()`` is called on the root node, each document in the RE tree is
transformed into PDF. ::

    node("/").genPDF()

The full tree can be dumped on the console for testing purposes. Partial trees can be printed by calling dump()
on the respective node. ::

    node("/").dump()

Compare the PDF output and the original files (``meeting_scheduler.py`` and ``example_project.py``).

Figures
-------

Figures can be added to a document. The Figure element refers to an image file in JPG, PNG, or EPS format. The
Figure element requires a title and a file name. Optional are an explanation and a list of properties. Two
layout hints can be used for PDF output in the properties:

* size = {``fit``, ``asis``}, ``fit``: image is resized to fit page width, ``as is``: the original image size is kept
* position = {``float``, ``fixed``}, ``float``: figure is floating to a optimal layout position, a reference to the
  figure is added, ``fixed``: the figure sticks to current position in the document.

An example is provided in the following. ::

    Figure("RE - World, Documents, and Workflows", 'model.png',
           "This figure shows the main corner stones of RE.",
           {'size': 'fit'})

The defaults are ``as is`` and ``float``.  A figure must fit on a single page.

Tables
------
Tables can be used in a document. A table is intended to structure a single requirement or to structure a
single piece of information. The Table element requires a title and the content of the table. The content is
described by a list containing a list of strings for each line. The first line is treated as the table heading.
Optional parameters are an explanation and a list of properties. Two layout hints can be used for PDF output
in the properties:

* size = {``fit``, ``equal``}, ``fit``: the column widths are chosen such that the content fits, ``equal``: each
  column has the same width
* position = {``float``, ``fixed``}, ``float``: table is floating to an optimal layout position, a reference
  to the table is added, ``fixed``: the table sticks to current position in the document.

::

    Table("Actor Description", [
        ['Term', 'Description'],
        ['Customer-Relationship-Management',
             'Customer-Relationship-Management, kurz CRM
              (dt. Kundenbeziehungsmanagement) oder Kundenpflege,
              bezeichnet die konsequente Ausrichtung einer Unternehmung
              auf ihre Kunden und die systematische Gestaltung der ']
        ], "This table defines some terms.")

The defaults are ``fit`` and ``fixed``.   The option ``fit`` works best when the content of the columns differ
significantly (e.g., a term and a description). The option ``equal`` is useful, if the content is more or less
balanced. In any case, the columns must fit on a single page. A page break is inserted between rows if required
such that a table may span more than one page.

Numbering
---------
Each element in the RE tree has an *ID*. The ID is generated when the element is created. The ID does not change
through the lifetime of the element.

Each element in a Document has in addition a *number*, which is derived from the chapter number and the hierarchical
order of element. That is, the number represents the position of the element in the document subtree. A
typical number could be 3.2.1-2-3. Let us explain the numbering scheme in the following:

* The chapters in a document are numbered as in any other ordinary document. That is, “3.2.1 System Requirements”
  means that this chapter is a subchapter of 3.2, which is in turn a subchapter of chapter 3. A Chapter element itself
  serves as a *purely structural element* and does not carry any requirements.
* Any other element added to a chapter (Information, Requirement, Figure, Table, …) contains information or
  requirements. These elements are numbered in the same way, but a dash (‘-‘) serves as separator. The
  number 3.2.1-2-3 tells us, that we see the 3rd subelement (e.g. an information) of the 2nd element
  (e.g., a requirement) in Chapter 3.2.1. That is, the number is a representation of the tree structure, which
  lays behind a document, but which is not directly visible.

* Please note: to ensure a consistent numbering, you can insert into a chapter either *sub-chapters* or *non-chapter
  elements* (information, requirement, table, figure, ..), but **not a mixture of both**. If you mix both, an
  exception is thrown.

Edit and Delete Nodes
---------------------

Each member of the RE tree can be modified or deleted. The command ``ch(<node>, <attr>, <value>)`` changes an
attribute of the node to the given value. Two attributes are predefined: ``name`` and ``text``. Example how to
add an explanation to a chapter: ::

    ch(node('/*/Portability'), "text",
        """This Section describes the platforms on which the system shall run.""")

The command ``rm(<node>)`` deletes a node and its subtree of nodes. For example, ::

    rm(node('/*/States of a Traffic Light'))

deletes the whole model describing the state of a traffic light, i.e., the whole diagram.

Add, Change, and Delete Attributes
----------------------------------
The commands ``ch`` (“change”) and ``rm`` (“remove”) are also used to maintain attributes. Use the ``ch`` command in
order to add an attribute to a node. ::

    ch(node('/*/Rot'), "Author", "Erik", insert=True)

The parameter ``insert`` indicates that an attribute shall be created if it does not exist. The value of the
attributes is changed easily: ::

    ch(node('/*/Rot'), "Author", "Fabian”)

An attribute is deleted from a node with the ``rm`` command. ::

    rm(node('/*/Rot'), "Author")

Generic Requirements Models
---------------------------
DO\ :sub:`RE`\ F allows for generic requirements modeling ("box and line diagrams"). A model is created with the
``GenericModel`` command, which expects a short name (for the caption of the diagram) and a description. ::

    cd("/*/Specific Requirements")
    GenericModel("States of a Traffic Light",
       "This model shows the states and transitions of a traffic light in Germany.")

The command creates an empty diagram. In a next step, nodes are added to the diagram. Currently,
the following nodes are supported: *Box* and *Circle*. A node just requires a name. The concrete semantics
of these symbols has
to be defined in the description of the generic requirements model. In the following
example, four circles (states) are added to the diagram. ::

    cd('./-')
    Circle("Red")
    Circle("Red-yellow")
    Circle("Green")
    Circle("Yellow")

Finally, when the nodes are present, the edges can be added. Currently,
the following edges are supported: *Line* and *Arrow*. An edge requires a source and a destination node. These are
usually provided using the ``node`` command. Again, the semantics has to be provided separately.
In the following example, four arrows (state transitions) are added to connect the circles (states). ::

    Arrow(node('./*/Red'), node('./*/Red-yellow'))
    Arrow(node('./*/Red-yellow'), node('./*/Green'))
    Arrow(node('./*/Green'), node('./*/Yellow'))
    Arrow(node('./*/Yellow'), node('./*/Red'))

Please note that we use *relative* path expressions to avoid the problem that other nodes somewhere else in
the RE tree accidentally have the same name.

DO\ :sub:`RE`\ F generates a diagram using autolayout (based on Graphviz) and includes it in the respective PDF
document.

Specific requirements modeling techniques are available as separate modules.



Define Workflows
================

A workflow describes a domain-dependent, project-specific approach to RE. A workflow consists of activities.
You can define your own activities or you can refer to activities, which are defined in the modules that
you are using. When you create a workflow a *web-based process guide* is generated, which supports engineers
to carry out their tasks.

Creating a workflow with activities
-----------------------------------

In the following example, we create a workflow for a goal-oriented RE process. This example refer to
``meeting_scheduler.py`` example. First, we create a workflow as a child of a Project. ::

    cd("/*/Meeting Scheduler Development")
    Workflow("Goal-oriented RE")

Then, we create an Activity. This is a self-defined activity - it describes what to do at the beginning
of a project. An activity has a name and a description. Use the `ReStructuredText (RST) markup
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ to beautify your description of an activity.
All tags of RST can be used.  ::

    cd("./-")
    Activity("Initiate RE Project", \'''
            In this activity, the folder structure and the (empty) documents are created.
        \''')

Modules come with predefined activities (which inherit from Activity). For example, the istar module
offers an activity called ``DevelopSRModel``, which contains a  description of how to create
a Strategic Relation model. In the following, we add a predefined activity to our workflow. ::

    DevelopSRModel("Develop SR-Model Meeting Scheduler")

Executing a workflow
--------------------

Some activities can be fully automatized and thus can be implemented. For example, the activity ``PropagateLabels``
of the istar module can be implemented (except for the *Human Judgement* in Rule 10). In this case, the activity
can be called (i.e., executed) using the ``do()`` method. ::

    PropagateLabels("Initially Propagate Labels", goalModel=node("/*/SD-Model of Meeting Schedule")).do()

Note that PropagateLabels takes an extra parameter ``goalModel``. That is, it requires a goal model (subtree of the
RE tree) on which the label propagation algorithm is applied on.

Errors
======
A few errors might appear when you run your RE project.

**Wrong signature**: you create an object of RE tree with a wrong list of parameters.
For example, a Requirement needs a short name and a description, while an Information just
needs a description. When you create an information with a short name and a description
(like a requirement) you will see a message similar to the following one: ::

    C:\Python34\python.exe D:/Kamsties/.../example_project.py
    Traceback (most recent call last):
      File "D:/Kamsties/.../example_project.py", line 40, in <module>
        Inf("Clean", "The vacuum cleaner should not disturb the persons living in the apartment.")
      File "D:/Kamsties/.../ref.py", line 456, in __init__
        properties['Type'] = 'Information'
    TypeError: 'str' object does not support item assignment

    Process finished with exit code 1

Recommendation: look at the error trace and click on the last entry before ref.py is called.

**Exceptions**: DO\ :sub:`RE`\ F raises a few exceptions, when a specific problems appear at runtime:

* ``cd('<path>')``

  * The path does not exist or
  * is syntactically incorrect

* ``Document(…)``

  * the ``chapterStructure`` variable does not contain a list, which can be represented as a tree structure

* ``Chapter(…)``

  * A non-chapter element (requirement, information, table, …) is added to a chapter, which does contain only
    subchapters so far.
  * A chapter is added to chapter, which does only contain non-chapter elements so far.

* any type of node

  * The nodes under a parent (direct successors) must have unique names. An exception is thrown when a second
    node with the same name is added to a respective parent.

The API of DO\ :sub:`RE`\ F is explained in alphabetical order in the remainder of this document.
'''

import copy
import re
import os
import os.path
from graphviz import Digraph

# Generic tree management

root = None
cursor = None
lastInsert = None


def parseString(string):
    string = string.replace("\t", " ")
    string = findLink(string)
    string = findReference(string)
    string = findReferenceAfterUnicode(string)
    string = findBold(string)
    string = findItalics(string)
    string = findItemize(string)
    return string


def changeString(old, first, last, new):
    newString = old[0:first] + new + old[last:len(old)]
    return newString


def findReference(text):
    expression = r' `([^`]* )`\_'
    replace = r' (-ref-)\1(-ref-)'
    p = re.compile(expression, re.VERBOSE + re.UNICODE)
    text = p.sub(replace, text)
    split = text.split("(-ref-)")
    out = []
    for line in split:
        if str(line).startswith(r'/*/'):
            out.append(node(line).getReference())
        else:
            out.append(line)
    text = "".join(out)
    return text


def findReferenceAfterUnicode(text):
    expression = r' `([^`]* )`\\_'
    replace = r' (-ref-)\1(-ref-)'
    p = re.compile(expression, re.VERBOSE + re.UNICODE)
    text = p.sub(replace, text)
    split = text.split("(-ref-)")
    out = []
    for line in split:
        if str(line).startswith(r'/*/'):
            out.append(node(line).getReference())
        else:
            out.append(line)
    text = "".join(out)
    return text


def findLink(text):
    expression = r' `( [^<`]* ) \< ( [^>]* ) \>`\\_ '
    replace = r'\href{\2}{\1}'
    p = re.compile(expression, re.VERBOSE + re.UNICODE)
    text = p.sub(replace, text)
    return text


def findBold(text):
    expression = r'(\n | \  | \( | \\\{ | \[ ) \*\*( [^**\ | ^**\n]+ [^**]* [^**\ | ^**\n]+  )\*\* ' \
                 r'( \n | \ | \) | \\\} | \] | \. | \! | \? | \, | \: | \; )'
    replace = r'\1\\textbf{\2}\3'
    p = re.compile(expression, re.VERBOSE + re.UNICODE)
    text = p.sub(replace, text)
    return text


def findItalics(text):
    expression = r'(\n | \  | \( | \\\{ | \[ ) \* ( [^*\ | ^*\n]+ [^*]* [^*\ | ^*\n]+  )\* ' \
                 r'( \n | \ | \) | \\\} | \] | \. | \! | \? | \, | \: | \; )'
    replace = r'\1\\textit{\2}\3'
    p = re.compile(expression, re.VERBOSE)
    text = p.sub(replace, text)
    return text


def findItemize(text):
    split = text.split("\n\n")
    out = []
    for part in split:
        part = "\n" + part
        index = part.find('* ')
        if index != -1:
            i = 1
            while index - i > 0 and part[index - i] == ' ':
                i += 1
            if index - i == 0 or index == 0:
                expression = r'(\n\ *) \*\ ( [^(\n\*\ )(\ \*\ )]* )'
                replace = r'\1\\item \2'
                p = re.compile(expression, re.VERBOSE + re.UNICODE)
                part = p.sub(replace, part)
        index = part.find('\\item ')
        if index != -1:
            lastindex = 0
            newtab = 0
            while index - newtab > lastindex and part[index - newtab] != '\n':
                newtab += 1
            tab = newtab

            part = part[:index] + "\n" + r"\begin{itemize}" + "\n" + (' ' * (newtab - 1)) + part[index:]
            while index != -1:
                index = part.find(r"\item ", lastindex)

                if index != -1:
                    newtab = 0
                    while index - newtab > lastindex and part[index - newtab] != '\n':
                        newtab += 1
                    if newtab > tab:
                        part = part[:index] + r"\begin{itemize}" + "\n" + (' ' * newtab) + part[index:]
                        lastindex = index + 21 + newtab
                    elif newtab < tab:

                        part = part[:index] + (r"\end{itemize}" + "\n") * (tab - newtab) + (' ' * newtab) + part[index:]

                        lastindex = index + 5 + 14 * (tab - newtab) + newtab
                    else:
                        lastindex = index + 5
                    tab = newtab
            begin = part.count(r"\begin")
            end = part.count(r"\end")
            part = part + "\n" + (r"\end{itemize}" + "\n") * (begin - end)
            out.append(part)
        else:
            out.append(part)

    return "\n".join(out)


def cd(path):
    """ Short Description TODO
        
        Long Description
        
        Args:
            Description of the parameters
            path: Description of the parameter 'path'
        
        Returns:
            Description of the return value (Structure)
        Raises:
            Description of the Errors
    """
    global cursor
    cursor = node(path)


def node(path):
    """Returns the node object specified by a path expression.

    :param path: Path expression '/`*`/node_x' - searches for node_x in the tree

    :return: node object

    :raises: TypeError: An error occurred during evaluation of path command.
             TypeError: node not found
    """
    if path == "./-":
        node_ = lastInsert
    elif path == "..":
        node_ = cursor.getParent()
    else:
        patharray = path.split('/')
        if patharray[0] == '.':
            seed = cursor
        elif patharray[0] == '':
            seed = root
        else:
            raise NameError("misformed path!")
        del patharray[0]
        node_ = nodeR(seed, patharray, False)
    return node_


def nodeR(pNode, pathArray, nextLevel):
    if not pathArray or pathArray[0] == '':  # catching root "/" = ['','']
        return pNode
    if pathArray[0] == '*':
        pNode = pNode.getNodeByName(pathArray[1], nextLevel)
        if pNode is None:
            raise NameError('node \'' + pathArray[1] + '\' not found!')
        del pathArray[0:2]
        return nodeR(pNode, pathArray, True)
    else:
        raise NameError("cd: misformed path!")


def pwd():
    print('===> ' + pwdR(cursor, ""))


def pwdR(pNode, path):
    if pNode is None:
        return '/ ' + path
    else:
        return pwdR(pNode.parent, pNode.name + ' / ' + path)


def ch(modNode, attribute, value, insert=False):
    """ The ch command changes the value of an attribute of a node of the RE tree. Also, a new attribute
    can be added.

    :param modNode: node to be modified

    :param attribute: build-in attribute to be modified

    :param value: new value

    :param insert: if true, the attribute is added to the object if it does not exist

    :return: none
    """
    print(value)
    if hasattr(modNode, attribute):
        modNode.setNode(attribute, value)
    elif hasattr(modNode, 'properties'):
        if attribute in modNode.properties or insert is True:
            modNode.properties[attribute] = value  # TODO: nach Node verschieben
        else:
            raise AttributeError("Attribute '" + attribute + "' not in node '" + modNode.name + "' !")
    else:
        raise AttributeError("Attribute '" + attribute + "' not in node '" + modNode.name + "' !")


def rm(delNode, delAttribute=None):
    """ Deletes either an attribute from a node (this can only be done for self-defined attributes) or
    it deletes the subtree of node and node itself. Afterwards, cursor is on the parent node of the deleted node.

    :param delNode: root of subtree to be deleted

    :param delAttribute: attribute to be deleted (optional)
    """
    if delAttribute is None:
        global cursor, lastInsert
        # __del(delNode)   # TODO: was heisst das?
        cursor = delNode.getParent()
        lastInsert = delNode.getParent()
        delNode.getParent().delNode(delNode)  # remove node from parent
        del delNode  # remove subtree
    else:
        if hasattr(delNode, delAttribute):
            delAttribute.setNode(delAttribute, None)
        elif hasattr(delNode, 'properties'):
            del delNode.properties[delAttribute]  # TODO: nach Node verschieben
        else:
            raise AttributeError("Attribute '" + delAttribute + "' not in node '" + delNode.name + "' !")


def mv(movNode, destination, position=None):
    """ Moves the subtree of the node and the node itself to the given destination.
    Afterwards, cursor is on the new parent node of the moved node.

    :param movNode: root of subtree to be moved

    :param destination: destination node for moving

    :param position: position in child nodes of the destination node. None = append
    """
    movNode.getParent().delNode(movNode)  # remove node from current parent
    if position is not None:  # add node to new parent to given position
        if position <= len(destination.nodes):  # TODO: nach Node verschieben
            destination.nodes.insert(position, movNode)
        else:
            destination.nodes.append(movNode)
    else:
        destination.nodes.append(movNode)
    movNode.parent = destination


def clone(cpNode, destination, position=None):
    """ Clones the subtree of node and node itself to the given destination.
    This is an identical copy of the original subtree (nodes keep their
    IDs and names). For framework internal use only!

    :param cpNode: root of subtree to be copied

    :param destination: destination node

    :param position: position in child nodes of the destination node
    """

    newNode = copy.deepcopy(cpNode)
    if position is not None:
        if position <= len(destination.nodes):
            destination.nodes.insert(position, newNode)
        else:
            destination.nodes.append(newNode)
    else:
        destination.nodes.append(newNode)
    newNode.parent = destination


class Node(object):
    def __init__(self, name, parent=None):
        global root, cursor, lastInsert
        self.name = name
        self.nodes = []  # subnodes of the current node
        self.parent = parent
        if self.parent is None:
            self.parent = cursor  # use possibly uninitialized cursor
        if self.parent is not None:
            self.parent.addNode(self)
        else:  # root of tree, init globals
            root = self
            cursor = self
        lastInsert = self
        self.id = self.getID()  # assign world-unique ID

    def addNode(self, n):
        if not isinstance(n, Inf) and n.name is not None and n.name != "":
            for tmpnode in self.nodes:
                if tmpnode.name == n.name:
                    raise AttributeError("Duplicate name: " + n.name)
        self.nodes.append(n)

    def getReference(self):
        return " " + self.name + " (" + self.getLabel() + "-" + str(self.id) + ") " + \
               r"on page \pageref{" + self.name + str(self.id) + "} "

    def delNode(self, n):
        self.nodes.remove(n)

    def getType(self):
        return type(self).__name__

    def setNode(self, attribute, value):
        """ This method allows to modify the value of arbitrary attributes (but not methods) of a tree node.

        :param attribute: name of the attribute to be modified

        :param value: new value

        :return: none

        :raises: AttributeError if attribute is not in node
        """
        if not callable(getattr(self, attribute)):  # it is only allowed to overwrite true attributes but not methods
            if isinstance(value, str):
                setattr(self, attribute, ' '.join(value.split()))  # remove unnecessary whitespaces in multi-line string
            else:
                setattr(self, attribute, value)

    def getParent(self):
        return self.parent

    def getLabel(self):
        if self.parent is None:
            return "ID"
        else:
            return self.parent.getLabel()

    def getID(self):
        return self.parent.getID()

    def getName(self):
        return self.name

    def getNodeByName(self, name, nextLevel):
        if not nextLevel and self.name.startswith(name):
            return self
        else:
            ret = None
            for n in self.nodes:
                ret = n.getNodeByName(name, False)
                if ret is not None:
                    break
            return ret

    def dump(self):
        print(type(self).__name__ + ' \'' + self.getName() + '\'')
        for n in self.nodes:
            n.dump()

    def genTxt(self, index, number):
        index = 1
        for n in self.nodes:
            n.genTxt(index, number)
            index += 1

    def genPDF(self, overwrite=True, log=False):
        """ Traverses the tree from the current node and generates a PDF for each document.

        """
        for n in self.nodes:
            n.genPDF(overwrite=overwrite, log=log)

    def genTeX(self, outArray, level, index, number):
        level += 1
        index = 1
        for n in self.nodes:
            n.genTeX(outArray, level, index, number)
            index += 1

    def genRst(self, index):
        if self is not index:
            vDir = os.path.abspath(Document.path + "/rst/")
            filename = vDir + "/" + self.name
            filename = filename.replace(' ', '_')
            if not os.path.isdir(vDir):
                os.mkdir(vDir)
            opfile = filename + '.rst'
            outfile = open(opfile, 'w', encoding='utf-8')

            title = self.getType() + ' "' + self.name + '"\n'
            rstout = [title,
                      ("=" * (len(title) - 1)) + "\n\n"]
            if len(self.nodes) > 0:
                rstout.append("Content:\n")
                rstout.append("--------\n\n")
                rstout.append(".. toctree::" + "\n")
                rstout.append("  :titlesonly:" + "\n")
                rstout.append("  :maxdepth: 4" + "\n\n")
                for n in self.nodes:
                    if n is not index:
                        content = n.name + ".rst"
                        content = content.replace(' ', '_')
                        rstout.append('  ' + content + "\n")
            self.genRstBody(rstout)

            for l in rstout:
                outfile.writelines(l)
            outfile.close()
            for n in self.nodes:
                n.genRst(index)

    def genRstBody(self, rstOut):
        pass

    def genDot(self, dot):
        """ Traverses the tree from the current node and generates a graphviz model.

        """
        for n in self.nodes:
            n.genDot(dot)

    def do(self):
        """ Traverses the tree from the current node and execute each node.

        """
        for n in self.nodes:
            n.do()


def getUnicodeStr(tmpStr):
    """ This function escapes all characters with a special meaning in LaTeX

    :param tmpStr: Input String
    :return: Escaped string
    """
    split = tmpStr.split("`")
    out = []
    for part in split:
        if part.find("/*/") == -1 and part.find("<http:") == -1 and part.find("<www.") == -1:
            part = part.replace('\\', r'\textbackslash ')
            part = part.replace('_', '\_')
            part = part.replace('<', r'\textless ')
            part = part.replace('>', r'\textgreater ')
            part = part.replace('$', r'\$')
            part = part.replace('&', r'\&')
            part = part.replace('#', r'\#')
            part = part.replace('{', r'\{')
            part = part.replace('}', r'\}')
            part = part.replace('%', r'\%')
            part = part.replace('~', r'\textasciitilde ')
            part = part.replace('€', r'\texteuro ')
        out.append(part)
    return '`'.join(out)


# -------------------------------------------------------------------------------------------------------------------

class System(Node):
    """
    Dieses Sprachelement repräsentiert ein System, welches entwickelt werden soll. Ein System kann aus
    Systemen bestehen. Ein System besitzt einen Kontext. Externe Systeme, die bereits existieren und
    außerhalb des Projektaufgabenbereichs liegen, werden nicht als System, sondern als Teil des Kontextes
    aufgefasst. Jedes System besitzt einen Kontext. Dies führt zu der Situation, dass die Einordnung als
    System oder Kontext nicht absolut sondern relativ zum Blickwinkel ist.
    """

    def genRstConf(self):
        vDir = os.path.abspath(Document.path)
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        vDir = os.path.abspath(Document.path + "/rst/")
        filename = vDir + '/conf.py'
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        opfile = filename
        outfile = open(opfile, 'w', encoding='utf-8')
        confout = [r"#!/usr/bin/env python3" + "\n",
                   r"# -*- coding: utf-8 -*-" + "\n\n",
                   r"import sys" + '\n',
                   r"import os" + '\n\n',
                   r"sys.path.append(os.path.abspath('./'))" + '\n',
                   r"sys.path.append(os.path.abspath('./python'))" + '\n\n',
                   r"extensions = [" + '\n',
                   r"    'sphinx.ext.autodoc'," + '\n',
                   r"    'sphinx.ext.intersphinx'," + '\n',
                   r"    'sphinx.ext.todo'," + '\n',
                   r"    'sphinx.ext.ifconfig'," + '\n',
                   r"    'sphinx.ext.viewcode'," + '\n',
                   r"]" + '\n\n',
                   r"templates_path = ['../../etc/_templates']" + '\n',
                   r"source_suffix = '.rst'" + '\n',
                   r"master_doc = 'index'" + '\n\n',
                   r"exclude_patterns = []" + '\n\n',
                   r"pygments_style = 'sphinx'" + "\n\n",
                   r"html_theme = 'default'" + "\n\n",
                   r"html_static_path = ['../../etc/_static']" + "\n\n",
                   r"htmlhelp_basename = 'Test'" + "\n\n"]

        for l in confout:
            outfile.writelines(l)
        outfile.close()

    def genDocu(self, module):
        vDir = os.path.abspath(Document.path + "/rst/")
        filename = vDir + '/' + module + '.rst'
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        opfile = filename
        outfile = open(opfile, 'w', encoding='utf-8')

        title = module + r" -- explicit members" + "\n"
        moduleout = [title,
                     ("=" * (len(title) - 1)) + "\n\n",
                     r".. automodule:: " + module + "\n",
                     r"   :members:"]

        for l in moduleout:
            outfile.writelines(l)
        outfile.close()

    def genRst(self, index):
        if self is not index:
            vDir = os.path.abspath(Document.path + "/rst/")
            filename = vDir + "/" + self.name
            filename = filename.replace(' ', '_')
            if not os.path.isdir(vDir):
                os.mkdir(vDir)
            opfile = filename + '.rst'
            outfile = open(opfile, 'w', encoding='utf-8')

            title = self.getType() + ' " ' + self.name + '"\n'
            rstout = [title,
                      ("=" * (len(title) - 1)) + "\n\n"]
            sub = 0
            project = 0
            for n in self.nodes:
                if isinstance(n, System) and n is not index:
                    sub += 1
                if isinstance(n, Project):
                    project += 1

            if sub > 0:
                rstout.append("\nSub-System:" + "\n")
                rstout.append("-----------" + "\n\n")
                rstout.append(".. toctree::" + "\n")
                rstout.append(" :titlesonly:" + "\n")
                rstout.append(" :maxdepth: 4" + "\n\n")
                for n in self.nodes:
                    if isinstance(n, System) and self is not index:
                        content = n.name + ".rst"
                        content = content.replace(' ', '_')
                        rstout.append(" " + content + "\n")
            if project > 0:
                rstout.append("\nDeveloped by Project:" + "\n")
                rstout.append("---------------------" + "\n\n")
                rstout.append(".. toctree::" + "\n")
                rstout.append(" :titlesonly:" + "\n")
                rstout.append(" :maxdepth: 4" + "\n\n")
                for n in self.nodes:
                    if isinstance(n, Project):
                        content = n.name + ".rst"
                        content = content.replace(' ', '_')
                        rstout.append(" " + content + "\n")
            for l in rstout:
                outfile.writelines(l)
            outfile.close()
            for n in self.nodes:
                n.genRst(index)

    def genHTML(self, modules):
        """

        :param modules:
        """
        self.genRstConf()
        for module in modules:
            self.genDocu(module)
        vDir = os.path.abspath(Document.path + "/rst/")
        filename = vDir + '/index'
        filename = filename.replace(' ', '_')
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        opfile = filename + '.rst'
        outfile = open(opfile, 'w', encoding='utf-8')

        title = self.getType() + ' " ' + self.name + '"\n'
        rstout = [title,
                  ("=" * (len(title) - 1)) + "\n\n"]

        if self.parent is not None:
            rstout.append("Context:\n")
            rstout.append("--------\n\n")
            parent = self.parent
            depp = 2
            print(parent.name)
            while parent.parent is not None:
                parent = parent.parent
                print(parent.name)
                depp += 1
            rstout.append(".. toctree::" + "\n")
            rstout.append(" :titlesonly:" + "\n")
            rstout.append(" :maxdepth: " + str(depp) + "\n\n")
            content = parent.name + ".rst"
            content = content.replace(' ', '_')
            parent.genRst(self)
            rstout.append(' ' + content + "\n")
        sub = 0
        project = 0
        for n in self.nodes:
            if isinstance(n, System):
                sub += 1
            if isinstance(n, Project):
                project += 1

        if sub > 0:
            rstout.append("\nSub-System:" + "\n")
            rstout.append("-----------" + "\n\n")
            rstout.append(".. toctree::" + "\n")
            rstout.append(" :titlesonly:" + "\n")
            rstout.append(" :maxdepth: 4" + "\n\n")
            for n in self.nodes:
                if isinstance(n, System):
                    content = n.name + ".rst"
                    content = content.replace(' ', '_')
                    rstout.append(" " + content + "\n")
        if project > 0:
            rstout.append("\nDeveloped by Project:" + "\n")
            rstout.append("---------------------" + "\n\n")
            rstout.append(".. toctree::" + "\n")
            rstout.append(" :titlesonly:" + "\n")
            rstout.append(" :maxdepth: 4" + "\n\n")
            for n in self.nodes:
                if isinstance(n, Project):
                    content = n.name + ".rst"
                    content = content.replace(' ', '_')
                    rstout.append(" " + content + "\n")
        self.genRstBodyM(rstout, modules)

        for l in rstout:
            outfile.writelines(l)
        outfile.close()
        for n in self.nodes:
            n.genRst(self)

        os.system('sphinx-build -b html ' + Document.path + "/rst " + Document.path + "/html")
        print("")

    def genRstBodyM(self, rstOut, modules):
        rstOut.append("\n\n")
        rstOut.append("Source Code Documentation" + "\n")
        rstOut.append("=========================" + "\n\n")
        rstOut.append(".. toctree::" + "\n")
        rstOut.append("  :maxdepth: 4" + "\n\n")
        for module in modules:
            rstOut.append("  " + module + ".rst")
            rstOut.append("\n")
        rstOut.append("\n")
        rstOut.append("Indices and Tables" + "\n")
        rstOut.append("==================" + "\n\n\n")
        rstOut.append("* :ref:`genindex`" + "\n")
        rstOut.append("* :ref:`modindex`" + "\n")
        rstOut.append("* :ref:`search`" + "\n")
        rstOut.append("\n")


# World (Discourse Perspective)
class World(System):
    """
    This class represents the root of the RE tree. Think of it as the universe of discourse. It is the
    subject world which is relevant to the system to be developed. It embraces the system and its context.
    For instance, if the system to be  developed is a calender tool, the world could be described as
    *Personal Information Management*.
    """

    ID = 0  # world-unique ID

    def __init__(self, name):
        Node.__init__(self, name, None)

    def getID(self):
        self.ID += 1
        return self.ID


class Context(Node):  # related to a system
    pass


class Concept(Node):  # something in the context
    def __init__(self, name, description, parent=None):
        Node.__init__(self, name, parent)
        self.description = description


# -------------------------------------------------------------------------------------------------------------------
# Documents (Product Perspective)

class Project(Node):
    """ This class is the topmost element for organizing documentation. It contains Products.

    """
    def genRst(self, index):
        vDir = os.path.abspath(Document.path + "/rst/")
        filename = vDir + "/" + self.name
        filename = filename.replace(' ', '_')
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        opfile = filename + '.rst'
        outfile = open(opfile, 'w', encoding='utf-8')

        title = self.getType() + ' " ' + self.name + '"\n'
        rstout = [title, ("=" * (len(title) - 1)) + "\n\n"]
        sub = 0
        folder = 0
        product = 0
        workflow = 0
        for n in self.nodes:
            if isinstance(n, Project) and n is not index:
                sub += 1
            if isinstance(n, Folder):
                folder += 1
            if isinstance(n, Product):
                product += 1
            if isinstance(n, Workflow):
                workflow += 1
        product = product - folder
        if sub > 0:
            rstout.append("\nSub-Projects:" + "\n")
            rstout.append("-------------" + "\n\n")
            rstout.append(".. toctree::" + "\n")
            rstout.append(" :titlesonly:" + "\n")
            rstout.append(" :maxdepth: 4" + "\n\n")
            for n in self.nodes:
                if isinstance(n, Project) and self is not index:
                    content = n.name + ".rst"
                    content = content.replace(' ', '_')
                    rstout.append(" " + content + "\n")
        if folder > 0:
            rstout.append("\nFolder:" + "\n")
            rstout.append("-------" + "\n\n")
            rstout.append(".. toctree::" + "\n")
            rstout.append(" :titlesonly:" + "\n")
            rstout.append(" :maxdepth: 4" + "\n\n")
            for n in self.nodes:
                if isinstance(n, Folder):
                    content = n.name + ".rst"
                    content = content.replace(' ', '_')
                    rstout.append(" " + content + "\n")
        if product > 0:
            rstout.append("\nResults in:" + "\n")
            rstout.append("-----------" + "\n\n")
            rstout.append(".. toctree::" + "\n")
            rstout.append(" :titlesonly:" + "\n")
            rstout.append(" :maxdepth: 4" + "\n\n")
            for n in self.nodes:
                if isinstance(n, Product) and not isinstance(n, Folder):
                    content = n.name + ".rst"
                    content = content.replace(' ', '_')
                    rstout.append(" " + content + "\n")
        if workflow > 0:
            rstout.append("\nFollows:" + "\n")
            rstout.append("--------" + "\n\n")
            rstout.append(".. toctree::" + "\n")
            rstout.append(" :titlesonly:" + "\n")
            rstout.append(" :maxdepth: 4" + "\n\n")
            for n in self.nodes:
                if isinstance(n, Workflow):
                    content = n.name + ".rst"
                    content = content.replace(' ', '_')
                    rstout.append(" " + content + "\n")
        for l in rstout:
            outfile.writelines(l)
        outfile.close()
        for n in self.nodes:
            n.genRst(index)


class Product(Node):
    """ Base class for Products

    """


class Folder(Product):
    """ This class is a container for storing documents.

    """
    pass


class Document(Product):
    """This class presents a document in a RE process.

    This class is intended to derive classes, which represent particular documents types
    specific to an organization. For this purpose, put your chapter structure (represented as a list
    of lists) into the static variable 'chapterStructure' of your derived class. Also some defaults
    for parameters may be useful (refer to method/project example).

    :var name: name of the document
    :var typ: type of the document (as used in your organization)
    :var mnemonic: for naming elements of a document
    :var authors (list of lists): list of authors, each author is defined by list of strings including name,
         organization, etc.. Two or more authors from the same organization share a list item
    :var properties: optional settings (e.g., language) language = {english, german}, paper = {a4}
         font = {10pt, 11pt, 12pt}, default = {german, a4, 11pt}
    :var folder (node): folder in which the document is contained.
    """

    chapterStructure = []
    path = '../doc'
    imgPath = '../doc/images/'

    def __init__(self, name, typ, mnemonic, authors, properties, folder):
        Node.__init__(self, name, folder)
        self.typ = typ
        self.mnemonic = mnemonic
        self.authors = authors
        self.properties = properties
        self.addChaptersByName()

    def addChaptersByName(self):
        self.addChaptersByNameR(self.chapterStructure, self, self)

    def addChaptersByNameR(self, chapters, parent, pNode):
        if isinstance(chapters, list):
            parent = pNode
            if parent is None:  # a list cannot be followed by a list
                raise TypeError("addChaptersByName: misformed tree!")
            for c in chapters:
                pNode = self.addChaptersByNameR(c, parent, pNode)
            return None  # end of a list
        else:
            return Chapter(chapters, "", {}, parent)

    def getLabel(self):
        return self.mnemonic

    def dump(self):
        print('\n=======================================\n' + self.typ)
        print(self.name)
        Node.genTxt(self, 0, "")
        print('\n=======================================\n')

    def genPDF(self, overwrite=True, log=False):
        vDir = Document.path
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        vDir += "/pdf"
        filename = vDir + '/' + self.name
        filename = filename.replace(' ', '_')
        if not os.path.isdir(vDir):
            os.mkdir(vDir)

        if overwrite is False:
            n = 0
            while os.path.isfile(filename + '_' + str(n) + '.tex') is True:
                n += 1
            opfile = filename + '_' + str(n) + '.tex'
        else:
            opfile = filename + '.tex'
        outfile = open(opfile, 'w', encoding='utf-8')

        docAuthor = []
        for author in self.authors:
            docAuthor.append(r' \\ '.join(author))
        docPaper = 'a4paper'
        docLanguage = 'english'
        docFont = '11pt'
        if 'language' in self.properties and self.properties['language'] == 'german':
            docLanguage = 'ngerman'
        if 'font' in self.properties:
            docFont = self.properties['font']
        texout = [r'\documentclass[' + docPaper + ',' + docFont + ',' + docLanguage + r']{report}' + '\n',
                  r'\usepackage[utf8]{inputenc}' + '\n',
                  r'\usepackage[T1]{fontenc}' + '\n',
                  r'\usepackage{lmodern,textcomp}' + '\n',
                  r'\usepackage{graphicx}' + '\n',
                  r'\graphicspath{{' + Document.imgPath + r'}}' + '\n',
                  r'\usepackage[colorlinks, linkcolor = black, citecolor = black, filecolor = black, ' +
                  r'urlcolor = blue, bookmarks=true]{hyperref}' + '\n',
                  r'\usepackage{babel}' + '\n',
                  r'\usepackage{epstopdf}' + '\n',
                  r'\usepackage{tabularx}' + '\n',
                  r'\usepackage{tabulary}' + '\n',
                  r'\setcounter{secnumdepth}{5}' + '\n\n',
                  r'\begin{document}' + '\n',
                  r'\title{' + self.name + '}' + '\n',
                  r'\author{' + r' \and '.join(docAuthor) + r'}' + '\n',
                  r'\date{\today}' + '\n',
                  r'\maketitle' + '\n',
                  r'\tableofcontents' + '\n',
                  r'\listoffigures' + '\n',
                  r'\listoftables' + '\n\n']
        Node.genTeX(self, texout, 0, 1, "")
        texout.append(r'\end{document}' + '\n')
        for i in texout:
            if not isinstance(i, str):
                i = "\n".join(i)
            i = parseString(i)
            outfile.writelines(i)
        outfile.close()

        os.system('pdflatex -shell-escape -synctex=1 -interaction=batchmode -output-directory=../doc/pdf/ ' + opfile)
        print("")
        os.system('pdflatex -shell-escape -synctex=1 -interaction=batchmode -output-directory=../doc/pdf/ ' + opfile)
        print("")
        for tmpRoot, dirs, files in os.walk(Document.path + "/pdf"):
            for currentFile in files:
                if log is True:
                    exts = ['.aux', '.lof', '.out', '.toc', '.lot', '.gz']
                else:
                    exts = ['.aux', '.lof', '.out', '.toc', '.lot', '.gz', 'log']
                if any(currentFile.lower().endswith(ext) for ext in exts):
                    os.remove(os.path.join(tmpRoot, currentFile))

    def genRst(self, index):
        vDir = os.path.abspath(Document.path + "/rst/")
        filename = vDir + "/" + self.name
        filename = filename.replace(' ', '_')
        if not os.path.isdir(vDir):
            os.mkdir(vDir)
        opfile = filename + '.rst'
        outfile = open(opfile, 'w', encoding='utf-8')

        title = self.getType() + ' "' + self.name + '"\n'
        rstout = [title,
                  ("=" * (len(title) - 1)) + "\n\n"]
        content = self.name + ".pdf"
        content = content.replace(' ', '_')
        rstout.append(":download:`" + self.name + "<../pdf/" + content + ">`")
        self.genRstBody(rstout)

        for l in rstout:
            outfile.writelines(l)
        outfile.close()


class Element(Node):
    mnemonic = "ELEM"
    layoutProps = ['size', 'position']

    def __init__(self, name, properties=None, pNode=None):
        if properties is None:
            properties = {}
        Node.__init__(self, name, pNode)
        self.properties = properties

    def setNode(self, attribute, value):
        if attribute in self.properties:
            self.properties[attribute] = value
        else:
            Node.setNode(self, attribute, value)

    def buildNumber(self, index, number):
        if number != "":
            number += '-'
        number += str(index)
        return number

    def getText(self):
        return self.name

    def genTxt(self, index, number):
        number = self.buildNumber(index, number)
        print(number + ' ' + ' \'' + self.getText() + '\' (' + self.getLabel() + str(
            self.id) + ', ' + self.mnemonic + ')')
        if self.properties:
            for prop, value in self.properties.items():
                print("   " + str(prop) + ":\t" + str(value))  # TODO object names
        Node.genTxt(self, index, number)

    def headTeX(self, level, number):
        head = number + ' ' + self.name + ' (' + self.getLabel() + '-' + str(self.id) + ').'
        texout = [r'\noindent \textbf{' + getUnicodeStr(head) + '} ',
                  '\phantomsection \label{' + self.name + str(self.id) + '}']
        return texout

    def bodyTeX(self):
        return getUnicodeStr(self.getText()) + '\n'

    def tailTeX(self):
        texout = ['\n']
        if self.properties:
            for prop, value in self.properties.items():
                if not prop in self.layoutProps:  # do not print layout attributes
                    if not isinstance(value, str) and not type(value) is int and not type(value) is float:
                        if isinstance(value, list):
                            if isinstance(value[0], str) or type(value[0]) is int or type(value[0]) is float:
                                if isinstance(value[0], str) and value[0].find(r"/*/") != -1:
                                    texout.append(r'\indent \textit{' + str(prop) + '}:')
                                    tmp = []
                                    for pathnode in value:
                                        tmp.append(node(pathnode).name + "(" + node(pathnode).getLabel() + "-" +
                                                   str(node(pathnode).id) + ")" +
                                                   r' on page \pageref{' + node(pathnode).name +
                                                   str(node(pathnode).id) + '}')
                                    texout.append(", ".join(tmp))
                                else:
                                    texout.append(r'\indent \textit{' + str(prop) + '}: ' + ', '.join(map(str, value)))
                                    texout.append('\n')

                            else:
                                texout.append(r'\indent \textit{' + str(prop) + '}:')
                                tmp = []
                                for tmpnode in value:
                                    tmp.append(tmpnode.name + "(" + tmpnode.getLabel() + "-" +
                                               str(tmpnode.id) + ")" + r' on page \pageref{'
                                               + tmpnode.name + str(tmpnode.id) + '}')
                                texout.append(", ".join(tmp))
                            texout.append('\n')
                        else:
                            texout.append(r'\indent \textit{' + str(prop) + '}: ' + value.name + r' \pageref{'
                                          + value.name + str(value.id) + '}')
                            texout.append('\n')
                    else:
                        if str(value) != 'Information':  # do not print 'Type: Information'
                            texout.append(
                                r'\indent \textit{' + str(prop) + '}: ' + str(value) + '\n')  # TODO Object names
                            # else:
                            #texout.append(r'\vspace{1em}' + '\n\n')
            texout.append(r'\vspace{1em}' + '\n\n')
        texout.append('\n\n')
        return texout

    def genTeX(self, texAry, level, index, number):
        number = self.buildNumber(index, number)
        texAry.append(self.headTeX(level, number))
        texAry.append(self.bodyTeX())
        texAry.append(self.tailTeX())
        Node.genTeX(self, texAry, level, index, number)


class Link(Element):
    mnemonic = "LINK"

    def __init__(self, begin, end, name="", properties=None):  # a link is put under the begin node
        if properties is None:
            properties = {}
        Element.__init__(self, name, properties, begin)
        self.begin = begin
        self.end = end


class TextLink(Link):
    def bodyTeX(self):
        texOut = ['Link to \'' + getUnicodeStr(self.end.name) + '\' (' + self.end.getLabel + '-' + str(self.end.id),
                  r') on page \pageref{' + self.end.mnemonic + str(self.end.id) + '}' + '\n']
        return texOut


class TextElement(Element):
    """Abstract, derive all concrete textual constructs from here """
    mnemonic = "TEXT"

    def __init__(self, shortText, text, properties=None, pNode=None):
        if properties is None:
            properties = {}
        Element.__init__(self, shortText, properties, pNode)
        # self.text = ' '.join(text.split())  # remove unnecessary whitespaces in multi-line strings

        split = text.split("\n\n")
        out = []
        for splittext in split:
            if splittext.find("* ") == -1:
                out.append(' '.join(splittext.split()))
            else:
                out.append(splittext)
        text = "\n\n".join(out)
        self.text = text
        #TODO remove unnecessary whitespaces

    # self.text = Template(text)
    def getText(self):
        # return self.text.safe_substitute()
        return self.text


class Req(TextElement):
    """
    This element introduces a requirement in the RE tree. A requirement has a short name and a text describing
    the requirement.
    """

    def __init__(self, shortName, text, properties=None, pNode=None):
        if properties is None:
            properties = {}
        properties['Type'] = 'Requirement'
        TextElement.__init__(self, shortName, text, properties, pNode)


class Inf(TextElement):
    """
    This element introduces an information in the RE tree. An information has just a text.
    The short name is defaulted to 'Information'.
    """

    def __init__(self, text, properties=None, pNode=None):
        if properties is None:
            properties = {}
        properties['Type'] = 'Information'
        TextElement.__init__(self, properties['Type'], text, properties, pNode)


class Chapter(TextElement):
    """ This element introduces a chapter in the RE tree. A chapter has a name and an explanation ('meta text').
    A chapter helps to organize the information in a document. Higher level chapter structure is given by
    a document template. The lower level structure is project specific.
    """
    mnemonic = "HEAD"

    def __init__(self, heading, explanation="", properties=None, pNode=None):
        """Init chapter

        :param heading: short name of the table.
        :param explanation: optional description of the content of the chapter.
        :param properties: yet no special properties
        :param pNode: parent node
        """
        if properties is None:
            properties = {}
        properties['Type'] = 'Information'
        TextElement.__init__(self, heading, explanation, properties, pNode)
        self.content = None

    def addNode(self, n):
        """ In order to ensure a consistent numbering of elements, a chapter may contain
        either sub chapters or non-chapter elements (Req, ...), but not a mixture of both """
        if self.content is None:
            self.content = type(n).__name__
        else:
            if self.content == 'Chapter' and type(n).__name__ != 'Chapter':
                raise TypeError('\'' + n.name + '\' (Typ ' + type(n).__name__
                                + '): Only a chapter can be added to this chapter.')
            else:
                if self.content != 'Chapter' and type(n).__name__ == 'Chapter':
                    raise TypeError(n.name + ' (Typ ' + type(n).__name__
                                    + '): Only a non-chapter element can be added to this chapter.')
        Node.addNode(self, n)

    def getReference(self):
        return r" Chapter \ref{" + self.name + str(self.id) + "} " + self.name + "(" + self.getLabel() + "-" + \
            str(self.id) + ") " + r"on page \pageref{" + self.name + str(self.id) + "} "

    def buildNumber(self, index, number):
        if number != "":
            number += '.'
        number += str(index)
        return number

    def getText(self):
        return self.name

    def headTeX(self, level, number):
        name = getUnicodeStr(self.getText())
        texOut = []
        if level == 1:
            texOut.append('\chapter{' + name + '}\n')
        elif level == 2:
            texOut.append('\section{' + name + '}\n')
        elif level == 3:
            texOut.append('\subsection{' + name + '}\n')
        elif level == 4:
            texOut.append('\subsubsection{' + name + '}\n')
        elif level == 5:
            texOut.append('\paragraph{' + name + '}\n')
        else:
            texOut.append('\subparagraph{' + name + '}\n')
        texOut.append('\label{' + self.name + str(self.id) + '}\n\n')
        return texOut

    def bodyTeX(self):
        texOut = []
        if self.text != "":
            texOut.append(r'\noindent ' + ' (' + self.getLabel() + '-' + str(self.id) + '). ' + self.text + '\n\n')
        return texOut

    def tailTeX(self):
        if len(self.properties) > 1 or 'Type' not in self.properties:
            return Element.tailTeX(self)
        else:
            return [r'\indent' + '\n\n']


class Table(TextElement):
    """ Table is a simple table. That is, the whole table is treated as a single element of the RE tree.
    A table has the default type 'information'. """
    mnemonic = "TAB"

    def __init__(self, caption, table, text="", properties=None, pNode=None):
        """
        :param caption: short name of the table.
        :param table: a list, which contains a list for each row of the table.
        :param text: optional description of the table.
        :param properties:
            size = {fit, equal}, i.e. columns fit to content (default) or equal-sized
            position = {float, fixed}, i.e., table is floating to an layout optimal position
        :param pNode: parent node
        :return:
        """
        if properties is None:
            properties = {}
        if not 'Type' in properties:
            properties['Type'] = 'Information'
        TextElement.__init__(self, caption, text, properties, pNode)
        self.table = table

    def bodyTeX(self):
        texOut = []
        isFloat = 'position' in self.properties and self.properties['position'] == 'float'
        if isFloat:
            texOut.append(r'See Table \ref{tab:' + self.name + str(self.id) + '}. ')
        texOut.append(getUnicodeStr(self.getText()))
        if isFloat:
            texOut.append('\n' + r'\begin{table}[h!]' + '\n')
            texOut.append(r'\centering' + '\n')
        col = 'L'
        tabular = 'tabulary'
        if 'size' in self.properties and self.properties['size'] == 'equal':
            col = 'X'
            tabular = 'tabularx'
        tabspec = '|'
        for i in range(0, len(self.table[0])):
            tabspec += col + '|'
        texOut.append('\n\n' + r'\noindent\begin{' + tabular + r'}{\textwidth}{' + tabspec + '}\n')
        texOut.append(r'\hline' + '\n')
        head = True
        for line in self.table:
            texOut.append(' & '.join(line))
            texOut.append('\\\\ \n')
            if head:
                texOut.append(r'\hline' + '\n')
                head = False
            texOut.append(r'\hline' + '\n')
        texOut.append(r'\end{' + tabular + r'}' + '\n')
        if isFloat:
            texOut.append(r'\caption{' + self.name + '}\n')
            texOut.append(r'\label{tab:' + self.name + str(self.id) + '}\n')
            texOut.append(r'\end{table}' + '\n')
        texOut.append('\n')
        return texOut


class Figure(TextElement):
    """
    The figure element allows to add image files (.png, .jpg., .eps) to a document. The image has a caption
    and is referenced by a text element. A figure has the default type 'information'.
    """
    mnemonic = "FIG"

    def __init__(self, caption, figure, text="", properties=None, pNode=None):
        """
        :param caption: short name of the figure.
        :param figure: name of the image file (to be placed in the directory ./Doc/Images)
        :param text: description of the figure.
        :param properties: size = {'fit'}, i.e., image is shrinked/enlarged to fit page width
        :param pNode: parent node
        :return:
        """
        if properties is None:
            properties = {}
        if not 'Type' in properties:
            properties['Type'] = 'Information'
        TextElement.__init__(self, caption, text, properties, pNode)
        self.figure = figure

    def bodyTeX(self):
        options = []
        if 'size' in self.properties and self.properties['size'] == 'fit':
            options.append(r'width=\textwidth')
        texOut = []
        isFixed = 'position' in self.properties and self.properties['position'] == 'fixed'
        if not isFixed:
            texOut.append(r'See Figure \ref{fig:' + self.mnemonic + self.name + str(self.id) + '}. ')
        texOut.append(getUnicodeStr(self.getText()) + '\n\n')
        if not isFixed:
            texOut.append(r'\begin{figure}[h!]' + '\n')
            texOut.append(r'\centering' + '\n')
        texOut.append(r'\includegraphics[' + r', '.join(options) + ']{' + self.figure + '}\n')
        if not isFixed:
            texOut.append(
                r'\caption{' + self.name + '}\n')
            texOut.append(
                r'\label{fig:' + self.mnemonic + self.name + str(self.id) + '}\n')
            texOut.append(
                r'\end{figure}' + '\n\n')
        return texOut


class Model(Figure):
    """
    This is the base class for all requirements models. A model consists of model elements (e.g., in case of an
    ER-model 'entities' and 'relationships'). A PNG image of the requirements model will be created during LaTeX
    generation using the Graphviz dot language and according rendering. For this purpose all model elements must
    implement the genDot method. Overwrite the addNode() method inherited from Node to enforce well-formedness
    rules. A model has the default type 'requirement'. The difference between a model and a figure is that all
    elements of a model are visible in the RE tree and can be accessed (linked, checked, etc.)
    """
    mnemonic = "MOD"

    def __init__(self, caption, text="", properties=None, pNode=None):
        """
        :param caption: caption of the model (shown in the document)
        :param text: optional explanation of the model to be shown in the document
        :param properties: yet no special properties for models (rendering options envisioned)
        :param pNode: parent node
        :return:
        """
        if properties is None:
            properties = {}
        if not 'Type' in properties:
            properties['Type'] = 'Requirement'
        Figure.__init__(self, caption, None, text, properties, pNode)

    def bodyTeX(self):
        tmpname = self.name.replace(' ', '_')
        dot = Digraph(comment=tmpname)
        dot.format = 'eps'
        # dot.charset = 'UTF-8'
        self.genDot(dot)
        dot.render(Document.imgPath + tmpname, view=False)
        self.figure = tmpname + '.eps'
        return Figure.bodyTeX(self)

    def genTeX(self, texAry, level, index, number):
        number = self.buildNumber(index, number)
        texAry.append(self.headTeX(level, number))
        texAry.append(self.bodyTeX())
        texAry.append(self.tailTeX())
        # end of recursion, because a model is represented as Graphviz figure in LaTeX


class ModelElement(Element):
    """ This is the base class for model elements. Derive all specific model elements from here.
    A derived class must implement genDot to provide if Graphviz rendering. """
    pass


class ModelLink(Link):
    """ This is the base class for model links. A model link is a connection between two model elements.
    Derive all model links from here. A derived class must implement genDot to provide if Graphviz rendering. """
    pass


# -------------------------------------------------------------------------------------------------------------------


class GenericModel(Model):
    """ The Generic Model is a a very simple model for expressing requirements models
    using boxes, circles, lines, and arrows. Special semantics are not enforced. """
    pass


class Box(ModelElement):
    def genDot(self, dot):
        dot.node(str(self.id), self.name, fillcolor='white', style='filled', fontsize='11', shape='box')
        Element.genDot(self, dot)


class Circle(ModelElement):
    def genDot(self, dot):
        dot.node(str(self.id), self.name, fillcolor='white', style='filled', fontsize='11', shape='circle')
        Element.genDot(self, dot)


class Line(ModelLink):
    def genDot(self, dot):
        dot.edge(str(self.begin.id), str(self.end.id), dir='none')
        Link.genDot(self, dot)


class Arrow(ModelLink):
    def genDot(self, dot):
        dot.edge(str(self.begin.id), str(self.end.id), constraint='true')
        Link.genDot(self, dot)


# -------------------------------------------------------------------------------------------------------------------
# Engineering (Process Perspective)

class Workflow(Node):  # related to Project
    pass


class Activity(Node):  # contained in a workflow
    """Describes a step in a workflow.
        
    An Activity can be an automatic Algorithm of an Requirements Engineering Method
    or a description how this Activity shout be done.

    :var name (str): Name of the Activity.
    :var guideline (list of str): List of Guidelines of the Activity.
    :var parent (node): Parent Node in the RE-Process-Tree.
    """

    def __init__(self, name, guideline, pNode=None):
        """Constructor of the Activity class.
            
        :param name (str): Name of the Activity.
        :param guideline (list of str): List of Guidelines of the Activity.
        :param parent (node): Parent Node in the RE-Process-Tree.
            
        """
        Node.__init__(self, name, pNode)
        self.guideline = guideline

    def do(self):
        """Some Method that do something
        
        """
        pass

    def dump(self):
        """Prints the Activity to console
        """
        print('Activity: ' + self.name + ': ' + "".join(self.guideline))
        Node.dump(self)

    def genRstBody(self, rstOut):
        rstOut.append("\n\n\n")
        rstOut.append(self.guideline + "\n")


# Quality

class Quality(object):
    pass


class Traceable(Quality):
    def measure(self):
        pass  # die Idee ist, verschiedene Metriken zu definieren
