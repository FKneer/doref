#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Quick Start Guide for iStar
===========================


1. Purpose
----------

1.1 Education
^^^^^^^^^^^^^

    The i* Quick Guide is intended to be both an introduction to i* for new users and a reference guide for experienced
    users. It is intended to be brief and readable, without an in depth exploration of the motivations for, usage, and
    underlying philosophies of the i* Framework.

1.2 Collaboration
^^^^^^^^^^^^^^^^^

    As this guide is intended to be part of the i* collaborative wiki we encourage feedback and collaboration in terms
    of suggesting alternative i* syntax and semantics, including extensions to the Framework. However, in order to keep
    the Quick Guide brief and easily understandable, we suggest collecting i* adaptations, expansions, and further
    examples in separate document(s), namely the istarSyntaxVariations? page. If enough variations ends.jpg"}
    of i* usage are collected, this can facilitate interesting and useful comparisons.


2. Basic i* Notation
--------------------

    This section provides only the graphical notation of i* syntax. An explanation of each notation can be found in the
    i* Glossary Section. Note that as i* models can be created by a variety of software tools, there can be small
    variations in notation appearance, mainly pertaining to color and line size.

2.1 Actors
^^^^^^^^^^
    .. figure:: ../../python/_istar/actor.gif
        :width: 25%
        :scale: 50%
    .. figure:: ../../python/_istar/agent.gif
        :width: 25%
        :scale: 50%
    .. figure:: ../../python/_istar/position.gif
        :width: 25%
        :scale: 50%
    .. figure:: ../../python/_istar/role.gif
        :width: 25%
        :scale: 50%

    .. figure:: ../../python/_istar/actorboundary.gif
        :scale: 50%

2.2 Actor Associations
^^^^^^^^^^^^^^^^^^^^^^

    .. figure:: ../../python/_istar/isa.gif
        :width: 30%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/ispartof.gif
        :width: 30%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/plays.gif
        :width: 30%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/covers.gif
        :width: 30%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/occupies.gif
        :width: 30%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/ins.gif
        :width: 30%
        :scale: 50%
        :align: left


2.3 Elements
^^^^^^^^^^^^

    .. figure:: ../../python/_istar/goal.gif
        :width: 25%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/task.gif
        :width: 25%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/resource.gif
        :width: 25%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/softgoal.gif
        :width: 25%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/belief.gif
        :width: 25%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/belief2.gif
        :width: 25%
        :scale: 50%
        :align: left

2.4 Links
^^^^^^^^^

    .. figure:: ../../python/_istar/dependencylink.gif
        :width: 30%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/meansendslink.jpg
        :width: 30%
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/decomposition.jpg
        :width: 30%
        :scale: 50%
        :align: left


2.5 Contribution Links
^^^^^^^^^^^^^^^^^^^^^^

    .. figure:: ../../python/_istar/contribuitonlinks.jpg
        :scale: 50%
        :align: left


2.6 Strategic Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. figure:: ../../python/_istar/goaldependency.gif
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/taskdependency.gif
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/resourcedependency.gif
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/softgoaldependency.gif
        :scale: 50%
        :align: left


2.7 Dependency Strengths
^^^^^^^^^^^^^^^^^^^^^^^^

    .. figure:: ../../python/_istar/dependencystrengths.jpg
        :scale: 50%
        :align: left


2.8 SR Decomposition Links
^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. figure:: ../../python/_istar/taskdecomposition.gif
        :scale: 50%
        :align: left


2.9 SR Means-End Links
^^^^^^^^^^^^^^^^^^^^^^

    .. figure:: ../../python/_istar/meansends.gif
        :scale: 50%
        :align: left


2.10 Contributions
^^^^^^^^^^^^^^^^^^

    .. figure:: ../../python/_istar/contributions.gif
        :scale: 50%
        :align: left



3. i* Glossary
--------------

3.1 Strategic Dependency (SD) Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Set of nodes and links where each node represents an actor and each link between two actors indicates that one
    actor depends on the other for something in order that the former may attain some goal. The SD model is used to
    express the network of intentional, strategic relationships among actors.

3.1.1 Actors

    Active entities that carries out actions to achieve goals by exercising its know-how. We use the term actor to
    refer generically to any unit to which intentional dependencies can be ascribed. Agents, roles and positions are
    sub-units of a complex social actor, each of which is an actor in a more specialized sense.

    .. figure:: ../../python/_istar/actor.gif
        :scale: 50%
        :align: left



3.1.1.1 Role

    Abstract characterization of the behavior of a social actor within some specialized context or domain of endeavor.
    Its characteristics are easily transferable to other social actors. The dependencies associated with a role apply
    regardless of the agent who plays the role.

    .. figure:: ../../python/_istar/role.gif
        :scale: 50%
        :align: left


3.1.1.2 Agent

    Actor with concrete, physical manifestations, such as a human individual. We use the term agent instead of person
    for generality, so that it can be used to refer to human as well as artificial (hardware/software agents). An agent
    has dependencies that apply regardless of what roles he/she/it happens to be playing. These characteristics are
    typically not easily transferable to other individuals, e.g. its skills and experiences, and its physical
    limitations.

    .. figure:: ../../python/_istar/agent.gif
        :scale: 50%
        :align: left


3.1.1.3 Position

    Intermediate abstraction that can be used between a role and an agent. It is a set of roles typically played by
    one agent (e.g., assigned jointly to that one agent). We say that an agent occupies a position. A position is said
    to cover a role.

    .. figure:: ../../python/_istar/position.gif
        :scale: 50%
        :align: left


3.1.2 Actor Association Links

    The relationships between actors are described by graphical association links between actors.

3.1.2.1 Is-part-of (Part) Association

    Roles, positions, and agents can each have subparts. Aggregate actors are not compositional with respect to
    intentionality. Each actor, regardless of whether it has parts, or is part of a larger whole, is taken to be
    intentional. There can be intentional dependencies between the whole and its parts, e.g., a dependency by the hole
    on its parts to maintain unity.

    .. figure:: ../../python/_istar/ispartof.gif
        :scale: 50%
        :align: left


3.1.2.2 ISA Association

    The is_a association represents a generalization, with an actor being a specialized case of another actor. Both ISA
    and Is-part-of can be applied between any two instances of the same type of actor.

    .. figure:: ../../python/_istar/isa.gif
        :scale: 50%
        :align: left


3.1.2.3 Plays Association

    The plays association is used between an agent and a role, with an agent playing a role. The identity of the agent
    who plays a role should have no effect on the responsibilities of that role, and similarly, aspects of an agent
    should be unaffected by the roles it plays.

    .. figure:: ../../python/_istar/plays.gif
        :scale: 50%
        :align: left


3.1.2.4 Covers Relationship

    The association link covers is used to describe the relationship between a position and the roles that it covers.

    .. figure:: ../../python/_istar/covers.gif
        :scale: 50%
        :align: left


3.1.2.5 Occupies Relationship

    The occupies link is used to show that an agent occupies a position, meaning that it plays all of the roles that
    are covered by the position.

    .. figure:: ../../python/_istar/occupies.gif
        :scale: 50%
        :align: left



3.1.2.6 INS Relationship

    The ins association, representing instantiation, is used to represent a specific instance of a more general entity.
    An agent is an instantiation of another agent.

    .. figure:: ../../python/_istar/ins.gif
        :scale: 50%
        :align: left



3.1.3 Strategic Dependencies

    Dependee
    Actor who is depended upon on a dependency relationship.

    Depender
    The depending actor on a dependency relationship.

    Dependum
    Element around which a dependency relationship centers.

    We distinguish among four types of dependencies, based on the type of the dependum: Resource dependency, Task
    dependency, Goal dependency, Softgoal dependency.

3.1.3.1 Goal Dependency

    In a goal dependency, the depender depends on the dependee to bring about a certain state of affairs in the world.
    The dependum is expressed as an assertion statement. The dependee is free to, and is expected to, make whatever
    decisions are necessary to achieve the goal (namely, the dependum). The depender does not care how the dependee
    goes about achieving the goal.

    .. figure:: ../../python/_istar/goaldependency.gif
        :scale: 50%
        :align: left



