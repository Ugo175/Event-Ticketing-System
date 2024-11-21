"""
Event Ticketing System

Uses a min heap to keep order of users

Removing ticket
"""
import csv
import datetime
import heapq

from random import sample
from string import ascii_lowercase


print("""
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

""")

def main():
    """Code starts execution here"""
    ticket_system = TicketSystem()

    while ticket_system.n_tickets < ticket_system.N_TOTAL:
        print("""
Welcome to our Event Ticketing System. Enter a number to begin.
1. Register for ticket
2. Login to make changes
""")
        user_action = valid_input(">>> ", {'1', '2'})
        # match user_action:
        #     case '1':
        #         User.register(ticket_system)
        #     case '2':
        #         pass
        if user_action == '1':
            User.register(ticket_system)

    # process tickets
    while ticket_system.tickets:
        print(heapq.heappop(ticket_system))


class User:
    """The User class"""
    users = {"admin": ""}  # placeholder to make code generation easy
    id_length = 5

    def __init__(self, name, ticket, priority):
        self.name = name
        self.ticket = ticket
        self.priority = priority
        # If it is regular, give it high position, so that
        # The PriorityQueue will pop it only after all VIPs processed
        if self.ticket == TicketSystem.REGULAR:
            self.priority *= TicketSystem.N_TOTAL*5
        self.active = False
        self.user_id = User.make_id()
        User.users[self.user_id] = self

    @staticmethod
    def register(ticket_system):
        """Class method to add a new user"""
        name = valid_input("Enter your name: ")
        ticket_type = valid_input(
            "Enter ticket type: ", valid=TicketSystem.TICKET_TYPES, upper=True)

        # Check if user can still register
        ticket_type_attr = "n_"+ticket_type.lower()

        other_type = TicketSystem.VIP
        if ticket_type == TicketSystem.VIP:
            other_type = TicketSystem.REGULAR
        
        # Was this for debugging purposes?
        print(getattr(ticket_system, ticket_type_attr))
        
        if getattr(ticket_system, ticket_type_attr) >=\
              getattr(TicketSystem, ticket_type_attr.upper()):
            print(f"""{ticket_type} tickets are sold out now.
Would you like to get a {other_type} ticket instead?
1. Yes
2. No""")
            if valid_input(">>> ", {'1', '2'}) == '1':
                ticket_type = other_type
            else:
                print("Thank you for your time! Good bye!")
                return

        # Instead of the new_priority to be the number of users
        # Make a new class variable to keep track
        # - users might cancel, that will reduce number
        user = User(name, ticket_type, ticket_system.new_priority)
        ticket_system.new_priority += 1
        ticket_system.add_ticket(user)

        # generateid


    @staticmethod
    def make_id():
        """Function for generating user id"""
        user_id = "admin"
        # Create a unique user id. 26Combination5 possible user_ids
        while user_id in User.users:
            user_id = "".join(sample(ascii_lowercase, User.id_length))
        return user_id


def valid_input(prompt: str="Input: ", valid: set=None, upper: bool=False) -> str:
    """Function to persist until valid input gotten"""
    answer = ""
    while answer == "" or (valid and answer not in valid):
        answer = input(prompt)
        if upper:
            answer = answer.upper()
    return answer


class TicketSystem:
    """The ticket management class - will have only one instance"""
    N_VIP = 3
    N_REGULAR = 7
    N_TOTAL = N_VIP+N_REGULAR
    VIP = "VIP"
    REGULAR = "REGULAR"
    REG_ACTIONS = {'1', '2'}
    TICKET_TYPES = {VIP, REGULAR}

    def __init__(self):
        self.n_vip = 0
        self.n_regular = 0
        self.tickets = []  # The starting priority queue
        self.new_priority = 0
        print("Called Ticket")
        # Stop this from having more calls
        TicketSystem.__init__ = lambda *args: None

    def add_ticket(self, user: User):
        """Function to add a ticket/user to the heap"""
        ticket_type_attr = "n_"+user.ticket.lower()
        n_ticket_type = getattr(self, ticket_type_attr)
        setattr(self, ticket_type_attr, n_ticket_type+1)
        heapq.heappush(self.tickets, (user.priority, user.user_id))


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

    NAB = 3

class LoggingSystem:
    """Class to log ticket events"""
    def __init__(self):
        pass

if __name__ == "__main__":
    main()
