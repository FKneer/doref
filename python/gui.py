#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from ref import *


class ShowTree:
    def __init__(self, world):
        self.root = tk.Tk()
        self.tree = ttk.Treeview()
        self.tree.pack(fill="both", expand="YES")
        self.world = world
        parent = self.tree.insert("", "end", text=world.name)
        for itr_node in world.nodes:
            newparent=self.tree.insert(parent, "end", text=itr_node.name)
            self.insertNode(newparent, itr_node)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.root.mainloop()

    def insertNode(self, parent, childnode):
        for itr_node in childnode.nodes:
            newparent = self.tree.insert(parent, "end", text=itr_node.name)
            self.insertNode(newparent, itr_node)

    def OnDoubleClick(self, event):
        item = self.tree.identify('item',event.x,event.y)
        print("you clicked on", self.tree.item(item,"text"))
