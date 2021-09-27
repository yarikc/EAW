import random
import pyqrcode
import sys

quotes = [
    "“If everyone is moving forward together, then success takes care of itself.” – Henry Ford",
    "“The ratio of we’s to I’s is the best indicator of the development of a team.” – Lewis B. Ergen",
    "“If I have seen further, it is by standing on the shoulders of giants.” – Isaac Newton",
    "“No one can whistle a symphony. It takes a whole orchestra to play it.” – H.E. Luccock",
    "“Coming together is a beginning, staying together is progress, and working together is a success.” – Henry Ford",
    "“It takes two flints to make a fire.” – Louisa May Alcott",
    "“Great things in business are never done by one person; they’re done by a team of people.” – Steve Jobs",
    "“The way a team plays as a whole determines its success. You may have the greatest bunch of individual stars in the world, \
      but if they don’t play together, the club won’t be worth a dime.” – Babe Ruth",
    "“A group is a bunch of people in an elevator. A team is a bunch of people in an elevator, but the elevator is broken.” – Bonnie Edelstein",
    "“There is immense power when a group of people with similar interests gets together to work toward the same goals.” – Idowu Koyenikan",
    "“Politeness is the poison of collaboration.” – Edwin Land",
    "“Cooperation is the thorough conviction that nobody can get there unless everybody gets there.” – Virginia Burden",
    "“If you want to go fast, go alone. If you want to go far, go together.” – African Proverb",
    "“Success is best when it’s shared.” – Howard Schultz",
    "“It is amazing what you can accomplish if you do not care who gets the credit.” – Harry Truman",
    "“Teamwork is the lynchpin in our long term success.” – Ned Lautenbach",
    "“Team spirit is knowing and living the belief that what a group of people can accomplish together is much larger, \
      far greater, and will exceed that which an individual can accomplish alone.” – Diane Arias",
    "“Only by binding together as a single force will we remain strong and unconquerable” – Chris Bradford"
]   

def get_quote():
    print(random.choice(quotes))

if __name__ == "__main__":
    person = input("Enter your name: ")
    print(f"Hi {person}! Your team quote of teh day is: \n")
    get_quote()
    url = pyqrcode.create("tinyurl.com/59ru32md", error='L', version=2)
    print(url.terminal(quiet_zone=0))
