def cost_delivery(quantity, *some, discount=0):
  if quantity:
    cost = (3 + (quantity * 2))
  if discount:
    cost = cost * discount
  return cost 