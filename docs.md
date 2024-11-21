Help on module main:

NAME
    main

DESCRIPTION
    Event Ticketing System
    Uses a min heap to keep order of users

    Removing ticket

CLASSES
    builtins.object
        LoggingSystem
        TicketSystem
        User

    class LoggingSystem(builtins.object)
     |  Class to log ticket events
     |
     |  Static methods defined here:
     |
     |  clear_log()
     |      Clear log file
     |
     |  log_canceled_ticket(name)
     |      Log canceled ticket
     |
     |  log_changed_ticket(name, ticket_type, user_id)
     |      Log user changed ticket
     |
     |  log_processed_success(name, ticket_type, user_id)
     |      Log proccessed user
     |
     |  log_register_failure(name, ticket_type)
     |      Log registration failure
     |
     |  log_register_success(name, ticket_type, user_id)
     |      Log registration success
     |
     |  log_requested_summary(name, user_id)
     |      Log proccessed user
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  TICKET_LOG_FILE = 'udd_log.txt'

    class TicketSystem(builtins.object)
     |  The ticket management class - will have only one instance
     |
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  add_ticket(self, user)
     |      Function to add a ticket/user to the heap
     |
     |  change_priority(self, user)
     |      Code to change the priority of a user's process
     |      Optimal way would require bubbling through the heap
     |
     |  change_ticket(self, ticket_type: str)
     |      Function to increase/reduce the number of ticket counts in counters
     |
     |  is_available(self, ticket_type)
     |      Method that tells whether ticket can be changed or not
     |
     |  process_tickets(self)
     |      Process from the priority queue from first to last
     |      Preferring VIPs first
     |      The first part of elements in the heapq is the priority
     |      higher number means low priority
     |
     |  remove_ticket(self, ticket_type: str)
     |      Function to subtract from ticket count
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  switch_ticket(ticket)
     |      Returns the other type of ticket, limits DRY
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  n_tickets
     |      return the number of tickets
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  N_REGULAR = 6
     |
     |  N_TOTAL = 9
     |
     |  N_VIP = 3
     |
     |  REGULAR = 'REGULAR'
     |
     |  TICKET_TYPES = {'REGULAR', 'VIP'}
     |
     |  VIP = 'VIP'

    class User(builtins.object)
     |  User(name, ticket, priority)
     |
     |  The User class
     |
     |  Methods defined here:
     |
     |  __init__(self, name, ticket, priority)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  cancel(self, ticket_system)
     |      Remove user from list of ticket registered users
     |
     |  make_change(self, ticket_system)
     |      Upgrade/Downgrade ticket
     |
     |  prioritize(self)
     |      Set priority for regular user
     |
     |  summarize(self)
     |      Provide summary for this user
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  login() -> set | None
     |      Log user in
     |
     |  make_id()
     |      Function for generating user id
     |
     |  register(ticket_system)
     |      Class method to add a new user
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  change
     |      The type of change that can be made for this user
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  id_length = 5
     |
     |  users = {'admin': ''}

FUNCTIONS
    main()
        Code starts execution here

    valid_input(prompt: str = 'Input: ', valid: set = None, upper: bool = False) -> str
        Function to persist until valid input gotten

DATA
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
