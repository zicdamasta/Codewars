# ------------------------------------------------------
# Your task in order to complete this Kata is to write a function which formats a duration, 
# given as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now". 
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#
# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
#
# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. 
# In general, a positive integer and one of the valid units of time, separated by a space. 
# The unit of time is used in plural if the integer is greater than 1.
#
# The components are separated by a comma and a space (", "). 
# Except the last component, which is separated by " and ", just like it would be written in English.
#
# A more significant units of time will occur before than a least significant one. 
# Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
#
# Different components have different unit of times. 
# So there is not repeated units like in 5 seconds and 1 second.
#
# A component will not appear at all if its value happens to be zero. 
# Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
#
# A unit of time must be used "as much as possible". 
# It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, 
# the duration specified by of a component must not be greater than any valid more significant unit of time.
# ------------------------------------------------------

def format_duration(seconds):
    if not seconds:
        return "now"
    years = seconds // 31536000 
    days = (seconds % 31536000) // 86400
    hours = ((seconds % 31536000) % 86400) // 3600
    minutes = (((seconds % 31536000) % 86400) % 3600) // 60
    seconds = ((((seconds % 31536000) % 86400) % 3600) % 60)
    
    times = ["year", "day", "hour", "minute", "second"]
    t_vars = [str(e) for e in [years, days, hours, minutes, seconds]]
    times = [times[i] if int(t) == 1 else times[i] + "s" for i, t in enumerate(t_vars)]
    delims = [""," and",",",",",","][:5-t_vars.count("0")]
    return " ".join([f"{t[0]} {t[1]}{delims.pop()}" for t in zip(t_vars, times) if int(t[0]) > 0])
    
if __name__ == '__main__':
    print(format_duration(0)) # "1 second"
    print(format_duration(62))# "1 minute and 2 seconds"
    print(format_duration(120)) # 2 minutes"
    print(format_duration(3600)) # 1 hour"
    print(format_duration(3662)) # 1 hour, 1 minute and 2 seconds"
    print(format_duration(31556953)) # 1 hour, 1 minute and 2 seconds"
    print(format_duration(86400))
    print(format_duration(132030240))