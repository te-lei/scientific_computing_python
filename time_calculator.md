# Time Calculator

#### This is my submission for the Time Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator


### Code begins:

#### Define function, set required arguments of start_time and duration with an optional argument of weekday (automatically set to None).

#### Create a list for the final time to be computed. Set 'time_swap' variable (to determine if a change from PM to AM was recognized) default to 0. Populate day of week list with days of the week.
    def add_time(start_time, duration, weekday=None):
    
        final_time = []
        time_swap = 0
        dow = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#### Standardize weekday entry by making it lower case (if it was provided).

        try:
            start_day = weekday.lower()
        except:
            None

#### Determine the time of day ("AM" or "PM") and create a requirement for it to be included in the input. Present an error and exit the code if time of day is not present.

        find_tod = start_time.split()
        
        try:
            tod = find_tod[1]
        except:
            print("Error. Please specify AM or PM.")
            exit()

#### Parse start_time to find hour values. Present errors for values that are not whole numbers and exit the code.

        emit = find_tod[0]

        fun = emit.split(":")

        h = fun[0]

        try:
            hour = int(h)
        except:
            print("Error. Invalid starting hour.")
            exit()
        if 0 < hour <= 12:
            None
        else:
            print("Error. Invalid starting hour.")
            exit()

#### Parse start_time to find minute values. Present errors for values that exceed two digits and values that are not whole numbers and exit the code.

        m = fun[1]

        m_length = len(m)

        if 1 <= m_length <= 2:
            None
        else:
            print("Error. Invalid starting minute.")
            exit()

        try:
            minute = int(m)
        except:
            print("Error. Invalid starting minute.")
            exit()

#### If the start_time minute value exceeds 59, present an error and exit the code.

        if 0 <= minute < 60:
            None
        else:
            print("Error. Invalid starting minute.")
            exit()

#### Parse duration to find hour values. Present errors for values that are not whole numbers and exit the code.

        duration_time = duration.split(":")

        h2 = duration_time[0]

        try:
            hour2 = int(h2)
        except:
            print("Error. Invalid duration hour.")
            exit()

        if 0 <= hour2:
            add_hours = hour2
        else:
            print("Error. Invalid duration hour.")
            exit()
#### Parse duration to find minute values. Present errors for values that exceed two digits and values that are not whole numbers and exit the code.

        m2 = duration_time[1]

        m_length2 = len(m2)

        if 1 <= m_length2 <= 2:
            None
        else:
            print("Error. Invalid duration minute.")
            exit()

        try:
            minute2 = int(m2)
        except:
            print("Error. Invalid duration minute.")
            exit()
#### If the duration minute value exceeds 59, present an error and exit the code.

        if 0 <= minute2 < 60:
            add_minutes = minute2
        else:
            print("Error. Invalid duration minute.")
            exit()

#### Define m3 value as a sum of the start_time and duration minute values. Create mdif to calculate final minute - 60.

        m3 = minute + minute2

        zero = "0"
        mdif = m3 - 60
        
#### If m3 is between 61 and 69, the final minute equals "0" before mdif (the minute value minus 60) and note that an hour has been added by setting hmin = 1.

        if 60 < m3 <= 69:
            final_minute = zero + str(mdif)
            hmin = 1
#### Otherwise, if m3 equals or exceeds 70, the final minute equals mdif (the minute value minus 60) and note that an hour has been added by setting hmin = 1.

        elif m3 >= 70:
            final_minute = str(mdif)
            hmin = 1
#### Otherwise, if m3 equals 60, the final minute value equals "00" and not that an hour has been added by setting hmin = 1. If m3 is less than 60, the final minute = m3.

        elif m3 == 60:
            final_minute = zero * 2
            hmin = 1
        else:
            final_minute = m3
            hmin = 0
#### Define hz as the sum of the duration hour and hmin (any additional hour from adding the minutes).

#### Define h3 as the sum of the start_time hour and hz.
        
        hz = hour2 + hmin
        h3 = hour + hz
#### If h3 is between 1 and 11, the final hour equals h3.

        if 1 <= h3 < 12:
            final_hour = str(h3)
#### Otherwise if h3 is greater than 12, the final hour equals the remainder of h3 divided by 12 (to provide a number from 1 to 11). If there is no remainder, the final hour = 12.

        elif h3 > 12:
            final_hour = h3 % 12
            if final_hour == 0:
                final_hour = 12
            else:
                None
#### Define half days as hz (hours to be added) divided by 12. If the number is even, an even amount of 12 hour periods have elapsed, meaning the time of day remains the same. If it is odd, an odd amount of 12 hour periods have elapsed, meaning the time of day switches. If there is a switch from "PM" to "AM" set the time_swap = 1.
            
            half_days = hz / 12
            if half_days % 2 == 0:
                None
            else:
                if tod == "AM":
                    tod = "PM"
                else:
                    tod = "AM"
                    time_swap = 1
##### Otherwise, the final hour equals 12 and the time of day switches, so time_swap = 1.
        else:
            final_hour = 12

            if tod == "AM":
                tod = "PM"
            else:
                tod = "AM"
                time_swap = 1
#### Populate the final_time list with the final hour and minute values.

        final_time.append(str(final_hour))
        final_time.append(str(final_minute))
#### Set the variable new_time1 to combine the values with a ":" in between.

        new_time1 = ":".join(final_time)

#### Set a value z = 0. If hz is greater than 24, while that's the case, subtract 24 from it until it's below 24, adding 1 to z each time to denote that a day is being added. The number of days = z + time_swap. 
*(ex. We can be adding 3 hours from 11:00 PM to 2:00 AM, but a day is being added, so z = 0 as it will not run the while loop and time_swap = 1, meaning days = 1)*
        
        z = 0

        while hz > 24:
            hz = hz - 24
            z += 1

        days = z + time_swap

#### If days = 1 set the days_later to "(next day)", if it exeeds 1, set the days_later to "(x days later)", otherwise do nothing because days = 0.

        if days == 1:
            days_later = "(next day)"
        elif days > 1:
            days_later = "(" + str(days) + " days later)"
        else:
            days_later = None
#### Set new_time2 to include the new time and the time of day.

        new_time2 = new_time1 + " " + tod
#### If a weekday value is provided, calculate the weekday and set new_time3 to include the new_time2 and the weekday. Otherwise, set new_time3 = new_time2.

        if weekday is not None:
            x = dow.index(start_day) + 1

            y = x + days

            if y > 7:
                while y > 7:
                    y = y - 7

                end_day = dow[y - 1]
            else:
                end_day = dow[y - 1]

            final_day = end_day.capitalize()
            new_time3 = new_time2 + ", " + final_day
        else:
            new_time3 = new_time2
#### If the days_later is not None, set new_time to equal new_time 3 and the amount of days later. Otherwise set new_time = new_time3.
        if days_later is not None:
            new_time = new_time3 + " " + days_later
        else:
            new_time = new_time3

        return new_time
