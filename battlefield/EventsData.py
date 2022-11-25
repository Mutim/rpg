import player_info
"""
Objects that will hold all information about the random events.

indexing stars at 0, and moves forward from there when adding new events.
Event Text shows whenever the event is triggered, 0 and 1 text is called whenever the option is selected.
in the event object, 0 is the bad outcome, and 1 is the good outcome.

Within the events, the first key is always the name of the event.

"""
data = {
    0: {
        "name": " - Strange Chest of Thieves",
        "text": "You've come across a strange chest. There is an ornate skull, decorated with diamonds around the crest. The chest seems to be a war chest of some sort. Perhaps an unlucky thief left it here for a later retrieval?   This could be a trap.",
        0: {
            "name": " - You've Triggered a Trap!",
            "text": "The chest was trapped! You suffer a minor leg injury from the trap piercing your thigh. It would appear that things aren't always as they seem.",
            "action": "health",  # Player attribute affected
            "amount": -2
        },
        1: {
            "name": " - All That Glitters is Gold",
            "text": "What a find! You"
        }
    },
    1: {
        "name": " - Second Name",
        "text": "This is the second event text. Need more events.",
        0: {
            "name": "Bad"
        },
        1: {
            "name": "Good"
        }
    },
}
