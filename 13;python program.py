
def count_notes(amount):
   denominations = [1000, 500, 100, 50, 20, 10, 5, 1]
   notes_count = {}
   for denomination in denominations:
       if amount >= denomination:
           count = amount // denomination  # Count how many notes of this denomination
           notes_count[denomination] = count
           amount -= count * denomination  # Reduce the amount
   return notes_count
try:
   amount = int(input("Enter the amount: "))
   if amount < 0:
       print("Please enter a valid positive amount.")
   else:
       notes = count_notes(amount)
       print("Total number of notes required:")
       for denomination, count in notes.items():
           print(f"₹{denomination}: {count} notes")
except ValueError:
   print("Please enter a valid integer.")