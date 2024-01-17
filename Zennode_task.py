
# Function to calculate discount based on rules
def calculate_discount(cart, rules):
    max_discount = 0
    discount_name = ""

    for rule, condition in rules.items():
        if condition(cart):
            current_discount = condition(cart)
            if current_discount > max_discount:
                max_discount = current_discount
                discount_name = rule

    return discount_name, max_discount

# Function to calculate total cost including discounts and fees
def calculate_total(cart, discounts, gift_wrap_fee, shipping_fee):
    subtotal = sum(product['quantity'] * product['price'] for product in cart)
    discount_name, discount_amount = calculate_discount(cart, discounts)

    total_discounted_price = subtotal - discount_amount
    total_gift_wrap_fee = sum(product['quantity'] for product in cart) * gift_wrap_fee
    total_shipping_fee = (sum(product['quantity'] for product in cart) // 10) * shipping_fee

    total = total_discounted_price + total_gift_wrap_fee + total_shipping_fee

    return subtotal, discount_name, discount_amount, total_gift_wrap_fee, total_shipping_fee, total

# Function to take user input for each product
def get_product_info(product_name):
    quantity = int(input(f"Enter the quantity of {product_name}: "))
    gift_wrap = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == 'yes'

    return {'name': product_name, 'quantity': quantity, 'gift_wrap': gift_wrap}

# Main program
def main():
    products = [
        {'name': 'Product A', 'price': 20},
        {'name': 'Product B', 'price': 40},
        {'name': 'Product C', 'price': 50},
    ]

    discounts = {
        "flat_10_discount": lambda cart: sum(product['quantity'] * product['price'] for product in cart) > 200,
        "bulk_5_discount": lambda cart: any(product['quantity'] > 10 for product in cart),
        "bulk_10_discount": lambda cart: sum(product['quantity'] for product in cart) > 20,
        "tiered_50_discount": lambda cart: sum(product['quantity'] for product in cart) > 30 and any(product['quantity'] > 15 for product in cart),
    }

    gift_wrap_fee = 1
    shipping_fee = 5

    cart = [get_product_info(product['name']) for product in products]

    subtotal, discount_name, discount_amount, total_gift_wrap_fee, total_shipping_fee, total = calculate_total(cart, discounts, gift_wrap_fee, shipping_fee)

    # Output
    print("\nProduct Details:")
    for product in cart:
        print(f"{product['name']} - Quantity: {product['quantity']} - Total: ${product['quantity'] * product['price']}")

    print("\nSubtotal:", f"${subtotal}")
    print("Discount Applied:", f"{discount_name} - ${discount_amount}")
    print("Gift Wrap Fee:", f"${total_gift_wrap_fee}")
    print("Shipping Fee:", f"${total_shipping_fee}")
    print("\nTotal:", f"${total}")

if __name__ == "__main__":
    main()










        




