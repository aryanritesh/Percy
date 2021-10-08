import  random
greeting= ["hii", "hello", "hey", "yo"]
replyGreet=['heyya','hello', 'hey', 'yo', 'hiiii']
condition=["how are you", "how are you doing"]
replyCond=["I am fine, how are you?", "up and running, how about you?","young,wild and free, and you?"]
thanks=("okay","alright","thank you","thanks")
replyThanks=('you are welcome','glad to help','happy to help')
capabilities=("what all can you do","what are your functions","what can you do","what all can you perform")
replyCap= ('I can help you with a variety of things, try tell me the news', 'I can help you with a variety of things, try tell me the weather','I can help you with a variety of things, search for elon musk on wikipedia')
WhoAreYou=("who are you","what are you")
replyWay=('I am percy, a personal assistant to aryan', 'I am percy, a personal assistant')
ssup=("what is up","ssup","what you doing")
replySsup=('just chillin, you?','surfing the net for cute puppy videos, you?','nothing much, you?')
whoAmI=("who am I")
replyWIA=('You are Aryan')
Bday=("when is my birthday", "When was I born")
replyBday=('11th december','11th december, 2001')
bday=("when is your birthday", "when were you born")
replybday=('2nd October')
apology=('I am sorry I do not know the answer to that','I am sorry, I do not know this one','I am afraid I cannot assist you with that')


def talk(Text):
    Text=str(Text)
    for word in Text.split():
        word = Text
        if word in greeting:
            reply=random.choice(replyGreet)
            return reply
        elif word in condition:
            reply1=random.choice(replyCond)
            return reply1
        elif word in thanks:
            reply2=random.choice(replyThanks)
            return reply2
        elif word in capabilities:
            reply3=random.choice(replyCap)
            return reply3
        elif word in WhoAreYou:
            reply4=random.choice(replyWay)
            return reply4
        elif word in ssup:
            reply5=random.choice(replySsup)
            return reply5
        elif word in whoAmI:
            reply6=replyWIA
            return reply6
        elif word in Bday:
            reply7=random.choice(replyBday)
            return reply7
        elif word in bday:
            reply8=replybday
            return reply8
        else:
            return random.choice(apology)