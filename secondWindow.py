import PySimpleGUI as sg

class secondWindow():

    # __init__ is known as the constructor
    def __init__(self):
        self.window = None
        self.isDisplayed = False

    def handle_events(self,main_window):
        event_2, values_2 = self.window.read()
        if event_2 == sg.WINDOW_CLOSED:
            self.window.close()
            self.window = None
            self.isDisplayed = False
        elif event_2 == "Submit":
            new_data = [[self.window['-IN1-'].get(),
                        self.window['-IN2-'].get(),
                        self.window['-IN3-'].get(),
                        0,0,
                        self.window['-IN4-'].get(),
                        self.window['-IN5-'].get(),
                        # datetime.strptime(second_window['-IN4-'].get(), '%Y-%m-%d %H:%M:%S'),
                        # datetime.strptime(second_window['-IN5-'].get(), '%Y-%m-%d %H:%M:%S'),
                        0,0]]
            main_window.add_data(new_data)
            self.window.close()
            self.window = None
            self.isDisplayed = False

    def start_window(self):
        layout = [[sg.Text('Class/org'), sg.Input(enable_events=True, key='-IN1-', font=('Arial Bold', 12), expand_x=True)],
                [sg.Text('name'), sg.Input(enable_events=True, key='-IN2-', font=('Arial Bold', 12), expand_x=True)],
                [sg.Text('link'), sg.Input(enable_events=True, key='-IN3-', font=('Arial Bold', 12), expand_x=True)],
                [sg.Text('Start time'), sg.Input(key='-IN4-'), sg.CalendarButton("Choose Start Date", target = "-IN4-",close_when_date_chosen = False)],
                [sg.Text('End time'), sg.Input(key='-IN5-'), sg.CalendarButton("Choose End Date", target = "-IN5-",close_when_date_chosen = False)],
                [sg.Button("Submit", key = "Submit")]]
        self.window = sg.Window('Task Adder', layout)
        self.isDisplayed = True