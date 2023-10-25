
import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pandeyji_eatery"
)

def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()
        #calling the stored procedure
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))

        #Committing the changes

        cnx.commit()

        #Closing cursor
        cursor.close()

        print("Order item inserted successfully!")

        return 1
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        #Rollback changes if necessary

        cnx.rollback()

        return -1
    
    except Exception as e:
        print(f"An error occurred : {e}")

        cnx.rollback()
        return -1

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    #Fetching the result
    result = cursor.fetchone()[0]

    #closing the cursor

    cursor.close()

    return result
    

def get_next_order_id():
    cursor = cnx.cursor()

    #Executing the SQL order to get the next available order_id
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    #Fetching the result

    result = cursor.fetchone()[0]

    #Closing the cursor 
    cursor.close()

    # Returning the next available order_id

    if result is None:
        return 1
    else:
        return result + 1

def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()
    #inserting the record into the order tracking table

    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES(%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    cnx.commit()
    cursor.close()

def get_order_status(order_id: int):
    cursor = cnx.cursor()


    query = ("SELECT status FROM order_tracking WHERE order_id = %s")

    #execute the query

    cursor.execute(query,(order_id,))

    #Fetch the result

    result = cursor.fetchone()

    #Close the cursor and connection
    cursor.close()
    

    if result is not None:
        return result[0]
    
    else:
        return None