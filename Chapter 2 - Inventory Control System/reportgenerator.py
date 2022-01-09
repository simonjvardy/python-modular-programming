"""
Report Generator Module
"""

import datastorage


def generate_inventory_report():
    """
    Function to create the inventory report
    import a list of products, a list of locations and a list of items
    from the datastorage module and generate a simple text-based report
    from the contents of these lists.
    """
    product_names = {}
    for product_code, name, desired_number in datastorage.products():
        product_names[product_code] = name

    location_names = {}
    for location_code, name in datastorage.locations():
        location_names[location_code] = name

    grouped_items = {}
    for product_code, location_code in datastorage.items():
        if product_code not in grouped_items:
            grouped_items[product_code] = {}

        if location_code not in grouped_items:
            grouped_items[product_code][location_code] = 1
        else:
            grouped_items[product_code][location_code] += 1

    report = []
    report.append("INVENTORY REPORT")
    report.append("")

    for product_code in sorted(grouped_items.keys()):
        product_name = product_names[product_code]
        report.append("Inventory for product: {} - {}"
            .format(product_code, product_name))
        report.append("")

        for location_code in sorted(grouped_items[product_code].keys()):
            location_name = location_names[location_code]
            num_items = grouped_items[product_code][location_code]
            report.append("  {} at {} - {}"
                .format(num_items, location_code, location_name))
        report.append("")

    return report


def generate_reorder_report():
    """
    Function to create the re-order report
    import a list of products and a list of items in inventory
    from the datastorage module and generate a simple text-based report
    from the contents of these lists.
    """
    product_names = {}
    desired_numbers = {}

    for product_code, name, desired_number in datastorage.products():
        product_names[product_code] = name
        desired_numbers[product_code] = desired_number

    num_in_inventory = {}
    for product_code, location_code in datastorage.items():
        if product_code in num_in_inventory:
            num_in_inventory[product_code] += 1
        else:
            num_in_inventory[product_code] = 1

    report = []
    report.append("RE-ORDER REPORT")
    report.append("")

    for product_code in sorted(product_names.keys()):
        desired_number = desired_numbers[product_code]
        current_number = num_in_inventory.get(product_code, 0)
        if current_number < desired_number:
            product_name = product_names[product_code]
            num_to_reorder = desired_number - current_number
            report.append("  Re-order {} of {} - {}"
                .format(num_to_reorder, product_code, product_name))

    report.append("")

    return report
