#! /usr/bin/env python

import sys
import random as rnd
import time
################################################################
#                   This will later be turned
#           into a more object-oriented design in time!
################################################################

# Running number of solves
num_solves = 0

# Average number of moves in a 3x3 scramble
num_moves = 22

# List of possible moves you can use to scramble
moves = ['R', 'L', 'D', 'U', 'F', 'B', 
            'R2', 'L2', 'D2', 'U2', 'F2', 'B2', 
            'R\'', 'L\'', 'D\'', 'U\'', 'F\'', 'B\'']

# Number of possinble moves in the movelist
move_options = len(moves)

###############################################################
#             Helper method written for running
#               the main timer loop iteration 
#                and adding user-interaction
###############################################################

def scramble():
    # Empty list to be filled
    scramble_list = []
    # Generates random moves until length is satisfied
    while (len(scramble_list) != num_moves):
        # Calculations to help option selection
        list_length = len(scramble_list)
        option = moves[rnd.randrange(0, move_options - 1)]
        # Simple append
        if (list_length == 0):
            scramble_list.append(option)
        # Checks prior addition is not equal to current option
        elif (list_length == 1):
            if (scramble_list[-1] != option):
                if (scramble_list[-1][0] != option[0]):
                    scramble_list.append(option)
        # Checks prior two additions are not equal to current option
        else:
            if (scramble_list[-1] != option and scramble_list[-2] != option):
                if (scramble_list[-1][0] != option[0] and scramble_list[-2][0] != option[0]):
                    scramble_list.append(option)

    scramble_text = ""
    # Concatenates list elements to string for readability
    for letter in scramble_list:
        scramble_text += letter + " "
    print(scramble_text)


###############################################################
#               Helper method written for doing
#       calculations to find the time between start and stop
###############################################################

def time_math(start, end):
    time_between = (end - start) # Calculate start from end
    mins = time_between // 60    # Calculate mins
    sec = time_between % 60    # Calculate hours
    hours = mins // 60
    mins = mins % 60             # Add the extra minutes

    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


def time_save(time_between2):
    mins = time_between2 // 60    # Calculate mins
    sec = time_between2 % 60    # Calculate hours
    hours = mins // 60
    mins = mins % 60             # Add the extra minutes

    return [int(hours), int(mins), sec]

###############################################################
#           This method is for returning a 'running'
#       average. Meaning the last 5 solves are averaged
#           together and a current avg is calculated.
###############################################################

def calc_run_avg(times):
    last_five = times[-5:]
    last_five.remove(min(last_five)) # Remove fastest time
    last_five.remove(max(last_five)) # Remove slowest time
    mid_three = (sum(last_five) / len(last_five)) # Sum up remaining three times
    mid_three_avg = time_save(mid_three)
    return mid_three_avg


###############################################################
#               This main method will be run in a 
#               continuous loop, with scrambling,
#                   and interactive responses
###############################################################

def main(all_times, num_solved):
    dots= ['.', '..', '...']

    print("Your 3x3 scramble is: ")
    print("")
    scramble()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Press ENTER to start/end timer")
    print("Press any key plus ENTER to quit")
    if (len(all_times) == 0):
        print("Session best not recorded yet.")
        print("Session worst not recorded yet.")
    elif (len(all_times) == 1):
        oneSolve = time_save(min(all_times))
        mins = oneSolve[1]    # Calculate mins
        sec = oneSolve[2]    # Calculate seconds
        hours = oneSolve[0]    # Calculate hours
        print("Session best = {0}:{1}:{2}".format(hours, mins, sec))
        print("Session worst = {0}:{1}:{2}".format(hours, mins, sec))
    else:
        print("Total number of solves: " + str(num_solved))
        currBest = time_save(min(all_times))
        currWorst = time_save(max(all_times))
        seshAvg = time_save((sum(all_times) / len(all_times)))
        mins = currBest[1]    # Calculate mins
        sec = currBest[2]    # Calculate seconds
        hours = currBest[0]     # Calculate hours
        print("Session best = {0}:{1}:{2}".format(hours, mins, sec))
        mins2 = currWorst[1]    # Calculate mins
        sec2 = currWorst[2]    # Calculate seconds
        hours2 = currWorst[0]     # Calculate hours
        print("Session worst = {0}:{1}:{2}".format(hours2, mins2, sec2))
        mins3 = seshAvg[1]    # Calculate mins
        sec3 = seshAvg[2]    # Calculate seconds
        hours3 = seshAvg[0]     # Calculate hours
        print("Session average = {0}:{1}:{2}".format(hours3, mins3, sec3))
        if (len(all_times) > 4):
            runnAvg = calc_run_avg(all_times)
            mins4 = runnAvg[1]
            sec4 = runnAvg[2]
            hours4 = runnAvg[0]
            print("Current avg of 5 = {0}:{1}:{2}".format(hours4, mins4, sec4)) 

    run = input()
    if (len(run) > 0):
        return

    start = time.time()
    dots_num = rnd.randrange(0, 60) % 3 
    wait = input("Timing" + dots[dots_num])
    end = time.time() 

    # Increment running sum
    num_solved += 1
    
    all_times.append((end - start))

    # Runs calculations and prints results. 
    time_math(start, end)
    print("Press SPACE then ENTER to go again, " +
             "or any other key then ENTER to exit")
    cmd = input()
    if (cmd == ' ' or cmd == 'q'):
        main(all_times, num_solved)


    thanks = "Thanks for solving!"

    print(thanks)



main([], num_solves)
