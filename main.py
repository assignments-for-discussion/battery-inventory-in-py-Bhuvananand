
def count_batteries_by_health(present_capacities):
  rated_capacity = 120
  for capacity in present_capacities:
    SoH = 100 * capacity / rated_capacity

    battery_count = {}
    if SoH >= 80:
      SoH_dict['healthy'] += 1
    elif SoH >=63 and SoH < 80:
      SoH_dict['exchange'] += 1
    elif SoH <63:
      SoH_dict['failed'] += 1
      
  return SoH_dict
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }


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
