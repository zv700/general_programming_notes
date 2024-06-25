from sample_madlibs import xmas, food, pool # import each variable containing a madlib from folder: sample_madlibs



if __name__ == "__main__":
    m = [xmas, food, pool]    # runs through each madlib in the list in order
    m.madlib()      # applies the m variable to madlib() from the imported madlib files in the list before printing variable: madlib ---> each madlib file within sample_madlibs ends with madlib 

