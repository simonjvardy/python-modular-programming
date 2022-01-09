"""
Report Generator Module
"""

import datastorage


def generate_inventory_report():
    """
    Function to create the inventory report
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
