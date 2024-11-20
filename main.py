"""Event Ticketing System
Uses a min heap to keep order of users

Removing ticket
"""
import csv
import datetime
import heapq

from ast import literal_eval
from collections import deque
from random import sample
from string import ascii_lowercase


N_VIP = 3
N_REGULAR = 7
VIP = 1
REGULAR = 2
REG_ACTIONS = {'1', '2'}
TICKET_TYPES = {"VIP"}

"""
Register
Login

Register
    generate Id, log off
    if ticket for type_ticket:
        sugguest other
            if not want other
            sorry. bye.
    Give ticket
    If NO MORE TICKET:
        process all.

Login.
    Cancel
    downgrade/upgrade if this else downgrde

    if vip full - can't do

    

"""

SYSTEM_MAP = {
    "prompt": "1. Register for ticket\n2. Login",
    '1': {  # register
        "prompt": "1. Continue",
        '1': "User.register",
    },
    '2': {  # Login
        "prompt": "1. No\n2: Go",
        '1': "",
        '2': ""
    }
}


def main():
    """Code starts execution here"""
    ticket_system = TicketSystem(N_VIP, N_REGULAR)

    while ticket_system.n_tickets < N_VIP+N_REGULAR:
        print("Welcome to our Event Ticketing System. Enter a number to begin")
        sys_map = SYSTEM_MAP
        while isinstance(sys_map, dict):  # if not map to an action, like "TicketSystem.process..."
            print(sys_map["prompt"])
            actions = sys_map.keys()
            action = None
            while action != "prompt" and action not in actions:
                action = input(">>> ")
            sys_map = sys_map[action]
        # It is an action for a class
        class_action = sys_map
        literal_eval(class_action)()

    # process tickets
    while heapq:
        pass



class TicketSystem:
    """The ticket management class - will have only one instance"""
    def __init__(self, n_vip, n_regular):
        self.n_vip = n_vip
        self.n_regular = n_regular
        self.tickets = []  # The starting priority queue
        self.rank = 0


    def process_tickets(self):
        """Process from the priority queue from first to last
        Preferring VIPs first
        """
        return 3

    @property
    def n_tickets(self):
        """return the number of tickets
        """
        return len(self.tickets)

class LoggingSystem:
    """Class to log ticket events"""
    def __init__(self):
        pass

class User:
    """The User class"""
    users = deque()
    ids = {"admin"}
    id_length = 5

    def __init__(self, name, ticket, priority):
        self.name = name
        self.ticket = ticket
        self.active = False
        self.priority = priority

    @staticmethod
    def register():
        """Class method to add a new user"""
        name = valid_input("Enter your name: ")
        ticket_type = valid_input("Enter ticket type: ", valid=TICKET_TYPES)

    @staticmethod
    def make_id():
        """Function for generating user id"""
        user_name = "admin"
        # Create a unique user id. 26C5 possible ids
        while user_name in User.ids:
            user_name = "".join(sample(ascii_lowercase, User.id_length))
        return user_name


def valid_input(prompt: str="Input: ", valid=None) -> str:
    """Function to persist until valid input gotten"""
    answer = ""
    while answer == "":
        answer = input(prompt)
    return answer

if __name__ == "__main__":
    main()
