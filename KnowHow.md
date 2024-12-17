# SETUP
create virtual env:

```
conda create -n drf_kanban python=3.12 anaconda
```

activate venv:

```
conda activate drf_kanban
```

## RUN APP

activate venv:

```
conda activate django_drf
```

run server:

```
python manage.py runserver
```

## ADD TO DB MANUALLY IN SHELL

open shell:
    ```
    python manage.py shell
    ```

add an entry to db manually:

```
from sales.models import  Customer
```

```
first_customer = Customer(first_name="Mandy", last_name="Musterfrau")
```

validate:
    ```
    first_customer.clean_fields()
    ```
save (no validation here!)
    ```
    first_customer.save()
    ```

or:

```
Customer.objects.create(first_name="Ralle", last_name="Musterdude")
```

## SEE DB ENTRIES VIA SHELL
see all entries for a model:
    ```
    Customer.objects.all()
    ```

find specific entry via column value:
    ```
    Customer.objects.get(first_name="Mandy")
    ```
find specific entry via id:
    ```
    Customer.objects.get(id=1)
    ```

## UPDATE DB ENTRY VIA SHELL

get entry:
    ```
    customer = Customer.objects.get(id=0)
    ```

update entry:
    ```
    customer.first_name = "NeuName"
    ```

save entry:
    ```
    customer.save()
    ```

## DELETE DB ENTRY VIA SHELL

get entry:
    ```
    customer = Customer.objects.get(id=1)
    ```
delete entry:
    ```
    customer.delete()
    ```

## CREATE SUPERUSER

