#!/usr/bin/env python

import rospy
import smach


class StateFoo(smach.state):
    def __init__(self):
        smach.State.__init__(self, outcomes=['goto_bar', 'goto_end'])
        self.counter = 0

    def execute(self, userdate):
        rospy.loginfo('Executing state StateFoo')
        if self.counter < 3:
            self.counter += 1
            return 'goto_bar'
        else:
            return 'goto_end'


class StateBar(smach.state):
    def __init__(self):
        smach.State.__init__(self, outcomes=['goto_foo'])

    def execute(self, userdate):
        rospy.loginfo('Executing state StateFoo')
        return 'goto_foo'


def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(['end_point', 'outcome5'])

    # Open the container
    with sm:
        smach.StateMachine.add('FOO', StateFoo(),
                               transitions={'goto_bar':'StateBar',
                                            'goto_end':'end-point'})
        smach.StateMachine.add('BAR', StateBar(),
                               transitions={'goto_foo'})
    # Excute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()