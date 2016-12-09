print "================="
print "1.  Returning Customer"
print "2.  New Customer"
print "3.  Guest"
print "================="
option = 0


def get_customer():
    customer_id = raw_input('Please enter your user ID: \n')
    print '\n'
    return customer_id


def find_customer(customer_id):
    try:
        with open('CustomerList.txt', 'r+') as lists:
            customer_list = lists.readlines()
            for line in customer_list:
                record = line.split(',')
                if customer_id == record[0]:
                    return record
        return 'none'

    except IOError:
        print ("File not found")


def confirm():
    confirmation = raw_input("Is this information correct: \nY/N\n").capitalize()

    if confirmation == 'N':
        print "Sorry, please try again \n"
        returning()

    else:
        print 'Thank you'


def returning():
    customer = get_customer()
    records = find_customer(customer)
    if records == 'none':
        print "Customer ID not found"
        returning()

    else:
        for items in records:
            print items

        confirm()
    return


while option < 1 or option > 3:
    option = (int(raw_input("Choose a customer type, enter 1, 2, or 3: \n")))
    if option == 1:
        returning()
    elif option == 2:
        print "You selected New Customer. \n"
    elif option == 3:
        print 'You selected Guest.'
    else:
        print ValueError('Please select 1 for Returning Customer, 2 for New Customer, or 3 for Guest.')
