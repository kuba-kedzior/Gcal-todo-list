

from events import get_events, events_to_df


def main():
    events = get_events()

    event_df = events_to_df(events)
    

if __name__ == "__main__":
  main()































