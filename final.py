"""Event Ticketing System
Uses a min heap to keep order of users

Removing ticket
"""
import datetime
import heapq

from random import sample
from string import ascii_lowercase


def main():
    """Code starts execution here"""
    ticket_system = TicketSystem()

    while ticket_system.n_tickets < ticket_system.N_TOTAL:
        print("""
Welcome to our Event Ticketing System. Enter a number to begin.
1. Register for ticket
2. Login to make changes
""")
        ticket_action = valid_input(">>> ", {'1', '2'})
        match ticket_action:
            case '2':
                user = User.login()
                if user is None:
                    print("No user_id with that account exists! Consider creating an account")
                    continue
                print(f"""
Hey {user.name}!
What changes do you want to make to your ticket registration?
1. Cancel registration
2. {user.change}
3. View summary
4. Log out
""")
                change_action = valid_input(">>> ", {'1', '2', '3', '4'})
                match change_action:
                    case '1':
                        user.cancel(ticket_system)
                    case '2':
                        user.make_change(ticket_system)
                    case '3':
                        user.summarize()
                    case '4':
                        print("Thank you for your time!")
            case '1':
                User.register(ticket_system)

    # process tickets
    ticket_system.process_tickets()


class TicketSystem:
    """The ticket management class - will have only one instance"""
    N_VIP = 2
    N_REGULAR = 3
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
        # Stop this from having more calls
        TicketSystem.__init__ = lambda *args: None

    def add_ticket(self, user):
        """Function to add a ticket/user to the heap"""
        ticket_type_attr = "n_"+user.ticket.lower()
        n_ticket_type = getattr(self, ticket_type_attr)
        setattr(self, ticket_type_attr, n_ticket_type+1)
        heapq.heappush(self.tickets, (user.priority, user.user_id))

    def remove_ticket(self, ticket_type: str):
        """Function to subtract from ticket count"""
        ticket_type_attr = "n_"+ticket_type.lower()
        n_ticket_type = getattr(self, ticket_type_attr)
        setattr(self, ticket_type_attr, n_ticket_type-1)

    def process_tickets(self):
        """Process from the priority queue from first to last
        Preferring VIPs first
        The first part of elements in the heapq is the priority
        higher number means low priority
        """
        while self.tickets:
            priority, user_id = heapq.heappop(self.tickets)
            print(priority)
            if user_id not in User.users:
                continue
            user = User.users[user_id]
            print(f"Processed {user.name}'s {user.ticket} ticket")


    def is_available(self, ticket_type):
        """Method that tells whether ticket can be changed or not"""
        new_ticket_attr = 'n_'+ticket_type.lower()
        return getattr(self, new_ticket_attr) < \
              getattr(TicketSystem, new_ticket_attr.upper())

    @property
    def n_tickets(self):
        """return the number of tickets
        """
        return self.n_regular+self.n_vip

    @staticmethod
    def switch_ticket(ticket):
        """Returns the other type of ticket, limits DRY"""
        return TicketSystem.REGULAR \
            if ticket == TicketSystem.VIP else TicketSystem.VIP



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
        self.user_id = User.make_id()
        User.users[self.user_id] = self

    def cancel(self, ticket_system):
        """Remove user from list of ticket registered users"""
        del User.users[self.user_id]  # Instead of setting 'active'
        ticket_system.remove_ticket(self.ticket)
        print("Your registration has been canceled successfully")

    def make_change(self, ticket_system):
        """Upgrade/Downgrade ticket"""
        new_ticket = TicketSystem.switch_ticket(self.ticket)
        if ticket_system.is_available(new_ticket):
            self.ticket = new_ticket
            print(f"You have successfully changed your ticket type to {self.ticket}")
        else:
            print("Sorry, but you cannot change your ticket type at this time")

    def summarize(self):
        """Provide summary for this user"""
        print(f"""
Hello {self.name}!
You have registered for a {self.ticket} ticket.
{'How do you feel? Being part of the big folks at the event'\
  if self.ticket == TicketSystem.VIP
 else 'It\'s great that you chose to attend this event!'}

""")

    @property
    def change(self):
        """The type of change that can be made for this user"""
        change_prefix = "Down" if self.ticket == TicketSystem.VIP else "Up"
        new_ticket_type = TicketSystem.switch_ticket(self.ticket)
        return f"{change_prefix}grade to {new_ticket_type}"

    @staticmethod
    def login() -> set | None:
        """Log user in"""
        user_id = valid_input("Enter your user id: ")
        if user_id in User.users:
            return User.users[user_id]
        return None

    @staticmethod
    def register(ticket_system):
        """Class method to add a new user"""
        name = valid_input("Enter your name: ")
        ticket_type = valid_input(
            "Enter ticket type ('VIP'/'REGULAR'): ",
              valid=TicketSystem.TICKET_TYPES, upper=True)
        other_type = TicketSystem.switch_ticket(ticket_type)

        # Check if user can still register
        if not ticket_system.is_available(ticket_type):
            LoggingSystem.log_register_failure(name, ticket_type)
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
        LoggingSystem.log_register_success(name, ticket_type)
        print(f"""
Hey {user.name}! Your {user.ticket} ticket request is being processed.
Your user id is '{user.user_id}'. You can use it to login and change your details.
""")


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


class LoggingSystem:
    """Class to log ticket events"""
    @staticmethod
    def log_register_failure(name, ticket_type):
        """Log registration failure"""
        with open("udd_log.txt", 'a', encoding="utf-8") as file:
            file.write(f"""User {name} tried to register at {datetime.datetime.now()} but {ticket_type} tickets are sold out.\n""")

    @staticmethod
    def log_register_success(name, ticket_type):
        """Log registration success"""
        with open("udd_log.txt", 'a', encoding="utf-8") as file:
            file.write(f"""User {name} registered a {ticket_type} ticket at {datetime.datetime.now()}.\n""")

    @staticmethod
    def log_processed_success(name, ticket_type):
        """Log proccessed user"""
        with open("udd_log.txt", 'a', encoding="utf-8") as file:
            file.write(f"""User {name}'s {ticket_type} ticket was processed at {datetime.datetime.now()}.\n""")
  

if __name__ == "__main__":
    main()
