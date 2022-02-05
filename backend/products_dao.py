from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()

    query = "select product_id, name, price_per_unit, uom_name from  grocery_store.products " \
            "inner join grocery_store.uom on grocery_store.products.uom_id = grocery_store.uom.uom_id;"

    response = []
    cursor.execute(query)

    for (PRODUCT_ID, NAME, PRICE_PER_UNIT, UOM_NAME) in cursor:
        response.append({
            'PRODUCT_ID': PRODUCT_ID,
            'NAME': NAME,
            'PRICE_PER_UNIT': PRICE_PER_UNIT,
            'UOM_NAME': UOM_NAME
        })

    connection.close()
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = "insert into products (name, uom_id, price_per_unit) values (%s, %s, %s)"
    data = (product['PRODUCT_NAME'], product['UOM_ID'], product['PRICE_PER_UNIT'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where  product_id="+ str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == "__main__":
    connection = get_sql_connection()
    # print(get_all_products(connection))
    # print(insert_new_product(connection, {
    #     'PRODUCT_NAME': 'Cabbage',
    #     'UOM_ID': '1',
    #     'PRICE_PER_UNIT': '40'
    # }))
    print(delete_product(connection, 3))