3.1.3.2 Task Dependency

    In a task dependency, the depender depends on the dependee to carry out an activity. The dependum names a task
    which specifies how the task is to be performed, but not why. The depender has already made decisions about how
    the task is to be performed. Note that a task description in i* is not meant to be a complete specification of the
    steps required to execute the task. It is a constraint imposed by the depender on the dependee. The dependee still
    has freedom of action within these constraints.

    .. figure:: ../../python/_istar/taskdependency.gif
        :scale: 50%
        :align: left



3.1.3.3 Resource Dependency

    In a resource dependency, the depender depends on the dependee for the availability of an entity (physical or
    informational). By establishing this dependency, the depender gains the ability to use this entity as a resource.
    A resource is the finished product of some deliberation-action process. In a resource dependency, it is assumed
    that there are no open issues to be addressed or decisions to be made.

    .. figure:: ../../python/_istar/resourcedependency.gif
        :scale: 50%
        :align: left



3.1.3.4 Softgoal Dependency

    In a softgoal dependency, a depender depends on the dependee to perform some task that meets a softgoal. A softgoal
    is similar to a goal except that the criteria of success are not sharply defined a priori. The meaning of the
    softgoal is elaborated in terms of the methods that are chosen in the course of pursuing the goal. The depender
    decides what constitutes satisfactory attainment of the goal, but does so with the benefit of the dependee's know
    how.

    .. figure:: ../../python/_istar/softgoaldependency.gif
        :scale: 50%
        :align: left


3.1.4 Vulnerability

    Vulnerability is implied with Dependency Link(s). The dependency link represents that the depender, by depending on
    the actor who is the dependee, is able to achieve goals that it was not able to achieve before, or not as well, or
    not as quick. However this results in the depender becoming vulnerable to the intentions of the dependee. This
    vulnerability is implied because the dependee may fail to accomplish the specified element.
    The model distinguishes three degrees of strength for the dependency according to the level of vulnerability. These
    types of dependencies apply independently on each side of a dependency. They are described in the following:

     * Open dependency (uncommitted): Not obtaining the dependum would affect the depender to some extent but not
       seriously. This dependency strength is represented by including an "O" on the appropriate side of the link.
     * Committed dependency: Not obtaining the dependum would cause some action for achieving a goal to fail in the
       depender.
     * Critical dependency: Not obtaining the dependum would cause all actions to fail that the depender has planned
       to achieve a goal. This dependency strength is represented by including an "X" on the appropriate side of the link.

    .. figure:: ../../python/_istar/dependencystrengths.jpg
        :scale: 50%
        :align: left



3.1.5 Strategic Dependency Example Model: Buyer Drive E-Commerce from Yu01

    .. figure:: ../../python/_istar/sd.jpg
        :scale: 50%
        :align: center



3.2 Strategic Rationale (SR) Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The SR model is a graph, with several types of nodes and links that work together to provide a representational
    structure for expressing the rationales behind dependencies. The actors with the SD model are "opened up" to show
    their specific intentions. There are four types of nodes, based on the same distinctions made for dependum types
    in the SD model: goal, task, resource, and softgoal. There are three main classes of links internal to the i*
    actor: means-ends links, task decomposition links and contribution links.

3.2.1 Boundary / Actor Boundary

    Actor boundaries indicate intentional boundaries of a particular actor. All of the elements within a boundary for
    an actor are explicitly desired by that actor. In order to achieve these elements, often an actor must depend on
    the intentions of other actors, represented by dependency links across actor boundaries. In turn, an actor is
    depended upon to satisfy certain elements, represented by a dependency link in the opposite direction.

    .. figure:: ../../python/_istar/actorboundary.gif
        :scale: 50%
        :align: left


3.2.2 Elements/Nodes

    The meanings of these elements are the generally the same as found in dependencies, with the exception that the
    satisfaction of elements may be accomplished internally.



3.2.2.1 Goals (Hard Goals)

    Represents and intentional desire of an actor, the specifics of how the goal is to be satisfied is not described by
    the goal. This can be described through task decomposition.

    .. figure:: ../../python/_istar/goal.gif
        :scale: 50%
        :align: left



3.2.2.2 Softgoals

    Softgoals are similar to (hard) goals except that the criteria for the goal's satisfaction are not clear-cut, it is
    judged to be sufficiently satisfied from the point of view of the actor. The means to satisfy such goals are
    described via contribution links from other elements. The notion of softgoal satisfaction is described by the
    term satisficed meaning sufficiently satisfied. The converse is still described as denied.

    .. figure:: ../../python/_istar/softgoal.gif
        :scale: 50%
        :align: left



3.2.2.3 Tasks

    The actor wants to accomplish some specific task, performed in a particular way. A description of the specifics of
    the task may be described by decomposing the task into further sub-elements.

    .. figure:: ../../python/_istar/task.gif
        :scale: 50%
        :align: left



3.2.2.4 Resources

    The actor desires the provision of some entity, physical or informational. This type of elements assumes there are
    no open issues or questions concerning how the entity will be achieved.

    .. figure:: ../../python/_istar/resource.gif
        :scale: 50%
        :align: left



3.2.2.5 Beliefs

    A belief is a condition about the world that the actor holds to be true. The actual degree of truth (As indicated
    by evaluation labels) is influence by contributions from other beliefs. A belief is distinct from a goal in that
    the actor has no explicit desire to make the specified condition become true. Beliefs can effect other elements
    in the model via contribution links. Such links can effect other links, saying that this belief effects the effect
    of an element on another, or can have a direct effect on softgoals.

    .. figure:: ../../python/_istar/belief.gif
        :scale: 50%
        :align: left

    .. figure:: ../../python/_istar/belief2.gif
        :scale: 50%
        :align: left



3.2.3 Means-Ends Links

    These links indicate a relationship between an end, and a means for attaining it. The "means" is expressed in the
    form of a task, since the notion of task embodies how to do something, with the "end" is expressed as a goal. In
    the graphical notation, the arrowhead points from the means to the end.

    .. figure:: ../../python/_istar/meansends.gif
        :scale: 50%
        :align: left



3.2.4 Decomposition Links
    A task element is linked to its component nodes by decomposition links. A task can be decomposed into four types
    of elements: a subgoal, a subtask, a resource, and/or a softgoal - corresponding to the four types of elements.
    The task can be decomposed into one to many of these elements. These elements can also be part of dependency links
    in Strategic Dependency model(s) when the reasoning goes beyond an actor's boundary.

    Task-Goal Decomposition: Subgoal. In this kind of decomposition it is not specified how the goal is to be achieved,
    allowing alternatives to be considered.
    Task-Task Decomposition: subtask. When a task is specified as a subcomponent of a (higher) task, this restricts the
    higher task to that particular course of action.
    Task-Resource Decomposition: resourceFor: The entity represented by the resource is not considered problematic by
    the actor. The main concern is whether it is available (and from whom, if it is an external dependency).
    Task SoftGoal Decomposition: softgoalFor: When a softgoal is a component in a task decomposition, it serves as a
    quality goal for that task, and thus guides (or restricts) the selection among alternatives in further
    decomposition of that and other tasks.

    .. figure:: ../../python/_istar/taskdecomposition.gif
        :scale: 50%
        :align: left



3.2.5 Contribution Links

3.2.5.1 Make

    A positive contribution strong enough to satisfice a softgoal.

    .. figure:: ../../python/_istar/make.jpg
        :scale: 50%
        :align: left



3.2.5.2 Some+

    Either a make or a help contribution, a positive contribution whose strength is unknown.

    .. figure:: ../../python/_istar/someplus.jpg
        :scale: 50%
        :align: left



3.2.5.3 Help

    A partial positive contribution, not sufficient by itself to satisfice the softgoal.

    .. figure:: ../../python/_istar/help.jpg
        :scale: 50%
        :align: left



