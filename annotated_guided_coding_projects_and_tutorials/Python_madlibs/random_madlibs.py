### run play.py to run through multiple madlibs
### random function currently not working

from sample_madlibs import xmas, food, pool # import each variable containing a madlib from folder: sample_madlibs
import random   # random choice module

### Original: random choice not working with current additions to madlib structure
#if __name__ == "__main__":
    #m = random.choice([xmas, food, pool])    # chooses a random madlib from the list [] to display
    #m.madlib()      # applies the m variable to madlib() from the imported madlib files in the list before printing variable: madlib ---> each madlib file within sample_madlibs ends with  

### Attempt: currently not working
#if __name__ == "__main__":
    #x = int([xmas, food, pool])
    #m = random.choice(x)  # chooses a random madlib from the list [] to display
    #m.madlib()      # applies the m variable to madlib() from the imported madlib files in the list before printing variable: madlib ---> each madlib file within sample_madlibs ends with  
