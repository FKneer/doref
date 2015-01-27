#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ieee830 import *
from istar import *
from ref import *

w = World("Office Automation")
cd("./-")
System("Meeting Scheduler System")
cd("./-")
Project("Meeting Scheduler Development")
cd("./-")
Workflow("Goal-oriented RE")
cd("./-")
Activity("Initiate RE Project", "In this activity, the folder structure and the (empty) documents are created.")

cd("/*/Meeting Scheduler/*/Meeting Scheduler Development")
# Folder("Protocols")
Folder("Specifications")
cd("./-")
IEEE830SRS("Software Requirements for Meeting Scheduler System",
           [["Erik Kamsties and Fabian Kneer", "RE Research Group", "FH Dortmund"]],
           {'language': 'english', 'paper': 'a4', 'font': '10pt'})

cd("/*/Meeting Scheduler/*/Meeting Scheduler Development")

Activity("Specify initial requirements", "", node("/*/Goal-oriented RE"))

cd("/*/Purpose")
Inf('''
This preliminary description is deliberately intended to be sketchy and unprecise. Acquisition, formalization and
validation processes are needed to complete it and lift the many shadow areas.''')

Inf('''
A number of features of the Meeting Scheduler System were inspired from various experiences in organizing meetings
(faculty meetings, ESPRIT project meetings, Program Committee meetings, etc.) and from various discussions with
Steve Fickas' group at the University of Oregon.''')

Inf('''
The textual description in this document was prepared by Axel van Lamsweerde and updated by Mary Shaw.
''')

cd("/*/System Overview")
Chapter("Scheduling Meetings: Domain Theory")
cd("./-")
Inf('''
Meetings are typically arranged in the following way. A *meeting initiator* asks all potential meeting attendees
for the following information based on their personal agenda:

* a set of dates on which they cannot attend the meeting (hereafter referred as *exclusion set* );
* a set of dates on which they would prefer the meeting to take place (hereafter referred
  as *preference set* ).
''')

Inf('''
A meeting date is defined by a pair (calendar date, time period). The exclusion and preference sets are contained
in some time interval prescribed by the meeting initiator (hereafter referred as date range).
''')

Inf('''
The initiator also asks active participants to provide any special equipment requirements on the meeting location
(e.g., overhead-projector, workstation, network connection, telephones, etc.); he/she may also ask important
participants to state preferences about the meeting location.
''')

Inf('''
The proposed meeting date should belong to the stated date range and to none of the exclusion sets; furthermore it
should ideally belong to as many preference sets as possible. A date conflict occurs when no such date can be found.
''')

Inf('''A conflict is strong when no date can be found within the date range and outside all exclusion sets; it is weak
when dates can be found within the date range and outside all exclusion sets, but no date can be found at the
intersection of all preference sets.''')

Inf('''Conflicts can be resolved in several ways:

* the initiator extends the date range;
* some participants remove some dates from their exclusion set;
* some participants withdraw from the meeting;
* some participants add some new dates to their preference set.

''')

Inf('''
A meeting room must be available at the selected meeting date. It should meet the equipment requirements;
furthermore it should ideally belong to one of the locations preferred by as many important participants
as possible. A new round of negotiation may be required when no such room can be found.
''')

Inf('''
The meeting initiator can be one of the participants or some representative (e.g., a secretary).
''')

cd("/*/Product Functions")  # System requirements
Req("Purpose", '''
The purpose of the meeting scheduler system is to support the organization of meetings - that is, to determine,
for each meeting request, a meeting date and location so that most of the intended participants will effectively
participate.
''')

Req("Convenience", '''
The meeting date and location should thus be as convenient as possible to all participants.
''')

Req("Early", '''
Information about the meeting should also be made available as early as possible to all potential participants.
''')

Req("Reduce Overhead", '''
The intended system should considerably reduce the amount of overhead usually incurred in organizing meetings
where potential attendees are distributed over many different places. On another hand, the system should reflect
as closely as possible the way meetings are typically managed (see the domain theory above).
''')

Req("Activities", '''
The system should assist users in the following activities.''')
cd("./-")

Req("Contraints", '''
    Plan meetings under the constraints expressed by participants
''')

