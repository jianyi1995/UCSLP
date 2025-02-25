import random
import json

def generateInstance(num_users, num_stations, x_range, y_range, charging_time_range, charging_fee_range,
                     num_piles_range, cost_range):
    # coordinates of users
    users = [(random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])) for _ in range(num_users)]
    
    # coordinates of stations
    stations = [(random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])) for _ in range(num_stations)]
    
    charging_times = random.randint(charging_time_range[0], charging_time_range[1])
    charging_fees = random.randint(charging_fee_range[0], charging_fee_range[1])
    
    # randomly generated number of charging piles
    num_piles = []
    costs = []
    for _ in range(num_stations):
        piles = random.randint(num_piles_range[0], num_piles_range[1])
        base_cost = piles * random.randint(cost_range[0], cost_range[1])
        # there is an approximately direct proportional relationship between piles and cost.
        cost_variation = random.randint(-int(base_cost * 0.1), int(base_cost * 0.1))  
        cost = base_cost + cost_variation
        num_piles.append(piles)
        costs.append(cost)
    
    # return results
    return {
        "users": users,
        "stations": stations,
        "charging_times": charging_times,
        "charging_fees": charging_fees,
        "num_piles": num_piles,
        "costs": costs
    }



def saveInstanceToFile(instance, filename):
    with open(filename, 'w') as f:
        json.dump(instance, f, indent=4)


if __name__ == '__main__':
    num_users = 10
    num_stations = 4
    x_range = (0, 15)
    y_range = (0, 15)
    charging_time_range = (360, 360)
    charging_fee_range = (10, 10)
    num_piles_range = (1, 3)
    cost_range = (4, 8)

    instance = generateInstance(num_users, num_stations, x_range, y_range, charging_time_range, charging_fee_range, 
                                num_piles_range, cost_range)
    saveInstanceToFile(instance, 'instance.json')

    print(instance)