3.2.5.4 Unknown

    A contribution to a softgoal whose polarity is unknown.

    .. figure:: ../../python/_istar/unknown.jpg
        :scale: 50%
        :align: left



3.2.5.5 Break

    A negative contribution sufficient enough to deny a softgoal.

    .. figure:: ../../python/_istar/break.jpg
        :scale: 50%
        :align: left



3.2.5.6 Some-

    Either a break or a hurt contribution, a negative contribution whose strength is unknown.

    .. figure:: ../../python/_istar/someminus.jpg
        :scale: 50%
        :align: left



3.2.5.7 Hurt

    A partial negative contribution, not sufficient by itself to deny the softgoal.

    .. figure:: ../../python/_istar/hurt.jpg
        :scale: 50%
        :align: left



3.2.5.8 Or

    The parent is satisficed if any of the offspring are satisficed.

    .. figure:: ../../python/_istar/or.jpg
        :scale: 50%
        :align: left



3.2.5.9 And

    The parent is satisficed if all of the offspring are satisficed.

    .. figure:: ../../python/_istar/and.jpg
        :scale: 50%
        :align: left




3.2.6 Strategic Rationale Example Model: Buyer Drive E-Commerce from Yu01

    .. figure:: ../../python/_istar/sr.jpg
        :scale: 50%
        :align: left


4. i* in DOREF
--------------

4.1 SD-Model
^^^^^^^^^^^^

    In this section an example of the modeling processes of a SD-Model are given (Meeting-Scheduler Example).

    First specify a Chapter in the RE Tree for a Goal Model. ::

        Chapter("Goal Model")

    Next add a Model to the Document. ::

        GoalModel("SD-Model of Meeting Scheduler",
              "This model shows a Strategic Dependency (SD) model of the meeting scheduler.",
              {'size': 'fit'})

    Inside a SD-Model are Actors. ::

        cd("/*/SD-Model of Meeting Scheduler")
        Actor("Meeting Initiator",
              "The Meeting Initiator organizes a meeting (see Domain Theory). The Strategic "
              "Resource (SR) model shows the resources of the Meeting Initiator.", {'size': 'fit'})
        Actor("Meeting Participant", "The participant shall attend a meeting.", {'size': 'fit'})
        Actor("Meeting Scheduler",
              "The system which shall support the Meeting Initiator to organize meetings.",
              {'size': 'fit'})

    For every Actor a SR-Model will be generated.

    After adding the actors, the relationships between them must be modeled.
    Add all dependuums between the actors to the Goal Model. ::

        cd('/*/SD-Model of Meeting Scheduler')
        Goal("Attends Meeting D")
        Goal("Meeting Be Scheduled D")
        Task("Enter Date Range D")
        Task("Enter Avail Dates D")
        Resource("Proposed Date D")
        Resource("Agreement D")

    Then add the DependencyLinks. ::

        cd('/*/SD-Model of Meeting Scheduler')
        DependencyLink(node("/*/SD-Model/*/Meeting Scheduler"), node("/*/Meeting Initiator"),
                 node("/*/Meeting Be Scheduled D"))
        DependencyLink(node("/*/SD-Model/*/Meeting Scheduler"), node("/*/Meeting Participant"),
                    node("/*/Proposed Date D"))

        DependencyLink(node("/*/Meeting Initiator"), node("/*/SD-Model/*/Meeting Scheduler"),
                    node("/*/Enter Date Range D"))

        DependencyLink(node("/*/Meeting Participant"),
                       node("/*/SD-Model/*/Meeting Scheduler"),
                       node("/*/Enter Avail Dates D"))
        DependencyLink(node("/*/Meeting Participant"),
                       node("/*/SD-Model/*/Meeting Scheduler"),
                       node("/*/Agreement D"))
        DependencyLink(node("/*/Meeting Participant"),
                       node("/*/Meeting Initiator"),
                       node("/*/Attends Meeting D"))

    .. figure:: ../../python/_istar/SDMS.png
        :width: 100%
        :align: left

    Resulting model

4.2 SR-Model
^^^^^^^^^^^^

    In this Section the Meeting Scheduler Example will be enlarged for the Meeting Participant.
    Goto the the Meeting Participant. ::

        cd("/*/Meeting Participant")

    Now we add all Elements (Goals, Tasks, Softgoals, Resources) and Links (Decomposition-, MeanEnd-,ContributionLink)
    to the SR-Model. ::

        Task("Participate In Meeting")

        Task("Attend Meeting")
        DecompositionLink(node("/*/Attend Meeting"),
                          node("/*/Participate In Meeting"))

        SoftGoal("Convenient (Meeting, Date)")
        DecompositionLink(node("/*/Convenient (Meeting, Date)"),
                          node("/*/Participate In Meeting"))

        Task("Arrange Meeting")
        DecompositionLink(node("/*/Arrange Meeting"),
                          node("/*/Participate In Meeting"))

        SoftGoal("Low Effort")
        DecompositionLink(node("/*/Meeting Participant/*/Low Effort"),
                          node("/*/Arrange Meeting"))

        Goal("Agreeable (Meeting, Date)")
        DecompositionLink(node("/*/Agreeable (Meeting, Date"),
                          node("/*/Arrange Meeting"))

        Task("Find Agreeable Date By Talking To Initiator")
        MeanEndLink(node("/*/Find Agreeable Date By Talking To Initiator"),
                    node("/*/Agreeable (Meeting, Date)"))

        Task("Find Agreeable Date Using Scheduler")
        MeanEndLink(node("/*/Find Agreeable Date Using Scheduler"),
                    node("/*/Agreeable (Meeting, Date)"))

        Task("Agree To Date")
        DecompositionLink(node("/*/Agree To Date"),
                          node("/*/Find Agreeable Date Using Scheduler"))


        SoftGoal("Quality (Proposed Date)")
        ContributionLink(node("/*/Quality (Proposed Date)"),
                         node("/*/Convenient (Meeting, Date)"),"HELP")

        SoftGoal("Richer Medium")
        ContributionLink(node("/*/Richer Medium"),
                         node("/*/Quality (Proposed Date)"),"HELP")

        ContributionLink(node("/*/Find Agreeable Date Using Scheduler"),
                        node("/*/Richer Medium"),"HURT")
        ContributionLink(node("/*/Find Agreeable Date By Talking To Initiator"),
                         node("/*/Richer Medium"),"HELP")

        SoftGoal("User Friendly")
        ContributionLink(node("/*/User Friendly"),
                         node("/*/Meeting Participant/*/Low Effort"),"HELP")

        ContributionLink(node("/*/Find Agreeable Date Using Scheduler"),
                         node("/*/User Friendly"),"HURT")
        ContributionLink(node("/*/Find Agreeable Date By Talking To Initiator"),
                         node("/*/User Friendly"),"HELP")

    At last the DependencyLinks must be refined. ::

        cd("/*/SD-Model of Meeting Schedule")

        refineDependency(node("/*/Meeting Be Scheduled D"),
                         node("/*/SD-Model/*/Meeting Scheduler/*/Schedule Meeting"),
                         node("/*/Let Scheduler Schedule Meeting"))
        refineDependency(node("/*/Proposed Date D"),
                         node("/*/SD-Model/*/Meeting Scheduler/*/Schedule Meeting"),
                         node("/*/Agree To Date"))

        refineDependency(node("/*/Enter Date Range D"),
                         node("/*/Let Scheduler Schedule Meeting"),
                         node("/*/SD-Model/*/Meeting Scheduler/*/Schedule Meeting"))

        refineDependency(node("/*/Enter Avail Dates D"),
                         node("/*/Find Agreeable Date Using Scheduler"),
                         node("/*/Obtain Avail Dates"))
        refineDependency(node("/*/Agreement D"),
                         node("/*/Agree To Date"),
                         node("/*/Obtain Agreement"))
        refineDependency(node("/*/Attends Meeting D"),
                         node("/*/Attend Meeting"),
                         node("/*/Organize Meeting"))

    .. figure:: ../../python/_istar/SRMP.png
        :width: 100%
        :align: left

    Resulting model

