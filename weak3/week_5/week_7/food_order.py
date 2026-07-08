def calculate_total(price, quantity):
    if price <= 0:
        return "invalid price"

    if quantity <= 0:
        return "invalid quantity"

    return price * quantity