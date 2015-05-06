#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description
===========
This module implements a GUI to show the structure of the RE tree of a project.
To show the Tree use the following function ::

    ShowTree(node)

as an example ::

    ShowTree(node("/"))

This will open an window with the structure from the root to the leafs of the Tree.
If you only want to show the structure of an generated document, use the node of the document as a method parameter ::

    ShowTree(node("/*/Software Requirements for Meeting Scheduler System"))

'''

import tkinter as tk
import tkinter.ttk as ttk
from ref import *


class ShowTree:
    def __init__(self, root):
        self.root = tk.Tk()
        self.root.title("RE Tree")
        self.tree = ttk.Treeview()
        self.tree.pack(fill="both", expand="YES")
        self.world = root
        parent = self.tree.insert("", "end", text=root.getType() + ": " + root.name)
        for itr_node in root.nodes:
            newparent=self.tree.insert(parent, "end", text=itr_node.getType() + ": " + itr_node.name)
            self.insertNode(newparent, itr_node)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.root.mainloop()

    def insertNode(self, parent, childnode):
        for itr_node in childnode.nodes:
            newparent = self.tree.insert(parent, "end", text=itr_node.getType() + ": " + itr_node.name)
            self.insertNode(newparent, itr_node)

    def OnDoubleClick(self, event):
        item = self.tree.identify('item',event.x,event.y)
        print("you clicked on", self.tree.item(item, "text"))