4.3 Analyse of a Model
^^^^^^^^^^^^^^^^^^^^^^

4.3.1 Via source code

    To analyse a Model we define Activities. The default description can be found in over the html documentation.
    First define a general Acticity. ::

        EvaluateGoalModel("Evaluate Goal Model")


    Then add initial Activities. ::

        cd("Evaluate Goal Model")
        FindLeafs("Find Leaves for Analysis", goalModel=node("/*/SD-Model of Meeting Schedule")).do()
        FindRoot("Find Root", goalModel=node("/*/SD-Model of Meeting Schedule")).do()

        SetLabels("Set initial values of labels", "", {
            '/*/Proposed Date D' : 'Satisfied',
            '/*/Schedule Meeting': 'Denied',
            '/*/Merge Avail Dates': 'Satisfied',
            '/*/Attend Meeting': 'Satisfied',
            '/*/Find Agreeable Date By Talking To Initiator': 'Satisfied'}).do()

    After initialization of the leafs the first Propageten can be done. ::

        PropagateLabels("Initially Propagate Labels",
                         goalModel=node("/*/SD-Model of Meeting Schedule")).do()

    If any problems occur a Human Judgment is needed. ::

        MakeJudgements("Make judgement after inspection of goal model", "", {
            '/*/Meeting Participant/*/User Friendly': 'Conflict',
            '/*/Meeting Participant/*/Richer Medium': 'Conflict',
            '/*/Meeting Initiator/*/Low Effort': 'Partially Satisfied',
            '/*/Meeting Initiator/*/Quick': 'Partially Satisfied'}).do()

    After the judgment a last propagation can be done. ::

        PropagateLabels("Propagate Labels after Human Judgement",
                         goalModel=node("/*/SD-Model of Meeting Schedule")).do()



4.3.2 Via Console

    To open the Console goto Tools -> Run Python Console...

    First load the Modules so you can use the functions. ::

        from ref import *
        from ieee830 import *
        from istar import *

    Next load the project file with the model. ::

        import meeting_scheduler

    Open the resulting image of the generating process (Example: Meeting_Participant.png). You can use any imageviewer.

    During the analyse the resultst can be shown with the follwoing command ::

        Show("/*/Meeting Participant")

    In our example the leafs are already initialized, so the first propagation can be done. ::

        PropagateLabel("/*/SD-Model")

    The Output says, that a Human Judgment is needed in some Nodes ::

        Human Judgment in Node: Richer Medium (Path: /*/Meeting Participant/*/Richer Medium ) Label Set:
        Find Agreeable Date By Talking To Initiator : Partially Satisfied
        Find Agreeable Date Using Scheduler : Partially Denied

        Human Judgment in Node: User Friendly (Path: /*/Meeting Participant/*/User Friendly ) Label Set:
        Find Agreeable Date By Talking To Initiator : Partially Satisfied
        Find Agreeable Date Using Scheduler : Partially Denied

    To solve this problems use the command ``MakeJudgment``. The path to the node can be copy & past from the ouput. ::

        MakeJudgement("/*/Meeting Participant/*/Richer Medium", "Conflict")
        MakeJudgement("/*/Meeting Participant/*/User Friendly", "Conflict")

    After a last propagation the resulting model can be seen. ::

        PropagateLabel("/*/SD-Model")
        Show("/*/Meeting Participant")


    .. figure:: ../../python/_istar/SRMPa.png
        :width: 100%
        :align: left

    Resulting model
