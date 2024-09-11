import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products


# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
async def checkout_customer(queue: Queue, cashier_number: int):
    customer_count = 0
    checkout_start = time.perf_counter()
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"The Casshier_{cashier_number} "
            f"will checkout Customer_{customer.customer_id} ")
        for product in customer.products:
            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} "
                  f"in {product.checkout_time} secs ")
            await asyncio.sleep(product.checkout_time)
        print(f"The Cashier_{cashier_number} "
              f"finished checkout Customer_{customer.customer_id} "
              f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs ")
        
        customer_count += 1
        total_time = round(time.perf_counter() - checkout_start, ndigits=2)
        queue.task_done()

    return {'id': cashier_number, 'customer': customer_count, 'time': total_time}

# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id) for the_id in range(customer_count, customer_count+customers)]
        for customer in customers:
            print("Waiting to put customer in line...")
            await queue.put(customer)
            print("Customer put in line...")
            print(f"{queue.qsize()} Customer in queue")
        customer_count = customer_count + len(customers)
        time.sleep(0.001)
        return customer_count

# Finally, we use the main method to initialize the queue, 
# producer, and consumer, and start all concurrent tasks.
async def main():
    customer_queue = Queue(5)
    customer_start_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, 20))
    cashiers = [checkout_customer(customer_queue, i) for i in range(5)]

    result = await asyncio.gather(customer_producer, *cashiers)
    print(f"The supermarket process finished "
          f"{customer_producer.result()} customers "
          f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs\n")
    
    for cashier in result[1:]:
        print(f"The Cashier_{cashier['id']} take {cashier['customer']} total {cashier['time']} secs.")


if __name__ == "__main__":
    asyncio.run(main())

# +--------|------------|-------------|-----------------------|----------------------------------------------------------------    
# Customer | Queue      | Cashier	  |             Customer/time by Cashier                                        | 
# ---------|------------|-------------|-----------------------------------------------------------------------------|   Total
#          |            |             | c   | 0     | c     | 1     | c     | 2     | c     | 3     | c     | 4     |
#----------|------------|-------------|-----|-------|-------|-------|-------|-------|-------|-------|-------|-------|----------
# 2	       | 2	        | 2		      | 1   | 2.0s  | 1     | 2.0s  |       |       |       |       |       |       |   2.01s
# 3	       | 2	        | 2		      | 2   | 4.0s  | 1     | 2.0s  |       |       |       |       |       |       |   4.01s                           		
# 4	       | 2	        | 2		      | 2   | 4.0s  | 2     | 4.0s  |       |       |       |       |       |       |   4.01s
# 5	       | 5	        | 5		      | 1   | 2.0s  | 1     | 2.0s  | 1     | 2.0s  | 1     | 2.0s  | 1     | 2.0s  |   2.01s
# 10	   | 3	        | 3			  | 4   | 8.0s  | 3     | 6.0s  | 3     | 6.0s  |       |       |       |       |   8.03s
# 10	   | 3			| 5           | 4   | 8.0s  | 3     | 6.0s  | 3     | 6.0s  |       |       |       |       |   8.02s
# 20       | 5          | 5           | 4   | 8.0s  | 4     | 8.0s  | 4     | 8.0s  | 4     | 8.0s  | 4     | 8.0s  |   8.02s
# +--------|------------|-------------|----------------------------------------------------------------------------------------  