Req("Replan", '''
    Replan a meeting dynamically to support as much flexibility as possible. On one hand, participants should be
    allowed to modify their exclusion set, preference set and/or preferred location before a meeting date/location
    is proposed. On the other hand, it should be possible to take some external constraints into account after
    a date and location have been proposed - e.g., due to the need to accommodate a more important meeting.
    The original meeting date or location may then need to be changed; sometimes the meeting may even be
    cancelled. In all cases some bound on replanning should be set up.
''')

Req("Conflict resolution", '''
    Support conflict resolution according to resolution policies stated by the client.
''')

Req("Interactions", '''
    Manage all the interactions among participants required during the organization of the meeting - to communicate
    requests, to get replies even from participants not reacting promptly, to support the negotiation and conflict
    resolution processes, to make participants aware of what's going on during the planning process, to keep
    participants informed about schedules and their changes, to make them confident about the reliability of the
    communications, etc..

    Keep the amount of interaction among participants (e.g., number and length of messages, amount of negotiation
    required) as small as possible.
''')

cd("..")

Req("Several requests", '''
The meeting scheduler system must in general handle several meeting requests in parallel. Meeting requests can be
competing by overlapping in time or space. Concurrency must thus be managed.
''')

Req("Aspects", '''
The following aspects should also be taken into account.
''')

cd("./-")
Req("Decentralized requests", '''
    The system should accomodate decentralized requests; any authorized user should be able to request a meeting
    independently of his whereabouts.
''')

Req("Physical constraints", '''
    Physical constraints may not be broken - e.g., a person may not be at two different places at the same time,
    a meeting room may not be allocatable.
''')

Req("Performance", '''
    The system should provide an appropriate level of performance, for example:

        the elapsed time between the submission of a meeting request and the determination of the corresponding
        meeting date/location should be as small as possible;

        the elapsed time between the determination of a meeting date/location and the communication of this
        information to all participants concerned should be as small as possible;

        a lower bound should be fixed between the time at which the meeting date is determined and the time at which
        the meeting is actually taking place.
''')

Req("Privacy", '''
    Privacy rules should be enforced; a non-privileged participant should not be aware of constraints stated by
    other participants.
''')

Req("Usability", '''
    The system should be usable by non-experts.
''')

Req("Customizable", '''
    The system should be customizable to professional as well as private meetings. These two modes of use are
    characterized by different restrictions on the time periods that may be allocated (e.g., meetings during office
    hours, private activities during leisure time).
''')

Req("Flexible", '''
    The system should be flexible enough to accommodate evolving data - e.g., the sets of concerned participants may
    be varying, the address at which a participant can be reached may be varying, etc.
''')

Req("Expandable", '''
    The system should be easily extendable to accommodate the following typical variations:

    * handling of explicit status and priorities among participants;
    * handling of explicit priorities among dates in preference sets;
    * handling of explicit dependencies between meeting date and meeting location;
    * participation through delegation - a participant may ask another person to represent him/her at the meeting;
    * partial attendance - a participant can only attend part of the meeting;
    * variations in date formats, address formats, interface language, etc.
    * partial reuse in other contexts -e.g., to help establish course schedules.

''')

cd("/*/Goal-oriented RE")
DevelopGoalModel("Develop Goal Model Meeting Scheduler")
cd("./-")
DevelopSDModel("Develop SD-Model")
cd("./-")
DevelopActor("Find and model Actors")

cd("/*/Specific Requirements/*/Functional Requirements")
Chapter("Goal Model")
cd("./-")

GoalModel("SD-Model of Meeting Scheduler",
          "This model shows a Strategic Dependency (SD) model of the meeting scheduler.",
          {'size': 'fit'})
cd("./-")
Actor("Meeting Initiator", "The Meeting Initiator organizes a meeting (see Domain Theory). The Strategic "
                           "Resource (SR) model shows the resources of the Meeting Initiator.", {'size': 'fit'})
Actor("Meeting Participant", "The participant shall attend a meeting.", {'size': 'fit'})
Actor("Meeting Scheduler", "The system which shall support the Meeting Initiator to organize meetings.",
      {'size': 'fit'})

cd('/*/Develop SD-Model')
DevelopDependency("Find and model Dependencies between Actors")

cd('/*/SD-Model of Meeting Schedule')
Goal("Attends Meeting D")
Goal("Meeting Be Scheduled D")
Task("Enter Date Range D")
Task("Enter Avail Dates D")
Resource("Proposed Date D")
Resource("Agreement D")

