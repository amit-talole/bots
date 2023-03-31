import random
from opsdroid.matchers import match_regex
from opsdroid.skill import Skill



class MySkill(Skill):

    @match_regex(r'Bye|See you|by')
    async def bye_greet(self, message):
        text = random.choice(["Bye {}", "See you {} "]).format(message.user)
        await message.respond(text)
            
    
    @match_regex(r'Hi|hello|Hey')
    async def hi_greet(self, message):
        text = random.choice(["Hi {}", "Hello {}", "Hey {} "]).format(message.user)
        await message.respond(text)
