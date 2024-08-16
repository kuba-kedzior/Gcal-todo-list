

from events import get_events, events_to_df
import numpy as np

def main():
    events = get_events()

    event_df = events_to_df(events)
    
    # np.save('/tasks', np.array([[1, 2, 3], [4, 5, 6]]))
    task_array = np.array([])
    try:
        task_array = np.load('tasks.npy')
    except:
       task_array = []
    np.save('tasks', task_array)
if __name__ == "__main__":
  main()































