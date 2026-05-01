'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = Decimal ('100000')
MAX_QUANTITY = 100
MIN_QUANTITY = 0
MAX_ORDER_TOTAL = Decimal('1000000')


def _validate_payment(item):
    """Return the payment amount if valid, else None"""
    if -MAX_ITEM_AMOUNT <= Decimal(str(item.amount)) <= MAX_ITEM_AMOUNT:
        return Decimal(str(item.amount))
    return None

def _validate_product(item):
    """Return the line total if valid, else None."""
    if (
        isinstance(item.quantity, int)
        and MIN_QUANTITY < item.quantity <= MAX_QUANTITY
        and MIN_QUANTITY < item.amount <= MAX_ITEM_AMOUNT
    ):
        return Decimal(str(item.amount)) * item.quantity
    return None


def validorder(order):
    payments = Decimal('0')
    expenses = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            amount = _validate_payment(item)
            if amount is not None:
                payments += amount

        elif item.type == 'product':
            line_total = _validate_product(item)
            if line_total is not None:
                expenses += line_total

        else:
            return f"Invalid item type: {item.type}"

    if abs(payments) > MAX_ORDER_TOTAL or expenses > MAX_ORDER_TOTAL:
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return f"Order ID: {order.id} - Payment imbalance: ${payments - expenses:0.2f}"

    return f"Order ID: {order.id} - Full payment received!"