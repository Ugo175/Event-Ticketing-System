"""Event Ticketing System
Uses a min heap to keep order of users

Removing ticket
"""
import csv
import datetime
import heapq

from collections import deque
from random import choice, randint, sample


def main():
    """Code starts execution here"""
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

    def __init__(self, name, ticket):
        self.active = False

    def x(self):
        """Hi"""
        return 3

print(TicketSystem(1, 2).n_tickets)
