# Collect user input
principal = float(input("Enter the initial investment amount: "))
rate = float(input("Enter the annual interest rate (as decimal): "))
years = int(input("Enter the number of years: "))

# Store original principal for final comparison
initial_amount = principal

print("\n📆 Yearly Growth Breakdown")
print("Year\tValue")

# Loop through each year and update principal
for year in range(1, years + 1):
    principal *= (1 + rate)
    print(f"{year}\t${principal:,.2f}")

# Show final result outside the loop
print(f"\n✅ Final Amount after {years} years is: ${principal:,.2f}")
print(f"💡 Total Gain: ${principal - initial_amount:,.2f}")
