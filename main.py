from events import get_events, events_to_df
from datetime import datetime
import numpy as np
import PySimpleGUI as sg
from mainWindow import mainWindow
from secondWindow import secondWindow

def main():
    task_array = np.array([], ndmin = 2)

    events = get_events()

    event_df = events_to_df(events)
    
    # np.save('/tasks', np.array([[1, 2, 3], [4, 5, 6]]))
    try:
        task_array = np.load('tasks.npy')
    except Exception as e:
        print("unable to load tasks: ", e)
        task_array = np.array([],ndmin = 2)
    main_window = mainWindow(task_array)
    second_window = secondWindow()
    while True:
        result = main_window.handle_events()

        if result == "Done": 
            break
        elif result == "Added":
            second_window.start_window()
        if second_window.isDisplayed:
            second_window.handle_events(main_window)
        

if __name__ == "__main__":
  main()































