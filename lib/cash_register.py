#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.pricelist = []
    self.quantitylist = []
  def add_item(self,title,price,quantity=1):
    counter = 0
    while quantity > counter:
      self.items.append(title)
      self.pricelist.append(price)
      self.quantitylist.append(quantity)
      counter += 1
    self.total = self.total + (price * quantity)
  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total-((self.total / 100) * self.discount)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  def void_last_transaction(self):
    self.items.pop()
    self.total = self.total - (self.pricelist.pop() * self.quantitylist.pop())
    print(self.items)
    print(self.pricelist)
    print(self.quantitylist)
    print(self.total)