```
python manage.py createsuperuser
```
(dev: johannes S22//)

access local admin page:
    ```
    http://127.0.0.1:8000/admin/
    ```

## RUN MIGRATIONS

create migrations:

```
python manage.py makemigrations
```

apply migrations:

```
python manage.py migrate
```

## SETUP

create virtual env:

```
conda create -n django_drf python=3.12 anaconda
```

activate venv:

```
conda activate django_drf
```

create project:

```
python -m pip install Django
```

install rest framework if desired:

```
python -m pip install djangorestframework
```
to enable rest, add to installed apps in settings.py:
    ```
    'rest_framework',
    ```

start project:

```
django-admin startproject database_testproject .
```

create app (use one of the two commands):

```
python manage.py startapp sales
```

```
django-admin startapp sales
```

update requirements.txt

```
pip freeze > requirements.txt
```

install django cors headers:

```
python -m pip install django-cors-headers
```

- initialize in settings.py
- add CSRF_TRUSTED_ORIGINS and CORS_ALLOWED_ORIGINS (frontend project port)

comment csrf feature for dev in settings.py:

```
# 'django.middleware.csrf.CsrfViewMiddleware',
```

## TIPPS

set debug to false to see error pages (settings.py):

```
DEBUG = False
```

## GIT

init git:

```
git init
```

add files:

```
git add .
```

commit:

```
git commit -m "initial commit"
```

add remote:

```
git remote add origin

```

push:

```
git push -u origin master
```

## SOME USEFUL QUERIES:
### execute this to python manage.py shell:


#################### SETUP DB ############################################################################

###  import *do this each time after opening the shell*
from sales.models import Product, ProductType, Bill, Order, Customer

### create objects
customer1 = Customer.objects.create(first_name="John", last_name="Doe", is_subscribed_to_newsletter=True, email_address="john.doe@example.com", account=100.0)
customer2 = Customer.objects.create(first_name="Jane", last_name="Smith", is_subscribed_to_newsletter=False, email_address="jane.smith@example.com", account=200.0)
customer3 = Customer.objects.create(first_name="Alice", last_name="Johnson", is_subscribed_to_newsletter=True, email_address="alice.johnson@example.com", account=300.0)

product1 = Product.objects.create(name="Product A", price=10.0)
product2 = Product.objects.create(name="Product B", price=20.0)
product3 = Product.objects.create(name="Product C", price=30.0)

bill1 = Bill.objects.create(total_amount=50.0, is_paid=False)
bill2 = Bill.objects.create(total_amount=100.0, is_paid=True)
bill3 = Bill.objects.create(total_amount=150.0, is_paid=False)
bill4 = Bill.objects.create(total_amount=250.0, is_paid=False)
bill5 = Bill.objects.create(total_amount=50.0, is_paid=False)

order1 = Order.objects.create(customer=customer1, bill=bill1)
order2 = Order.objects.create(customer=customer2, bill=bill2)
order3 = Order.objects.create(customer=customer3, bill=bill3)
order4 = Order.objects.create(customer=customer3, bill=bill4)
order5 = Order.objects.create(customer=customer3, bill=bill5)

ProductType.objects.create(order=order1, product=product1, type_name="Wood")
ProductType.objects.create(order=order1, product=product2, type_name="Iron")

ProductType.objects.create(order=order2, product=product1, type_name="Wood")
ProductType.objects.create(order=order2, product=product3, type_name="Plastic")

ProductType.objects.create(order=order3, product=product1, type_name="Wood")
ProductType.objects.create(order=order3, product=product2, type_name="Iron")
ProductType.objects.create(order=order3, product=product3, type_name="Plastic")


### delete all

ProductType.objects.all().delete()
Order.objects.all().delete()
Bill.objects.all().delete()
Customer.objects.all().delete()
Product.objects.all().delete()

################## EXAMPLES *(see django docs for details) ########################################################

###  import *do this each time after opening the shell*
from sales.models import Product, ProductType, Bill, Order, Customer

### some queries
orders = Order.objects.all()
orders[0].products.all()

customer = Customer.objects.all()[1]
customer.order_set.all()

### some filters
Bill.objects.filter(is_paid=True)
Bill.objects.filter(total_amount__gt=100.0) # total_amount greater than 100
Bill.objects.filter(total_amount__lt=105.0) # total_amount less than 105
Bill.objects.filter(total_amount__lte=100.0) # total_amount less than or equal to 100
Customer.objects.filter(first_name__startswith="J") # first_name starts with J
Customer.objects.filter(first_name__contains="a") # first_name contains a
Customer.objects.filter(first_name__endswith="e") # first_name ends with e

### show sql query for a queryset
str(Bill.objects.filter(total_amount__gt=100.0).query)

### limit and offset
Bill.objects.all()[:2].get() # limit to 2
Bill.objects.all()[2:4].get() # offset 2, limit 2

### Q functions; or, and, not
from django.db.models import Q

Bill.objects.filter(Q(total_amount__gt=100.0) | Q(is_paid=True)) # total_amount greater than 100 or is_paid is True
Bill.objects.filter(Q(total_amount__gt=100.0) & Q(is_paid=False)) # total_amount greater than 100 and is_paid is False
Bill.objects.exclude(Q(total_amount__gt=100.0) & Q(is_paid=False)) # opposite of filter

### get data from relations and filter
Customer.objects.all()[1].order_set.all()[0] # get the first order of the second customer
Customer.objects.all()[0].order_set.filter(bill__total_amount__lt=100.0) # get orders of the first customer with total_amount less than 100

### order by
Customer.objects.order_by('first_name') # order by first_name ascending
Customer.objects.order_by('-first_name') # order by first_name descending
Order.objects.order_by(-'bill__total_amount') # order by total_amount descending

### aggrevations
from django.db.models import Avg, Max, Min, Sum, Count

Bill.objects.aggregate(Avg('total_amount', default=0)) # average of total_amount with default 0
Bill.objects.aggregate(Max('total_amount')) # maximum of total_amount
Bill.objects.aggregate(Min('total_amount')) # minimum of total_amount
Bill.objects.aggregate(Sum('total_amount')) # sum of total_amount
Bill.objects.aggregate(Count('total_amount'))  # count (amount) of total_amount

orders = Customer.objects.annotate(num_orders=Count('order')) # annotate count of orders for each customer
orders[2].num_orders # access the count for the third customer
