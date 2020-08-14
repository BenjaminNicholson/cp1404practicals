"""
Benjamin Nicholson
CP1404 Electricity bill
Calculates the price of the electricity bill
"""

# def main():
#     print("Electricity bill estimator")
#     cents_per_kwh = float(input("Enter cents per KWh: "))
#     daily_use = float(input("Enter daily use in KWh: "))
#     billing_days_number = int(input("Enter number of billing days: "))
#     cost_per_day = cents_per_kwh * daily_use
#     cost_per_quarter = cost_per_day * billing_days_number
#     print(f"Estimated bill: ${cost_per_quarter:.02f}")
#
#
# main()


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator 2.0")
    cents_per_kwh = int(input("Which tariff? 11 or 31: "))

    if cents_per_kwh == 11:  # calculates the tariff charge for cents per hour
        cents_per_kwh = 0.244618
    else:
        cents_per_kwh = 0.136928

    daily_use = float(input("Enter daily use in KWh: "))
    billing_days_number = int(input("Enter number of billing days: "))
    cost_per_day = cents_per_kwh * daily_use
    cost_per_quarter = cost_per_day * billing_days_number
    print(f"Estimated bill: ${cost_per_quarter:.02f}")


main()
