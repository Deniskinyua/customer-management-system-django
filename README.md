## Customer Management System with Django

### Project Description
Welcome to my project where i build a django application with Docker.

The application works as follows:

> But first, imagine this: You own a shop selling different items for example phones, accessories e.t.c. You would like to have an in-house system that helps yomanage customer orders, right? perfect. I have the right solution for you.

>    1. so,the user (shop owner / staff) registers at the login page. They can do so in 2 ways:
>       - via django authentication,
>       - OpenID via Facebook and Github.
Once logged in, they are met with a dashboard displaying different items:

2. The output of the program should be:
    - A `dashbaord preview`: ( Enables them to view the 5 latest invoices/receipts/notes provided or issued)
    - A complete `statistics dashboard` : Displays a breakdown of different items (customers, orders and ino), and (i've saved the best for last..)
    - `Invoice creation page` : They will use this to create different entries especially invoices, receipts e.t.c. How does it work?
3. User clicks the create invoices button, and is transferred to an invoice creattion page
4. They enter the details of the entry (notice that you can add colums if more entries are required per customer)
5. The entry autocalculates all entries into one entry ( you dont want to have too many reciepts for just one order)
6. upon saving (hit save), the receipt is added to the database, the user is directed to a new page : the invoice view page.
7. In the invoice page they get to see what they have added. But before we proceed, see that when the record is saved a prompt is shown to confirm.
8. Then, a message is sent to the customer that their order has been placed (how awesome!)
9. On this page, the user can edit a receipt (if wrongfully entered or even delete it entirely)
10. If they are satisfied, they can hit done and are redirected to the dashboard.

Vuala! 

## Setup
 - You can build the project with the following command
 - Activate the python environment
  `source my-env/bin/activate `
- Then build:
 `docker-compose up --build`
- Expect the project to be running at `port : 8000`

- Then have a look at the system design and CI-CD designs below

### System Design
![system design](images/system-design-primer.png)

## CI/CD Pipeline

![system design](images/ci-cd.png)
