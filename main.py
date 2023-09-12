
def count_batteries_by_health(present_capacities):
  rated_capacity = 120 
  battery_count = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  
  for capacity in present_capacities:
    SoH = 100 * capacity / rated_capacity #Calculate the SoH % of each battery

    #Increment the values in battery_count based on the given range of SoH
    if SoH >= 80 and SoH <= 100:
      battery_count["healthy"] += 1
    elif SoH >= 63 and SoH < 80:
      battery_count["exchange"] += 1
    elif SoH < 63 and SoH >= 0:
      battery_count["failed"] += 1
    else:
      print('Invalid value of SoH for battery with capacity', capacity) #Error message for batteries with SoH values above 100 or below 0
      
  return battery_count
  
def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
