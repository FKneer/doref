__author__ = 'kamsties'

from ieee830 import *
from gui import *
from datamodel import *

World("Smart Business")
cd("./-")
System("Hotel System")
cd("./-")
Project("Hotel System Redesign")
cd("./-")
Folder("Specifications")
cd("./-")

IEEE830SRS("Product Requirements for a Hotel System",
           [["Erik Kamsties", "RE Course 2015", "FH Dortmund"]],
           {'language': 'english', 'paper': 'a4', 'font': '10pt'})

cd("/*/Product Functions")
Chapter("Markup Language")

cd("./-")
Req("GFM Marddown", "The system supports Git-flavored Markdown.")

cd("/*/Logical Database Requirement")

DataItem("Guest",
         desc="A guest is a person is the person or company who has to pay the bill. A person has one or more stay "
                "records. A company may have none [b, c]. Customer is a synonym for guest, but in the database we only "
                "use guest [a]. The persons staying in the rooms are also called guests, but are not guests in the "
                "database terms.",
         expl=["A guest who stays one night.",
          "A company with employees staying now and then, each of them with his own stay record where his name is "
          "recorded [d]"],
         attr=[
             ["name", "Text: 50 chars [h]",
              "The name stated by the guest [f]. For companies the official name since the bill is sent there [g]. Longer   "
              "names exist, but better truncate at registration time that at print out time [g, j]"],
             ["passport", "Text, 16 chars [h]",
              "Recorded for guests who are obviously foreigners [f, i]. Used for police reports in case the guest doesn't pay "
              "[g] ..."]
         ])

DataItem('Stay',
    attr = [
        ["stay#", "", ""],
        ["paymethod", "", ""],
        ["employees", "", ""]
    ])

DataItem('RoomState',
    attr = [
        ["date"],
        ["n_persons", "", ""],
        ["state", "enum{booked|occupied|repair}", ""]
    ])

DataItem('Room',
    attr = [
        ["room#"],
        ["n_beds", ""],
        "type",
        ["price1", "", ""],
        ["price2", "", ""]
    ])

DataItem('Service',
    attr = [
        ["date", "", ""],
        ["count", "", ""]
    ])

DataItem('ServiceType',
    attr = [
        ["name", "", ""],
        ["price", "", ""]
    ])

DataModel("Hotel System", """
    Guest "1" -- "n" Stay
    Stay "1" -- "n" RoomState
    RoomState "n" -- "1" Room
    Stay "1" -- "n" Service
    Service "n" -- "1" ServiceType
""", "This diagram shows the relations between the major data items of the application")

Req('Booking', '''
A Guest books a room.
''')

node("/").genPDF()

ShowTree(node("/"))

