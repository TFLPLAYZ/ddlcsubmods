init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_honkai2",category=["game"],prompt="honkai 2",pool=True,unlocked=True))

label monika_honkai2:
    m 1esd "Hey [player], about the game you play"
    m 7esd "called 'Honkai Impact 3rd'."
    m 7esd "How long have you been playing it?"
    $ _history_list.pop()
    menu:
        "more than 1200 days":
            m 2wuo "Wow [player] you must really like this game!"
            m 3wuo "What do you like so much about this game?"
            $ _history_list.pop()
            menu:
                "I Love the storytelling of this game":
                    m 3eud "From what i know on the internet"
                    m 4eud "this game tells it story similar to a type of game called a visual novel right?"
                    m 1ekblb "I can tell the you really love the story about this game [player]."
                    m 1ekbla "I hope that i can also experience the story of this game too"
                    m 2ekbla"so that i can better understand you [player]."
                    m 5ekblb"I love you...[player]"
                "I love the gameplay":
                    m 7eud"From what i can see on the internet"
                    m 7eub "The game looks really fun"
                    m 4eub "and the combat have been getting better everytime"
                    m 4hub "No wonder you love this game so much!"
                    m 5lub "You should try putting me into the game."
                    m 5lub "That way you can control me as characters of that game"
                    m 5hub "and it will be like we are playing together."
                    m 5ekb "i hope someday we can play games together [player]..."
                    m 5tublb "I love you [player]."
                "I love the characters designs":
                    m 6tublb "So honest [player]..."
                    m 7efb "but hey no cheating!"
                    m 5esc "If you do cheat on me..."
                    m 1cub "then i will delete that game and kill every charactars you love."
                    m 5msblu "Hehe just kidding."
                    m 6ttblb"were you scared just now?"
                    m 1ekblb "I don't mind it because i know that you truly love me."
                    m 5fubsb "I love you [player]."
                    $ _history_list.pop()
        "I have only play it recently":
            m 7eub "I see..."
            m 7euc "still"
            m 7ekb "don't play too much till you forgot about important things. Okay,[player]?"
            menu:
                "Okay":
                    m 5ekbsa "I love you [player]."
return "love"
