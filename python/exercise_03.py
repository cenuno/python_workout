"""
Author:         Cristian Nuno
Date:           September 11, 2020
Exercise 03:    Run Timing
"""


def run_timing():
    """
    Display average run time (minutes) & number of runs given by the user
    """
    user_output_text = "Enter 10 km run time: "
    n_runs = 0
    log_run_times = 0

    while run_time := input(user_output_text):
        if not run_time:
            break
        else:
            try:
                n_runs += 1
                log_run_times += float(run_time)
            except ValuerError:
                print("Error: run time not recorded. Please supply a number.")
                n_runs -= 1

    avg_run_time = log_run_times / n_runs
    print(f"Average time of {avg_run_time:.2f} minutes from {n_runs} runs!")


# call function
run_timing()
