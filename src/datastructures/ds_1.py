
# this function return tuples - tuples are immutable and size can't change
def find_pe_and_pb(price,eps,book_value):
    pe = price/eps
    pb = price/book_value

    return pe, pb

# Dictinary
# We can call d[key] - incase key doesn't exists it returns error
# Alternative way is d.get(key) - incase key doesn't exists returns None

def country_product() :
    appl_revenues = {"USA" : { "iPhone": 20, "iPad" : 12, "MacBook": 8},
                     "Chine" : { "iPhone": 20, "iPad": 12, "MacBook": 8},
                     "India" : {"iPhone": 20, "iPad": 12, "MacBook": 8}
                     }
    
    # we will get key value using items function on the dictornary

    for country, product_data in appl_revenues.items() :
        for product, rev in product_data.items():
            print(f"{country} and {product} revenue is {rev} millions")


if __name__ == "__main__" :
    
    pe_ratio, pb_ratio = find_pe_and_pb(100,2,4)

    print(f"PE Ration : {pe_ratio}  PBRation : {pb_ratio}")

    d = {"name":"Monish", "age": 15}

    value = d.get("book")
    
    # Key doesn't exist in the dictonary it returns None
    print(value)

    country_product()