"""

from ref import *


def Show(pathModel):
    """
    Generates an image of the model.

    Parameters:
        :param pathModel: path to the Model node in the RE Tree.
    """
    tmpNode = node(pathModel)
    if isinstance(tmpNode, GoalModel):
        tmpNode.genImage(show=True)


def SetLabel(pathNode, newLabel):
    """
    Sets the Label of the Node.

    Parameters:
        :param pathNode: Path to the node in the RE Tree.
        :param newLabel: Label for the Node.
    """
    tmpNode = node(pathNode)
    if isinstance(tmpNode, Intention):
        if newLabel in GoalModel.Label:
            tmpNode.properties['InputLabel'] = newLabel
            tmpNode.properties['Label'] = newLabel
        else:
            raise AttributeError("newLabel must be one of the following Labels: " + ','.join(GoalModel.Label.keys()))


def MakeJudgement(pathNode, newLabel):
    """
    Sets a Human Judgement for a Node.

    Parameters:
        :param pathNode: Path to the Node in the RE Tre.
        :param newLabel: Label of the Node.
    """
    tmpNode = node(pathNode)
    if isinstance(tmpNode, SoftGoal):
        tmpNode.properties['Judgment'] = newLabel
        tmpNode.properties['Label'] = newLabel


def PropagateLabel(goalmodel):
    """
    Starts the label propagation of a goal model.

    Parameters:
        :param goalmodel: The goal model to be analyzed
    """
    model = node(goalmodel)
    if isinstance(model, GoalModel):
        model.forwardEvaluation()


def key_for_value(d, value):
    """Return a key in dictionary `d` having a value of `value`.

    Parameters:
        :param d:
        :param value:
    """
    for k, v in d.items():
        if v == value:
            return k


class GoalModel(Model):
    """
    This class describes a SD-Model. (Only Actors and DependencyLinks)

    Variables
        :var caption: caption of the model (shown in the document)
        :var text: optional explanation of the model to be shown in the document
        :var properties: yet no special properties for models (rendering options envisioned)
        :var pNode: parent node
        """
    mnemonic = 'SRM'

    Label = {'None': 0,
             'Satisfied': 6,
             'Partially Satisfied': 5,
             'Conflict': 4,
             'Unknown': 3,
             'Partially Denied': 2,
             'Denied': 1}

    def getLabel(self):
        """


        :return:
        """
        return self.mnemonic

    def __init__(self, caption, text="", properties=None, pNode=None):
        if properties is None:
            properties = {}
        Model.__init__(self, caption, text, properties, pNode)
        self.links = []
        self.intentions = []

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
        for n in self.nodes:
            if isinstance(n, GoalModel):
                n.genTeX(texAry, level, index, number)

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
        tmpname = self.cleanFileName()
        dot = Digraph(comment=tmpname)
        dot.format = 'png'
        # dot.engine = 'circo'
        # dot.charset = 'UTF-8'
        dot.graph_attr.update(rankdir='LR')

        self.genDot(dot)
        for link in self.links:
            link.genDot(dot)
        dot.node_attr.update(fontsize='11.0')
        dot.edge_attr.update(fontsize='11.0')

        if overwrite is False:
            n = 0
            while os.path.isfile(Document.imgPath + tmpname + '_' + str(n) + '.png') is True:
                n += 1
            saveImg = Document.imgPath + tmpname + '_' + str(n)
        else:
            saveImg = Document.imgPath + tmpname
        dot.render(saveImg, view=False)
        self.figure = tmpname + '.png'

    def findLeaf(self):
        """

        :param self:
        """
        for n in self.nodes:
            if isinstance(n, GoalModel):
                n.findLeaf()

    def findRoot(self):
        """

        :param self:
        """
        for n in self.nodes:
            if isinstance(n, GoalModel):
                n.findRoot()

    def forwardEvaluation(self, interactive=True):
        """

        :param self:
        :param interactive:
        """
        for n in self.nodes:
            if isinstance(n, GoalModel):
                n.forwardEvaluation(interactive=interactive)

    def clearLabel(self):
        """

        :param self:
        """
        for i in self.intentions:
            if 'Label' in i.properties:
                del i.properties['Label']
            if 'InputLabel' in i.properties:
                del i.properties['InputLabel']
            if 'humanJudgment' in i.properties:
                del i.properties['humanJudgment']
        for n in self.nodes:
            if isinstance(n, GoalModel):
                n.clearLabel()

    def clearIcon(self):
        """

        :param self:
        """
        for i in self.intentions:
            if 'NodeType' in i.properties:
                if i.properties['NodeType'] != 'depender':
                    del i.properties['NodeType']
        for n in self.nodes:
            if isinstance(n, GoalModel):
                n.clearLabel()

    def genDot(self, dot):
        """ Traverses the tree from the current node and generates a graphviz model.

        :param self:
        :param dot:
            """
        for i in self.intentions:
            i.genDot(dot)
        for n in self.nodes:
            if isinstance(n, Actor):
                n.genActor(dot)


class Actor(GoalModel):
    """
        :param caption: caption of the model (shown in the document)
        :param text: optional explanation of the model to be shown in the document
        :param properties: yet no special properties for models (rendering options envisioned)
        :param pNode: parent node
        """

    def __init__(self, caption, text="", properties=None, pNode=None):
        GoalModel.__init__(self, caption, text, properties, pNode)
        self.dependencyFrom = None
        self.dependenciesTo = []

    def genActor(self, dot):
        """

        :param dot:
        """
        dot.node(str(self.id), self.name, fillcolor='White',
                 style='filled',
                 shape='circle')

    def genImage(self, overwrite=True, show=False):
        """

        :param overwrite:
        :param show:
        """
        tmpname = self.cleanFileName()
        dot = Digraph(comment=tmpname)
        dot.format = 'png'
        # dot.engine = 'circo'
        # dot.charset = 'UTF-8'

        self.genDot(dot)
        for link in self.links:
            link.genDot(dot)
        dot.node_attr.update(fontsize='11.0')
        dot.edge_attr.update(fontsize='11.0')

        if overwrite is False:
            n = 0
            while os.path.isfile(Document.imgPath + tmpname + '_' + str(n) + '.png') is True:
                n += 1
            saveImg = Document.imgPath + tmpname + '_' + str(n)
        else:
            saveImg = Document.imgPath + tmpname
        dot.render(saveImg, view=False)  # TODO view=show only on Windows
        self.figure = tmpname + '.png'

    def findLeaf(self):
        """


        """
        for i in self.intentions:
            if not i.contributionFrom and not i.decompositionFrom and i.dependencyFrom is None:
                i.properties['NodeType'] = 'leaf'

    def findRoot(self):
        """


        """
        for i in self.intentions:
            if not i.contributionTo and not i.decompositionTo and not i.dependenciesTo:
                if 'NodeType' not in i.properties or \
                        'NodeType' in i.properties and i.properties['NodeType'] != 'depender':
                    i.properties['NodeType'] = 'root'

    def forwardEvaluation(self, interactive=True):
        """

        :param interactive:
        """
        self.findLeaf()
        startNodes = []
        for n in self.intentions:
            if 'NodeType' in n.properties and \
                    (n.properties['NodeType'] == 'leaf' or n.properties['NodeType'] == 'depender'):
                startNodes.append(n)
            if 'humanJudgment' in n.properties:
                del n.properties['humanJudgment']
                # if 'Label' in n.properties and n.properties['Label'] == 'Unknown':
                # del n.properties['Label']

        for n in startNodes:
            if 'InputLabel' in n.properties:
                n.properties['Label'] = n.properties['InputLabel']
            if n.properties['NodeType'] == 'depender':
                if 'Label' in n.dependencyFrom.dependuum.properties:
                    n.compute(n.dependencyFrom.dependuum.properties['Label'], n.dependencyFrom.dependuum.name)
                elif 'InputLabel' in n.dependencyFrom.dependuum.properties:
                    n.compute(n.dependencyFrom.dependuum.properties['InputLabel'], n.dependencyFrom.dependuum.name)
                elif 'Label' in n.dependencyFrom.begin.properties:
                    n.compute(n.dependencyFrom.begin.properties['Label'], n.dependencyFrom.begin.name)
                elif 'InputLabel' in n.dependencyFrom.begin.properties:
                    n.compute(n.dependencyFrom.begin.properties['InputLabel'], n.dependencyFrom.begin.name)
            else:
                n.compute()

        if interactive:
            for i in self.intentions:
                if 'humanJudgment' in i.properties:
                    print("\n Human Judgment in Node: " + i.name +
                          " (Path: /*/" + i.parent.name + '/*/' + i.name + " ) Label Set:")
                    for tmpNode, label in i.incomingLabels.items():
                        print(tmpNode, ":", label)
            self.genImage(show=True)


class Intention(ModelElement):
    """

        :param name:
        :param properties:
        :param pNode:
        """

    def __init__(self, name, properties=None, pNode=None):
        if properties is None:
            properties = {}
        ModelElement.__init__(self, name, properties, pNode)
        self.parent.intentions.append(self)
        self.contributionTo = []
        self.contributionFrom = []
        self.decompositionTo = []
        self.decompositionFrom = []
        self.dependencyFrom = None
        self.dependenciesTo = []
        self.incomingLabels = {}

    def getColor(self):
        """


        :return:
        """
        fillcolor = 'white'
        if 'NodeType' in self.properties:
            if self.properties['NodeType'] == 'root':
                fillcolor = 'lightblue'
            elif self.properties['NodeType'] == 'leaf':
                fillcolor = 'green'
            elif self.properties['NodeType'] == 'depender':
                fillcolor = 'yellow'
        return fillcolor

    def compute(self, newLabel='None', sourceName=None, ):

        """

        :param newLabel:
        :param sourceName:
        """
        for n in self.contributionTo:
            if 'Label' in self.properties:
                n.end.compute(n.computeLabel(), self.name)
            else:
                n.end.compute('None', self.name)
        for n in self.decompositionTo:
            if 'Label' in self.properties:
                n.end.compute(self.properties['Label'], self.name)
            else:
                n.end.compute('None')
        for n in self.dependenciesTo:
            if 'Label' in self.properties:
                n.dependuum.properties['Label'] = self.properties['Label']

    def getLabelImg(self):
        """


        :return:
        """
        image = ""

        if 'Label' in self.properties:
            if self.properties['Label'] == 'Satisfied':
                image = '_istar/sL.png'
            elif self.properties['Label'] == 'Partially Satisfied':
                image = '_istar/psL.png'
            elif self.properties['Label'] == 'Denied':
                image = '_istar/dL.png'
            elif self.properties['Label'] == 'Partially Denied':
                image = '_istar/pdL.png'
            elif self.properties['Label'] == 'Unknown':
                image = '_istar/uL.png'
            elif self.properties['Label'] == 'Conflict':
                image = '_istar/cL.png'
        return image


class Goal(Intention):
    mnemonic = "GOAL"

    def getLabel(self):
        """


        :return:
        """
        return self.mnemonic

    def genDot(self, dot):
        """

        :param dot:
        """
        if 'Label' in self.properties and self.properties["Label"] != 'None':
            dot.node(str(self.id),
                     '<<TABLE border="0" cellborder="0"><TR><TD>' + self.name +
                     ' </TD><td width="20" height="20" fixedsize="true"><IMG SRC="' + self.getLabelImg() +
                     '" scale="true"/></td></TR></TABLE>>',
                     fillcolor=self.getColor(), style='filled',
                     shape='ellipse')
        else:
            dot.node(str(self.id), self.name, fillcolor=self.getColor(),
                     style='filled',
                     shape='ellipse')

    def compute(self, newLabel='None', sourceName=None):
        """

        :param newLabel:
        :param sourceName:
        """
        if newLabel != 'None':
            self.incomingLabels[sourceName] = newLabel

            if 'Label' in self.properties:
                if self.properties['Label'] not in self.incomingLabels.values():
                    self.properties['Label'] = newLabel
                for l in self.incomingLabels.values():
                    if GoalModel.Label[self.properties['Label']] < GoalModel.Label[l]:
                        self.properties['Label'] = l
            else:
                self.properties['Label'] = newLabel
        if 'Label' in self.properties:
            Intention.compute(self, newLabel=self.properties['Label'])
        else:
            Intention.compute(self)


class SoftGoal(Intention):
    mnemonic = "SOFT"

    def getLabel(self):
        """


        :return:
        """
        return self.mnemonic

    def genDot(self, dot):
        """

        :param dot:
        """
        imageName = '_istar/sg.png'
        if 'NodeType' in self.properties:
            if self.properties['NodeType'] == 'root':
                imageName = '_istar/sgr.png'
            elif self.properties['NodeType'] == 'leaf':
                imageName = '_istar/sgl.png'
            elif self.properties['NodeType'] == 'depender':
                imageName = '_istar/sgd.png'

        if 'Label' in self.properties and self.properties['Label'] != 'None':
            dot.node(str(self.id),
                     '<<TABLE border="0" cellborder="0"><TR><TD>' + self.name +
                     ' </TD><td width="20" height="20" fixedsize="true"><IMG SRC="' + self.getLabelImg() +
                     '" scale="true"/></td></TR></TABLE>>',
                     shape='box', peripheries='0', image=imageName, imagescale='width')
        else:
            dot.node(str(self.id), self.name, shape='box', peripheries='0',
                     image=imageName,
                     imagescale='width')

    def compute(self, newLabel='None', sourceName=None):
        """

        :param newLabel:
        :param sourceName:
        """

        if not 'Judgment' in self.properties:
            if newLabel != 'None':
                self.incomingLabels[sourceName] = newLabel
                labels = list(self.incomingLabels.values())
                if len(labels) == 1:
                    resultLabel = labels[0]
                elif 'Unknown' not in labels and 'Conflict' not in labels:
                    if 'Satisfied' in labels and 'Denied' not in labels and 'Partially Denied' not in labels:
                        resultLabel = 'Satisfied'
                    elif 'Denied' in labels and 'Satisfied' not in labels and 'Partially Satisfied' not in labels:
                        resultLabel = 'Denied'
                    else:
                        self.properties['humanJudgment'] = 'need'
                        resultLabel = 'Unknown'
                else:
                    self.properties['humanJudgment'] = 'need'
                    resultLabel = 'Unknown'
                if 'InputLabel' in self.properties and self.properties['InputLabel'] != resultLabel:
                    self.properties['humanJudgment'] = 'need'
                    self.properties['Label'] = 'Unknown'
                else:
                    self.properties['Label'] = resultLabel

        else:
            self.properties['Label'] = self.properties['Judgment']

        if 'Label' in self.properties:
            Intention.compute(self, newLabel=self.properties)
        else:
            Intention.compute(self)


class Task(Intention):
    mnemonic = "TASK"

    def getLabel(self):
        """


        :return:
        """
        return self.mnemonic

    def genDot(self, dot):
        """

        :param dot:
        """
        if 'Label' in self.properties and self.properties['Label'] != 'None':
            dot.node(str(self.id),
                     '<<TABLE border="0" cellborder="0"><TR><TD>' + self.name +
                     ' </TD><td width="20" height="20" fixedsize="true"><IMG SRC="' + self.getLabelImg() +
                     '" scale="true"/></td></TR></TABLE>>',
                     fillcolor=self.getColor(), style='filled',
                     shape='hexagon')
        else:
            dot.node(str(self.id), self.name, fillcolor=self.getColor(),
                     style='filled',
                     shape='hexagon')

    def compute(self, newLabel='None', sourceName=None):
        """

        :param newLabel:
        :param sourceName:
        """
        if newLabel != 'None':
            if 'Label' in self.properties:
                self.incomingLabels[sourceName] = newLabel
                if self.properties['Label'] not in self.incomingLabels.values():
                    self.properties['Label'] = newLabel
                for l in self.incomingLabels.values():
                    if GoalModel.Label[self.properties['Label']] > GoalModel.Label[l]:
                        self.properties['Label'] = l
            else:
                self.properties['Label'] = newLabel
        if 'Label' in self.properties:
            Intention.compute(self, newLabel=self.properties['Label'])
        else:
            Intention.compute(self)


class Resource(Intention):
    mnemonic = "RESOURCE"

    def getLabel(self):
        """


        :return:
        """
        return self.mnemonic

    def genDot(self, dot):
        """

        :param dot:
        """
        if 'Label' in self.properties and self.properties['Label'] != 'None':
            dot.node(str(self.id),
                     '<<TABLE border="0" cellborder="0"><TR><TD>' + self.name +
                     ' </TD><td width="20" height="20" fixedsize="true"><IMG SRC="' + self.getLabelImg() +
                     '" scale="true"/></td></TR></TABLE>>',
                     fillcolor=self.getColor(), style='filled',
                     shape='box')
        else:
            dot.node(str(self.id), self.name, fillcolor=self.getColor(),
                     style='filled',
                     shape='box')

    def compute(self, newLabel='None', sourceName=None):
        """

        :param newLabel:
        :param sourceName:
        """
        if 'Label' in self.properties:
            Intention.compute(self, newLabel=self.properties['Label'])
        else:
            Intention.compute(self)


class MeanEndLink(Link):
    def __init__(self, begin, end):
        if type(begin).__name__ == 'Task' and type(end).__name__ == 'Goal':
            Link.__init__(self, begin, end)
            begin.decompositionTo.append(self)
            begin.parent.links.append(self)
            end.decompositionFrom.append(self)
        else:
            raise TypeError("'begin' must be a 'Task', 'end' must be a 'Goal' !")

    def genDot(self, dot):
        """

        :param dot:
        """
        dot.edge(str(self.end.id), str(self.begin.id), dir='back')

    def genTeX(self, texAry, level, index, number):
        pass


class ContributionLink(Link):
    def __init__(self, begin, end, TYPE='UNKNOWN'):
        types = ['MAKE', 'HELP', 'SOME+', 'UNKNOWN', 'SOME-', 'HURT', 'BREAK']
        if TYPE in types:
            if (type(begin).__name__ == 'Task' or type(begin).__name__ == 'Goal' or type(
                    begin).__name__ == 'SoftGoal') or type(begin).__name__ == 'Resource' and type(
                    end).__name__ == 'SoftGoal':
                Link.__init__(self, begin, end)
                self.type = TYPE
                begin.contributionTo.append(self)
                begin.parent.links.append(self)
                end.contributionFrom.append(self)
            else:
                raise TypeError("'begin' must be a Task, Goal or Softgoal, 'end' must be a 'SoftGoal' !")
        else:
            raise TypeError("'Wrong type useabled types: " + ', '.join(types))

    def genDot(self, dot):
        """

        :param dot:
        """
        dot.edge(str(self.begin.id), str(self.end.id), arrowhead='vee',
                 label=self.type)

    def genTeX(self, texAry, level, index, number):
        pass

    def computeLabel(self):
        """


        :return:
        """
        if 'Label' in self.begin.properties:
            if self.begin.properties['Label'] == 'Satisfied':
                if self.type == 'MAKE':
                    label = 'Satisfied'
                elif self.type == 'BREAK':
                    label = 'Denied'
                elif self.type == 'SOME+' or self.type == 'HELP':
                    label = 'Partially Satisfied'
                elif self.type == 'SOME-' or self.type == 'HURT':
                    label = 'Partially Denied'
                else:
                    label = 'Unknown'
            elif self.begin.properties['Label'] == 'Partially Satisfied':
                if self.type == 'MAKE' or self.type == 'HELP' or self.type == 'SOME+':
                    label = 'Partially Satisfied'
                elif self.type == 'BREAK' or self.type == 'HURT' or self.type == 'SOME-':
                    label = 'Partially Denied'
                else:
                    label = 'Unknown'
            elif self.begin.properties['Label'] == 'Conflict':
                if self.type == 'UNKNOWN':
                    label = 'Unknown'
                else:
                    label = 'Conflict'
            elif self.begin.properties['Label'] == 'Unknown':
                label = 'Unknown'
            elif self.begin.properties['Label'] == 'Partially Denied':
                if self.type == 'MAKE' or self.type == 'HELP' or self.type == 'SOME+':
                    label = 'Partially Denied'
                elif self.type == 'BREAK' or self.type == 'HURT' or self.type == 'SOME-':
                    label = 'Partially Satisfied'
                else:
                    label = 'Unknown'
            elif self.begin.properties['Label'] == 'Denied':
                if self.type == 'MAKE':
                    label = 'Denied'
                elif self.type == 'BREAK':
                    label = 'Partially Satisfied'
                elif self.type == 'SOME+' or self.type == 'HELP':
                    label = 'Partially Denied'
                elif self.type == 'SOME-' or self.type == 'HURT':
                    label = 'Partially Satisfied'
                else:
                    label = 'Unknown'
            else:
                label = 'None'
        else:
            label = 'None'
        return label


class DecompositionLink(Link):
    def __init__(self, begin, end):
        if type(end).__name__ == 'Task':
            Link.__init__(self, begin, end)

            begin.decompositionTo.append(self)
            begin.parent.links.append(self)
            end.decompositionFrom.append(self)
        else:
            raise TypeError("'end' must be a Task!")

    def genDot(self, dot):
        """

        :param dot:
        """
        dot.edge(str(self.begin.id), str(self.end.id), arrowhead='tee')

    def genTeX(self, texAry, level, index, number):
        pass


def refineDependency(dependuum, dependee=None, depender=None):
    """

    :param dependuum:
    :param dependee:
    :param depender:
    :raise AttributeError:
    """
    result = False
    if dependee is not None:
        if isinstance(dependee, Actor):
            for dlink in dependee.parent.links:
                if isinstance(dlink, DependencyLink) and dlink.dependuum == dependuum:
                    result = True
                    if depender is not None and not isinstance(depender, Actor):
                        depender.dependencyFrom = dlink
                        dlink.end = depender
                        depender.properties['NodeType'] = 'depender'
                    else:
                        raise AttributeError("Begin or end must be an element of an Actor")

        else:
            for dlink in dependee.parent.parent.links:
                if isinstance(dlink, DependencyLink) and dlink.dependuum == dependuum:
                    result = True
                    if dependee.dependenciesTo is not None:
                        dependee.dependenciesTo.append(dlink)
                    else:
                        dependee.dependenciesTo = [dlink]
                    dlink.begin = dependee
                    if depender is not None and not isinstance(depender, Actor):
                        depender.dependencyFrom = dlink
                        dlink.end = depender
                        depender.properties['NodeType'] = 'depender'
                    else:
                        raise AttributeError("Begin or end must be an element of an Actor")

        if not result:
            raise AttributeError("Dependency not found")
    elif depender is not None:
        if not isinstance(depender, Actor):
            for dlink in dependee.parent.parent.links:
                result = True
                if isinstance(dlink, DependencyLink) and dlink.dependuum == dependuum:
                    depender.dependencyFrom = dlink
                    dlink.end = depender
                    depender.properties['NodeType'] = 'depender'
                else:
                    raise AttributeError("Begin or end must be an element of an Actor")
        else:
            raise AttributeError("Begin or end must be an element of an Actor")
        if not result:
            raise AttributeError("Dependency not found")
    else:
        raise AttributeError("Begin or end must be set")


class DependencyLink(Link):
    def __init__(self, dependee, depender, dependuum):
        if depender.dependencyFrom is None or isinstance(depender, Actor):
            Link.__init__(self, dependee, depender)
            if isinstance(dependee, Actor):
                dependee.parent.links.append(self)
            else:
                dependee.parent.parent.links.append(self)
                dependee.dependenciesTo.append(self)
            if not isinstance(depender, Actor):
                depender.dependencyFrom = self
                depender.properties['NodeType'] = 'depender'
            self.dependuum = dependuum
        else:
            raise AttributeError("Only One Dependency From a Node!")

    def genDot(self, dot):
        """

        :param dot:
        """
        if isinstance(self.begin, Actor):
            dot.edge(str(self.begin.id), str(self.dependuum.id), arrowtail='odot', dir='back')

        else:
            dot.edge(str(self.begin.parent.id), str(self.dependuum.id), arrowtail='odot', dir='back')
        if isinstance(self.end, Actor):
            dot.edge(str(self.dependuum.id), str(self.end.id), arrowtail='odot', dir='back')
        else:
            dot.edge(str(self.dependuum.id), str(self.end.parent.id), arrowtail='odot', dir='back')

    def genTeX(self, texAry, level, index, number):
        pass


class DevelopGoalModel(Activity):
    def __init__(self, name, guideline=None, pNode=None):
        if guideline is None:
            guideline = '''
**Develop Goal Model:**

* Develop SD-Model
* Develop SR-Model
            '''
        Activity.__init__(self, name, guideline, pNode)

    def getType(self):
        return Activity.__name__


class DevelopSDModel(Activity):
    def __init__(self, name, guideline=None, pNode=None):
        if guideline is None:
            guideline = '''
**Description:**


Start the modeling with the SD model to capture the stakeholders and their associated strategic Dependency dependencies
and interactions

Discussion:
Start with this level of complexity to discover if other stakeholders have been neglected, understand the domain under
analysis, and uncover any issues related to the analysis and design alternatives. SD models are relatively less complex
than SR models. Therefore, this guideline could be optional and useful for students and beginners. Advanced users,
however, might start with an SR model first then collapse the actors to form an SD model. Not all i* notation tools,
however, can facilitate automatic collapsing for the Actors.

    * find and model Actors
    * find and model Dependencies between Actors
            '''
        Activity.__init__(self, name, guideline, pNode)


class DevelopActor(Activity):
    def __init__(self, name, guideline=None, pNode=None):
        if guideline is None:
            guideline = '''
Active entities that carries out actions to achieve goals by exercising its know-how. We use the term actor to refer
generically to any unit to which intentional dependencies can be ascribed.
'''
        Activity.__init__(self, name, guideline, pNode)

    def getType(self):
        return Activity.__name__


class DevelopDependency(Activity):
    def __init__(self, name, guideline=None, pNode=None):
        if guideline is None:
            guideline = '''Dependee
Actor who is depended upon on a dependency relationship.

Depender
The depending actor on a dependency relationship.

Dependum
Element around which a dependency relationship centers.

We distinguish among four types of dependencies, based on the type of the dependum: Resource dependency,
Task dependency, Goal dependency, Softgoal dependency.
'''
        Activity.__init__(self, name, guideline, pNode)

    def getType(self):
        return Activity.__name__


class DevelopSRModel(Activity):
    def __init__(self, name, guideline=None, pNode=None):
        if guideline is None:
            guideline = '''
Employ SR models to expand on the SD models and add the intentionality and rational dimension to the analysis.

Discussion: In case you start with and SD model to explore the various Actors in the domain under analysis, open up the
Actors and systematically add new dimensions about the internal intentionality of the Actors to develop SR models that
can be successfully used to uncover the rational behind the satisfaction or denial of the internal elements and external
dependencies.

Modeling SR - Model:
    1. For every Actor do:
        1. Model all high level Goals
        2. Model Tasks to resolve the Goals ( one or more Tasks per Goal + mean-end-Links)
        3. Repeat Step 2 until every Goal is resolved by a Task
        4. Model all Tasks
        5. Task decomposition if necessary
        6. Goto Step 2 if a Gaol is not resolved by a Task
        7. Model Softgoals and contributions by the other elements
    2. Add Dependencies from or to other Actors

Identification of incomplete models:
    - Unconnected elements
    - Goals or Softgoal are leafs
'''
        Activity.__init__(self, name, guideline, pNode)

    def getType(self):
        return Activity.__name__


class EvaluateGoalModel(Activity):
    def __init__(self, name, guideline=None, pNode=None):
        if guideline is None:
            guideline = '''
**Goal Model Evaluation:**

1. Develop analysis questions
2. Set EvaluationLabels for an analysis question
3. Propagate Labels
4. Interpret the resulting model
5. Repeat Step 2-4 for every question and modify model if necessary
'''
        Activity.__init__(self, name, guideline, pNode)

    def getType(self):
        return Activity.__name__


class PropagateLabels(Activity):
    def __init__(self, name, guideline=None, goalModel=None, pNode=None):
        self.goalModel = goalModel
        if guideline is None:
            guideline = '''
**Label Propagation Rules:**


Dependency Links related rules:
    1. A Dependum acquires the value of the Dependee.
    2. The Dependers take on the value of the Dependum.

Decomposition Links related rules:
    3. The Decomposition Link relationship is treated as an “and” in the evaluation process and therefore all of the
    decomposed elements must be satisfied in order for the upper level task to be satisficed. With the “and” logic, the
    upper level task acquires the minimum value given or marked to child or directly contributing elements. To determine
    the minimum value, we use the following ordering over evaluation elements:

        * Satisfied
        * Partially Satisfied
        * Conflict
        * Unknown
        * Partially Denied
        * Denied

    4. If a node is involved in decomposition as well as a dependency, the values produced by these two relationships
    are resolved using “and” logic and therefore the node acquires the minimum or lowest value provide by the two
    relations.

Means-Ends related rules:
    5. The means-ends relationship is evaluated using “or” logic between the means. With the “or” logic, the Ends take
    on the maximum value given or marked to the Means, using the same ordering as above.

Contribution Links related rules:

    6. The parent Softgoal that has multiple “And Contribution Links” takes on the minimum label of the contributing
    nodes or elements
    7. The parent Softgoal that has multiple “Or Contribution Links” takes on the maximum label of the contributing
    nodes or elements
    8. Propagation rules through other contribution links are derived from the semantic meanings of the contribution
    links. The resulting propagation rules are summarized in Table 1. For example, a Help link represents a partial
    positive contribution; therefore, as described in Table 1, if a satisfied label is propagated through a Help link,
    the resulting label is partially satisfied. Similarly, partially satisfied labels propagate as partially satisfied.
    Unknown and conflict labels propagate as-is. For Denied and partially denied labels, partially denied is propagated.
    In another example, the propagation rules for the Hurt link, which provides a partial negative contribution, are
    similar to the rules for Help, except that the polarity of the propagated labels are reversed. If an element hurts
    a softgoal and this element is satisfied, the softgoal receives a partially denied label. Inversely, if an element
    hurts a softgoal and this element is denied, the softgoal receives a partially satisfied label. The other
    propagation rules follow the same train of logic.

    Table 1: Propagation Rules for Contribution Links

    +--------------------------+------+-------+------+------+-------+-------+---------+
    |    originating Label     |                Contribution Link Type                |
    +--------------------------+------+-------+------+------+-------+-------+---------+
    | Label                    | Make | Break | Help | Hurt | Some+ | Some- | Unknown |
    +==========================+======+=======+======+======+=======+=======+=========+
    | Satisfied (S)            | S    | D     | PS   | PD   | PS    | PD    | U       |
    +--------------------------+------+-------+------+------+-------+-------+---------+
    | Partially Satisfied (PS) | PS   | PD    | PS   | PD   | PS    |PD     | U       |
    +--------------------------+------+-------+------+------+-------+-------+---------+
    | Conflict (C)             | C    | C     | C    | C    | C     | C     | C       |
    +--------------------------+------+-------+------+------+-------+-------+---------+
    | Unknown  (U)             | U    | U     | U    | U    | U     | U     | U       |
    +--------------------------+------+-------+------+------+-------+-------+---------+
    | Partially Denied (PD)    | PD   | PS    | PD   | PS   | PD    | PS    | U       |
    +--------------------------+------+-------+------+------+-------+-------+---------+
    | Denied (D)               | PD   | PS    | PD   | PS   | PD    | PS    | U       |
    +--------------------------+------+-------+------+------+-------+-------+---------+

    9. Often, softgoals receive evidence from multiple sources through multiple contribution links. In these cases,
    we must determine how these sources of evidence are combined into one overall evaluation label. In cases when there
    is only one incoming label, or when combining full and partial evidence of the same polarity, the final label for
    an element can be determined automatically. For example: the final label of an element receiving a bag of labels
    {Partially Satisfied, Satisfied} can be set automatically to Satisfied. Table 2 lists the cases where the overall
    label can be resolved using standard rules, without human judgment.

    Table 2: Cases where Final Labels for Parent Goals can Automatically Determined

    +------------------------------------------------------------+-------------------------+
    | Case                                                       | Resulting Label         |
    +------------------------------------------------------------+-------------------------+
    | If the bag has only one Label                              | the single label        |
    +------------------------------------------------------------+-------------------------+
    | If the parent goal has multiple full Labels of the same    | the full label          |
    | polarity, and no other labels, such as {S, S, S} or {D, D} |                         |
    +------------------------------------------------------------+-------------------------+
    | If all labels in the bag are of the same polarity, and a   | the full label          |
    | full label exists in the set of labels, such as            |                         |
    | {PS, S, PS} or {D, PD}                                     |                         |
    +------------------------------------------------------------+-------------------------+
    | If the previous human judgment produced S or D, and a      | the full label          |
    | new contribution is of the same polarity                   |                         |
    +------------------------------------------------------------+-------------------------+

    10. When the cases in Table 2 do not apply, human judgment, based on domain knowledge, is needed to determine the
    overall label for a softgoal. For instance, when an element receives both positive and negative values or evidence,
    such as {Partially Satisfied, Partially Denied}, or when multiple sources of only positive or only negative partial
    values or evidence is present, such as {Partially Denied, Partially Denied} and {Partially Satisfied,
    Partially Satisfied}, the evaluator can decide if this evidence is strong enough to satisfice or deny an element,
    fully or partially, or whether to the evidence is conflicting, combining the evidence to produce one of the
    evaluation labels.

'''
        Activity.__init__(self, name, guideline, pNode)

    def getType(self):
        return Activity.__name__

    def do(self):
        if self.goalModel is not None:
            self.goalModel.forwardEvaluation(interactive=False)


class FindLeafs(Activity):
    def __init__(self, name, guideline=None, goalModel=None, pNode=None):
        self.goalModel = goalModel
        if guideline is None:
            guideline = '''
Find leaf elements in the goal tree.

**Description:**

Elements in i* SR models which are not decomposed into further elements (mean-end or decomposition), or which do not
receive any contribution from any link, and which are no depender in a dependency link, are called leaf elements.
Leaf elements can be, but are not necessarily operationalizations, as they may not represent high-level executable
tasks.
'''
        Activity.__init__(self, name, guideline=guideline, pNode=pNode)

    def getType(self):
        return Activity.__name__

    def do(self):
        if self.goalModel is not None:
            self.goalModel.findLeaf()


class FindRoot(Activity):
    def __init__(self, name, guideline=None, goalModel=None, pNode=None):
        self.goalModel = goalModel
        if guideline is None:
            guideline = '''
Find root elements in the goal tree.

**Description**

Elements in i* SR models which are decomposed into further elements (mean-end or decomposition), or which receive any
contribution from any link, and which, and have no outgoing decomposition or contribution, are called root elements.

'''
        Activity.__init__(self, name, guideline=guideline, pNode=pNode)

    def getType(self):
        return Activity.__name__

    def do(self):
        if self.goalModel is not None:
            self.goalModel.findRoot()


class SetLabels(Activity):
    def __init__(self, name, guideline=None, labelList=None, pNode=None):
        self.labelList = labelList
        if guideline is None:
            guideline = '''
Set the satisfaction labels of selected nodes in a goal tree. This labels are needed for the label propagation.
'''
        Activity.__init__(self, name, guideline=guideline, pNode=pNode)

    def getType(self):
        return Activity.__name__

    def do(self):
        if self.labelList is not None:
            for l in self.labelList:
                SetLabel(l, self.labelList[l])


class MakeJudgements(Activity):
    def __init__(self, name, guideline=None, labelList=None, pNode=None):
        self.labelList = labelList
        if guideline is None:
            guideline = '''
Make a human judgement for the selected nodes. This judgments are needed for the label propagation.
'''
        Activity.__init__(self, name, guideline=guideline, pNode=pNode)

    def getType(self):
        return Activity.__name__

    def do(self):
        if self.labelList is not None:
            for l in self.labelList:
                MakeJudgement(l, self.labelList[l])