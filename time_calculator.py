def add_time(start_time, duration, weekday=None):
    final_time = []
    time_swap = 0
    dow = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    try:
        start_day = weekday.lower()
    except:
        None

    find_tod = start_time.split()
    try:
        tod = find_tod[1]
    except:
        print("Error. Please specify AM or PM.")
        exit()

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

    if 0 <= minute < 60:
        None
    else:
        print("Error. Invalid starting minute.")
        exit()

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

    if 0 <= minute2 < 60:
        add_minutes = minute2
    else:
        print("Error. Invalid duration minute.")
        exit()

    m3 = minute + minute2

    zero = "0"
    mdif = m3 - 60

    if 60 < m3 <= 69:
        final_minute = zero + str(mdif)
        hmin = 1
    elif m3 >= 70:
        final_minute = str(mdif)
        hmin = 1
    elif m3 == 60:
        final_minute = zero * 2
        hmin = 1
    else:
        final_minute = m3
        hmin = 0
    hz = hour2 + hmin
    h3 = hour + hz

    if 1 <= h3 < 12:
        final_hour = str(h3)
    elif h3 > 12:
        final_hour = h3 % 12
        if final_hour == 0:
            final_hour = 12
        else:
            None
        half_days = hz / 12
        if half_days % 2 == 0:
            None
        else:
            if tod == "AM":
                tod = "PM"
            else:
                tod = "AM"
                time_swap = 1
    else:
        final_hour = 12

        if tod == "AM":
            tod = "PM"
        else:
            tod = "AM"
            time_swap = 1
    final_time.append(str(final_hour))
    final_time.append(str(final_minute))

    new_time1 = ":".join(final_time)

    z = 0

    while hz > 24:
        hz = hz - 24
        z += 1

    days = z + time_swap

    if days == 1:
        days_later = "(next day)"
    elif days > 1:
        days_later = "(" + str(days) + " days later)"
    else:
        days_later = None

    new_time2 = new_time1 + " " + tod

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

    if days_later is not None:
        new_time = new_time3 + " " + days_later
    else:
        new_time = new_time3

    return new_time

