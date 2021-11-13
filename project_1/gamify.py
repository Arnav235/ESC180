def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time

    # global last_activity, last_activity_duration
    
    # global last_finished
    global cur_star, cur_star_activity
    global bored_with_stars
    global last_two_star_offerings
    global time_since_last_running_carrying
    global past_time_running

    cur_hedons = 0
    cur_health = 0
    
    cur_star = False
    cur_star_activity = None
    
    bored_with_stars = False
    last_two_star_offerings = []
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    time_since_last_running_carrying = 200
    past_time_running = 0
    
    last_finished = -1000
    

def is_tired():
    return time_since_last_running_carrying < 120

def star_can_be_taken(activity):
    return (not bored_with_stars and cur_star) and cur_star_activity == activity

    
def perform_activity(activity, duration):
    global cur_time, cur_health, cur_hedons, time_since_last_running_carrying, cur_star, past_time_running
    if activity == "running":
        #health points
        if past_time_running > 180:
            cur_health += duration
        elif (duration+past_time_running) > 180:
            cur_health += 3 * (180-past_time_running)
            cur_health += (duration+past_time_running - 180)
        else:
            cur_health += 3 * duration

        #hedons
        if is_tired():
            cur_hedons -= 2 * duration
        else:
            if duration <= 10:
                cur_hedons += 2 * duration
            else:
                cur_hedons += 2 * 10
                cur_hedons -= 2 * (duration - 10)

        time_since_last_running_carrying = 0
        past_time_running += duration
    if activity == "resting":
        time_since_last_running_carrying += duration
        past_time_running = 0

    if activity == "textbooks":
        #health points
        cur_health += 2 * duration

        #hedons
        if is_tired():
            cur_hedons -= 2 * duration
        else:
            if duration < 20:
                cur_hedons += duration
            else:
                cur_hedons += 20
                cur_hedons -= (duration - 20)

        time_since_last_running_carrying = 0
        past_time_running = 0

    if star_can_be_taken(activity):
        cur_hedons += 3 * min(10, duration)
    cur_star = False
    cur_time += duration

def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    global cur_star, cur_star_activity, last_two_star_offerings
    cur_star = True
    cur_star_activity = activity
    last_two_star_offerings.append([activity, cur_time])
    check_bored_of_stars()

def check_bored_of_stars():
    global last_two_star_offerings, bored_with_stars
    if len(last_two_star_offerings) == 3:
        if (last_two_star_offerings[2][1] - last_two_star_offerings[0][1]) < 120:
            bored_with_stars = True
        last_two_star_offerings = last_two_star_offerings[1:]

def most_fun_activity_minute():
    #hedons
    run_sum = 0
    if is_tired():
        run_sum -= 2
    else:
        run_sum += 2
    if star_can_be_taken("running"): 
        run_sum += 3

    textbook_sum = 0
    if is_tired():
        textbook_sum -= 2
    else:
        textbook_sum += 1 
    if star_can_be_taken("textbooks"):
        textbook_sum += 3
    
    if run_sum > textbook_sum and run_sum > 0:
        return "running"
    elif textbook_sum > run_sum and textbook_sum > 0:
        return "textbooks"
    else:
        return "resting"

################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10