init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_like",category=["you"],prompt="like",pool=True,unlocked=True))

label monika_like:
    m 1esd "[player],Do you like me?"
    $ _history_list.pop()
    menu:
        "Yes":
            m 7tuu "Of course you do."
            m 1fub "I Love You Too"
            m 1hub "I hope this moment will last forever"
        "No":
            m 7tuu "You can't deceive me love."
            m 1fub "I love you too."
            m 1hub "I hope this moment will last forever"
return
