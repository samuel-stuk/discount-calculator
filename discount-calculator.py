def find_possible_discounts(subtotal, target_total, tolerance=0.01):
    """
    Find all whole-number discount percentages (1–99) that can reach the target total
    by adding an amount to the subtotal before applying the discount.

    Args:
        subtotal (float): Original price before any additions.
        target_total (float): Desired price after discount.
        tolerance (float): Acceptable rounding error.

    Returns:
        List of tuples: (discount_percent, amount_to_add, final_total)
    """
    results = []
    for discount_percent in range(1, 100):
        discount_multiplier = 1 - discount_percent / 100
        try:
            required_addition = (target_total / discount_multiplier) - subtotal
            if required_addition < 0:
                continue  # Can't subtract, only add

            final_total = (subtotal + required_addition) * discount_multiplier
            if abs(final_total - target_total) <= tolerance:
                results.append((discount_percent, required_addition, final_total))
        except ZeroDivisionError:
            continue

    return results


# Enter values here and run the script
subtotal = 21546.32 # Original price
target_total = 11450.00 # Desired price

matches = find_possible_discounts(subtotal, target_total)

if matches:
    print(f"Discount options to reach £{target_total} from £{subtotal}:\n")
    for discount_percent, addition, final in matches:
        print(f"- Add £{addition:.2f} → Apply {discount_percent}% discount → Final: £{final:.2f}")
else:
    print("No suitable discount + addition combinations found.")