DependencyLink(node("/*/SD-Model/*/Meeting Scheduler"), node("/*/Meeting Initiator"), node("/*/Meeting Be Scheduled D"))
DependencyLink(node("/*/SD-Model/*/Meeting Scheduler"), node("/*/Meeting Participant"), node("/*/Proposed Date D"))

DependencyLink(node("/*/Meeting Initiator"), node("/*/SD-Model/*/Meeting Scheduler"), node("/*/Enter Date Range D"))

DependencyLink(node("/*/Meeting Participant"), node("/*/SD-Model/*/Meeting Scheduler"), node("/*/Enter Avail Dates D"))
DependencyLink(node("/*/Meeting Participant"), node("/*/SD-Model/*/Meeting Scheduler"), node("/*/Agreement D"))
DependencyLink(node("/*/Meeting Participant"), node("/*/Meeting Initiator"), node("/*/Attends Meeting D"))

cd("/*/Develop Goal Model Meeting Scheduler")
DevelopSRModel("Develop SR-Model Meeting Initiator")
cd("/*/Meeting Initiator")

Task("Organize Meeting")

Goal("Meeting Be Scheduled")
DecompositionLink(node('/*/Meeting Be Scheduled'), node('/*/Organize Meeting'))

SoftGoal("Quick")
DecompositionLink(node('/*/Quick'), node('/*/Organize Meeting'))

SoftGoal("Low Effort")
DecompositionLink(node('/*/Low Effort'), node('/*/Organize Meeting'))

Task("Schedule Meeting")
MeanEndLink(node('/*/Schedule Meeting'), node('/*/Meeting Be Scheduled'))

Task("Let Scheduler Schedule Meeting")
MeanEndLink(node('/*/Let Scheduler Schedule Meeting'), node('/*/Meeting Be Scheduled'))

ContributionLink(node('/*/Schedule Meeting'), node('/*/Quick'), "HURT")
ContributionLink(node('/*/Let Scheduler Schedule Meeting'), node('/*/Quick'), "HELP")
ContributionLink(node('/*/Schedule Meeting'), node('/*/Low Effort'), "HURT")
ContributionLink(node('/*/Let Scheduler Schedule Meeting'), node('/*/Low Effort'), "HELP")

cd("/*/Develop Goal Model Meeting Scheduler")
DevelopSRModel("Develop SR-Model Meeting Participant")

cd("/*/Meeting Participant")

Task("Participate In Meeting")

Task("Attend Meeting")
DecompositionLink(node("/*/Attend Meeting"), node("/*/Participate In Meeting"))

SoftGoal("Convenient (Meeting, Date)")
DecompositionLink(node("/*/Convenient (Meeting, Date)"), node("/*/Participate In Meeting"))

Task("Arrange Meeting")
DecompositionLink(node("/*/Arrange Meeting"), node("/*/Participate In Meeting"))

SoftGoal("Low Effort")
DecompositionLink(node("/*/Meeting Participant/*/Low Effort"), node("/*/Arrange Meeting"))

Goal("Agreeable (Meeting, Date)")
DecompositionLink(node("/*/Agreeable (Meeting, Date"), node("/*/Arrange Meeting"))

Task("Find Agreeable Date By Talking To Initiator")
MeanEndLink(node("/*/Find Agreeable Date By Talking To Initiator"), node("/*/Agreeable (Meeting, Date)"))

Task("Find Agreeable Date Using Scheduler")
MeanEndLink(node("/*/Find Agreeable Date Using Scheduler"), node("/*/Agreeable (Meeting, Date)"))

Task("Agree To Date")
DecompositionLink(node("/*/Agree To Date"), node("/*/Find Agreeable Date Using Scheduler"))

SoftGoal("Quality (Proposed Date)")
ContributionLink(node("/*/Quality (Proposed Date)"), node("/*/Convenient (Meeting, Date)"), "HELP")

SoftGoal("Richer Medium")
ContributionLink(node("/*/Richer Medium"), node("/*/Quality (Proposed Date)"), "HELP")

ContributionLink(node("/*/Find Agreeable Date Using Scheduler"), node("/*/Richer Medium"), "HURT")
ContributionLink(node("/*/Find Agreeable Date By Talking To Initiator"), node("/*/Richer Medium"), "HELP")

