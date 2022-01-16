# timer template 
# dev : Captain_Etrigan
# The package you need for the timer, it wont bother any other packages dont worry
# this code have a tempo code for testing if you want, its a meme, if you know it, you know it
import time

# Whatever code you want just like a normal code but no timers
print("Looking for problems...")


def Timer(t):
    # This is just a timer for the time, i put it in a def for better configuration
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    # --end of the timer code timer
    # Write whatever code you want down here :    (most of your code will be here probably)

    print('Unable to fix the issue')

t = 20
Timer(int(t))
