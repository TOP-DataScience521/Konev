def taxi_cost(long: int, time: int = 0) -> int | None:
   
    if long < 0 or time < 0:
        return None
    if not (isinstance(long, int) and isinstance(time, int)):
        return None 
    fine = 0
    if long == 0:
        fine = 80  
    cost = int(fine + 80 + (long / 150) * 6 + time * 3)
    return cost
    
    
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None
# >>> taxi_cost(100)
# 84
# >>>