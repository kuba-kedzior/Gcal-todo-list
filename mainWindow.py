import PySimpleGUI as sg
import numpy as np
class mainWindow():

    # __init__ is known as the constructor
    def __init__(self, task_array):
        layout = [[sg.Table(task_array.tolist(), headings=["class/org", "name", "link","priority","%done","start","end","time given","time left"], enable_click_events = True, key = "Table")],
              [sg.Button("Add", key = "Add")]]
        self.window= sg.Window('Tasks', layout)
        self.task_array = task_array

    """_summary_
        Handles all events made by the window, might return a new window,"Done, if window was closed, False otherwise
    """
    def handle_events(self):
        event, values = self.window.read()
        if event == sg.WINDOW_CLOSED:
            self.window.close()
            np.save('tasks', self.task_array)
            return "Done"
        elif event =='Table':
            item = values[event]
            print(item)
        elif event == 'Add':
            return "Added"
        return False
    
    def add_data(self, new_data):
        try:
            if not self.task_array.size > 0:
                self.task_array = np.array(new_data,ndmin = 2)
            else:
                self.task_array = np.append(self.task_array, new_data, axis = 0)
        except Exception as e:
            print("unable to make new task: ", e)
        np.save('tasks', self.task_array)

    def update_tasks():
        self.window['Table'].update(values=self.task_array.tolist())