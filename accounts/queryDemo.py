from accounts.models import *

#return all customers from the Customer Table
customers = Customer.objects.all()
print(customers)

#return first customer in table
print(customers.first())
firstCustomer = Customer.objects.first()

#return last customer in table
print(customers.last())
lastCustomer = Customer.objects.last()

#return single customer by name
customerByName = Customer.objects.get(name='goldy')
print(customerByName)

#return single customer by id
customerById = Customer.objects.get(id=2)
print(customerById)

#return all orders related to customer (firstCustomer) output = order 1 & 2 are made by John borel
#return first customer
firstCustomer = Customer.objects.first()
#print all orders related to that first customer
order = firstCustomer.order_set.all() 
#print  
print(order)

#return order and then from that get customer name who made the order
order = Order.objects.first()
customerName = order.customer.name
print(customerName)

#return products from products table with value from dropdown
products = Product.objects.filter(category='Out Door') #can add many value to the filter
print(products)

#Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
print(leastToGreatest)
#contrary, just add a '-'
greatestToLeast = Product.objects.all().order_by('-id')
print(greatestToLeast)

#return all products with tag of "sports"
#to query a manyt-many "attribute-name__name"
productsFiltered =Product.objects.filter(tags__name="sports")
print(productsFiltered)

#return the total count for number of time a ball was ordered by the first cusomer
ballOrders = firstCustomer.order_set.filter(product__name="ball").count()
print(ballOrders)

#return total count for each products or nuber of time each products have been ordered
allOrders = {}
for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
        
#returns allOrders: {'Ball':2, 'food':3}