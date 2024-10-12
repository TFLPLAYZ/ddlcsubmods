init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_honkai",category=["game"],prompt="honkai",pool=True,unlocked=True))

label monika_honkai:
    m 1esd "Hey [player], i've been noticing"
    m 1esd "that you play a certain game called"
    m 1esd "Honkai Impact 3rd everyday."
    m 1esd "From what i read on the internet"
    m 3esd "this game is a type of live service game"
    m 4esd "called a gacha games. These gacha games usually involve gambling..."
    m 2ekd "[player],Do you spend money on these type of games?"
    $ _history_list.pop()
    menu:
        "No":
            m 1hsblb "Thank goodness"
            m 3ekd "I'm just worried that you will get gambling addiction "
            m 1ekc "from these types of games."
            m 3eku "I hope you understand"
            m 4ekb "I don't mind you spending money on theese types of games"
            m 14eka "but i hope you dont waste too much money until you have to starve yourself"
            m 4ekbsa "Your well being is my no.1 concern"
            m 1eka "I hope you understand. [player]."
            m 2ekblb "I love you...[player]"
        "Yes":
            m 1etc "[player], oh i see."
            m 7etd "How much do you spend on these types of games?"
            $ _history_list.pop()
            menu:
                "Not more than $20-$30":
                    m 2esb "I see."
                    m 2esb "Then i won't mind you spend it as a little reward for yourself."
                    m 3esb "In my opinion, this is a good range for spending money on games."
                    m 4esc "Sometimes it's just not worth to spend on game that cost more than $30"
                    m 5eka"I hope you understand [player]."
                "Below $100":
                    m 3essdrb "[player], i hope you can reduce your spendings."
                    m 7eka "If you really want to spend money on games"
                    m 7ekb "you should spend it on a non live service game..."
                    m 1eka "I hope you understand. [player]."
                    m 2ekblb "I love you...[player]"
                "Over $100":
                    m 2essdld "[player], can you reduce your spendings?"
                    m 3eksdld "Spending too much money on a game is not worth it!"
                    m 3eksdlo "Especially on these type of games..."
                    m 4eksdlc "Do you understand me? [player]"
                    m 7eksdld "Promise me you won't spend this much money on games anymore."
                    $ _history_list.pop()
                    menu:
                        "I promise":
                            m 2ekb "Thank you for understanding [player]."
                            m 5ekbsa "I love you [player]."
                        "I'll try not to spend too much":
                            m 2ekb "Thank you for understanding [player]."
                            m 5ekbsa "I love you [player]."
        "Only on this game":
            m 72esb "I see..."
            m 7eksdla "still"
            m 7eksdlb "I hope you don't spend too much [player]."
            m 2esblb "Other than that im fine if you want to spend on games."
            m 5ekbsa "I love you [player]."
return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_honkai3",category=["game"],prompt="honkai 3",pool=True,unlocked=True))

label monika_honkai3:
    m 1esd "Hey [player], about the game you play"
    m 7esd "called 'Honkai Impact 3rd'."
    m 7esd "Does the game collab with other animes/games?"
    $ _history_list.pop()
    menu:
        "Yes, it does.":
            m 2wuo "Wow that is amazing"
            m 3wuo "How many games or aniime has it collaborated with so far?"
            $ _history_list.pop()
            menu:
                "Just only one anime called Evangelion":
                    m 7eub "Oh i've heard of this anime before!"
                    m 7eub "from natsuki"
                    m 7eub "she said that the anime is about"
                    m 1eub "a bunch of school student piloting robots"
                    m 1eub "and protect humanity from these so called monster called angels."
                    m 7eusdlb "It's kinda weird calling an angel a monster don't you think?"
                    m 4ssb "Imagine how cool it will be if both us fight together"
                    m 4ssb "to protect humanity and be known as the ultimate couple."
                    m 2fubsb "It will kinda cool don't you think [player]?"
                "Just only one game genshin impact":
                    m 7eub "Oh i've heard of this anime before!"
                    m 7eub "I have seen people play the before game"
                    m 7hub "it looks super fun!"
                    m 4hub "From what i know this game is also made by the same company"
                    m 7kub "that made your favourite game right [player]?"
                    m 7mublb "I also heard that its a good game for couples"
                    m 1fkblb "I can't wait to cross to reality and play it with you [player]"
                    m 7esblb "Or maybe you can code me into the game and we can play together."
                    m 1ekbla "I hope that these may come true someday..."
                "So far it has 2 anime collabs and 2 game collabs":
                    m 1wsb "Wow that's amazing [player]."
                    m 7esd "From what i know it's usually hard to do any kind of collabs"
                    m 7esd "with different franchises"
                    m 7esd "because of the copyright law and require so many plannings to be done."
                    m 7gsd "And don't get me started how they're going to make"
                    m 7gsd "sense to the lore of those games."
                    m 7esb "Still It's amazinng that they managed to do it."
                    m 5esb "They have my respect for it."
        "No, it doesn't do collabs":
            m 7eub "I see..."
            m 7euc "well that's kinda dissappointing."
            m 7ekb "Thank you for answering [player]?"
return
