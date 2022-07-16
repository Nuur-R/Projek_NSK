import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='nsk',
                                         user='root',
                                         password='')

def find_cardID(card_number):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM card WHERE cardID = %s", (card_number,))
    card_id = cursor.fetchone()
    return card_id

def data_checker(card_number):
    card_id = find_cardID(card_number)
    # print ("card_id: ")
    # print(type(card_id))
    # print("card_number: ")
    # print(type(card_number))
    if card_id is None:
        print('Card not found')
        return False
    else:
        print('Card found = = = == = = = = == = ')
        return True


print(data_checker('247 162 130 203'))