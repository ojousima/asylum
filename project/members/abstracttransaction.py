#!/usr/bin/python
# -*- coding: utf-8 -*-

class AbstractTransaction(object):
    "Exchange format for monetary transactions. Any import/export tool should use this as intermediary format"

    name      = None # name of sender / receiver, optional
    amount    = None # positive = income, negative = expence, required
    ID        = None # unique Id of transaction - SHA-1 of fields for example, required
    timestamp = None # date of transaction, required
    reference = None # reference number of transaction, not unique, optional
    message   = None # Freeform message, optional

    def __init__(self, amount, timestamp, ID):
        self.amount = amount
        self.timestamp = timstamp
        self.ID = ID

    def __repr__(self):
        return "<AbstractTransaction ID:%s amt:%s date:%s reference:%s>" \
                % (self.ID, self.amount, self.timestamp, self.reference)