SoftGoal("User Friendly")
ContributionLink(node("/*/User Friendly"), node("/*/Meeting Participant/*/Low Effort"), "HELP")

ContributionLink(node("/*/Find Agreeable Date Using Scheduler"), node("/*/User Friendly"), "HURT")
ContributionLink(node("/*/Find Agreeable Date By Talking To Initiator"), node("/*/User Friendly"), "HELP")

cd("/*/Develop Goal Model Meeting Scheduler")
DevelopSRModel("Develop SR-Model Meeting Scheduler")

cd("/*/SD-Model of Meeting Schedule/*/Meeting Scheduler")

Task("Schedule Meeting")

Task("Obtain Agreement")
DecompositionLink(node('/*/Obtain Agreement'),
                  node('/*/SD-Model of Meeting Schedule/*/Meeting Scheduler/*/Schedule Meeting'))

Task("Obtain Avail Dates")
DecompositionLink(node('/*/Obtain Avail Dates'),
                  node('/*/SD-Model of Meeting Schedule/*/Meeting Scheduler/*/Schedule Meeting'))

Goal("Find Agreeable Slot")
DecompositionLink(node('/*/Find Agreeable Slot'),
                  node('/*/SD-Model of Meeting Schedule/*/Meeting Scheduler/*/Schedule Meeting'))

Task("Merge Avail Dates")
MeanEndLink(node('/*/Merge Avail Dates'), node('/*/Find Agreeable Slot'))

cd("/*/SD-Model of Meeting Schedule")

refineDependency(node("/*/Meeting Be Scheduled D"), node("/*/SD-Model/*/Meeting Scheduler/*/Schedule Meeting"),
                 node("/*/Let Scheduler Schedule Meeting"))
refineDependency(node("/*/Proposed Date D"),
                 node("/*/SD-Model of Meeting Schedule/*/Meeting Scheduler/*/Schedule Meeting"),
                 node("/*/Agree To Date"))

refineDependency(node("/*/Enter Date Range D"), node("/*/Let Scheduler Schedule Meeting"),
                 node("/*/SD-Model of Meeting Schedule/*/Meeting Scheduler/*/Schedule Meeting"))

refineDependency(node("/*/Enter Avail Dates D"), node("/*/Find Agreeable Date Using Scheduler"),
                 node("/*/Obtain Avail Dates"))
refineDependency(node("/*/Agreement D"), node("/*/Agree To Date"), node("/*/Obtain Agreement"))
refineDependency(node("/*/Attends Meeting D"), node("/*/Attend Meeting"), node("/*/Organize Meeting"))

w.genPDF()

cd("/*/Goal-oriented RE")
EvaluateGoalModel("Evaluate Goal Model")
cd("./-")

FindLeafs("Find Leaves for Analysis", goalModel=node("/*/SD-Model of Meeting Schedule")).do()
FindRoot("Find Root", goalModel=node("/*/SD-Model of Meeting Schedule")).do()

SetLabels("Set initial values of labels", labelList={
    '/*/Proposed Date D': 'Satisfied',
    '/*/Schedule Meeting': 'Denied',
    '/*/Merge Avail Dates': 'Satisfied',
    '/*/Attend Meeting': 'Satisfied',
    '/*/Find Agreeable Date By Talking To Initiator': 'Satisfied'}).do()

PropagateLabels("Initially Propagate Labels", goalModel=node("/*/SD-Model of Meeting Schedule")).do()

MakeJudgements("Make judgement after inspection of goal model", labelList={
    '/*/Meeting Participant/*/User Friendly': 'Conflict',
    '/*/Meeting Participant/*/Richer Medium': 'Conflict',
    '/*/Meeting Initiator/*/Low Effort': 'Partially Satisfied',
    '/*/Meeting Initiator/*/Quick': 'Partially Satisfied'})

PropagateLabels("First Propagate Labels after Human Judgement", goalModel=node("/*/SD-Model of Meeting Schedule"))

Show("/*/SD-Model")
Show("/*/SD-Model/*/Meeting Scheduler")
Show("/*/Meeting Participant")
Show("/*/Meeting Initiator")

#node("/").genHTML(["ref", "istar", "ieee830"])
