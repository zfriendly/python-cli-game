from peewee import *

db = PostgresqlDatabase('trivia', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Trivia(BaseModel):
    question = CharField()
    option_1 = CharField()
    option_2 = CharField()
    option_3 = CharField()
    answer = IntegerField()
    category = CharField()
    correct_count = IntegerField()


db.connect()
db.drop_tables([Trivia])
db.create_tables([Trivia])


trivia_data = [
    {
        "question": "Which team became the Washington Nationals?",
        "option_2": "1) Montreal Expos",
        "option_2__1": "2) Minnesota Twins",
        "option_3": "3) Milwaukee Braves",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who was the first player to throw a pitch as a National?",
        "option_2": "1) Mike Stanton",
        "option_2__1": "2) Max Scherzer",
        "option_3": "3) Livan Hernandez",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which Nationals starter was NOT a first-round Draft choice?",
        "option_2": "1) Gio Gonzalez",
        "option_2__1": "2) Stephen Strasburg",
        "option_3": "3) Jordan Zimmermann",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who was the youngest player to win the NL Most Valuable Player award?",
        "option_2": "1) Juan Soto",
        "option_2__1": "2) Bryce Harper",
        "option_3": "3) Trea Turner",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which team did the Nationals NOT face in the 2019 playoffs?",
        "option_2": "1) Los Angeles Dodgers",
        "option_2__1": "2) Atlanta Braves",
        "option_3": "3) Houston Astros",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which pitcher threw two no-hitters in 2015?",
        "option_2": "1) Max Scherzer",
        "option_2__1": "2) Gio Gonzalez",
        "option_3": "3) Stephen Strasburg",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "What year did the Nationals win their first division title?",
        "option_2": "1) 2011",
        "option_2__1": "2) 2008",
        "option_3": "3) 2012",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who pitched the first no-hitter in Washington Nationals history?",
        "option_2": "1) Patrick Corbin",
        "option_2__1": "2) Livan Hernandez",
        "option_3": "3) Jordan Zimmermann",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who was the Nationals' very first draft pick?",
        "option_2": "1) Stephen Strasburg",
        "option_2__1": "2) Ryan Zimmerman",
        "option_3": "3) Terrmel Sledge",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "How many batters did Stephen Strasburg strike out in his major league debut?",
        "option_2": "1) 14",
        "option_2__1": "2) 17",
        "option_3": "3) 9",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who threw the ceremonial first pitch at the grand opening of Nationals Park?",
        "option_2": "1) Barack Obama",
        "option_2__1": "2) Jose Andres",
        "option_3": "3) George W. Bush",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "In what neighborhood is Nationals Park located?",
        "option_2": "1) Waterfront",
        "option_2__1": "2) Navy Yard",
        "option_3": "3) Bloomingdale",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who was the World Series MVP in 2019?",
        "option_2": "1) Stephen Strasburg",
        "option_2__1": "2) Anthony Rendon",
        "option_3": "3) Gerrit Cole",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which Nationals' pitcher has the most wins in a season?",
        "option_2": "1) Max Scherzer",
        "option_2__1": "2) Jordan Zimmermann",
        "option_3": "3) Gio Gonzalez",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "What season was the Capitals' first in the NHL?",
        "option_2": "1) 1972-73",
        "option_2__1": "2) 1980-81",
        "option_3": "3) 1974-75",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who is the Capitals' all-time leader in Goals?",
        "option_2": "1) Alex Ovechkin",
        "option_2__1": "2) Peter Bondra",
        "option_3": "3) Olaf Kolzig",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "How many Super Bowls have the Washington Redskins won?",
        "option_2": "1) Five",
        "option_2__1": "2) Two",
        "option_3": "3) Three",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who is the Redskins all-time leading rusher?",
        "option_2": "1) Clinton Portis",
        "option_2__1": "2) John Riggins",
        "option_3": "3) Stephen Davis",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which Redskins' great passed away tragically in 2007?",
        "option_2": "1) Sean Taylor",
        "option_2__1": "2) Kirk Cousins",
        "option_3": "3) Joe Gibbs",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Who did the Capitals beat in the Stanley Cups Finals in 2017-18?",
        "option_2": "1) Las Vegas Golden Knights",
        "option_2__1": "2) St. Louis Blues",
        "option_3": "3) Pittsburgh Penguins",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "What was the Washington Wizards' previous name?",
        "option_2": "1) Warthogs",
        "option_2__1": "2) Bullets",
        "option_3": "3) Kings",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which NBA Hall-of-Famer ended his career with the Wizards?",
        "option_2": "1) Karl Malone",
        "option_2__1": "2) Vince Carter",
        "option_3": "3) Michael Jordan",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which current Wizards player was drafted #1 overall in 2010?",
        "option_2": "1) Bradley Beal",
        "option_2__1": "2) John Wall",
        "option_3": "3) Thomas Bryant",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "In which league does D.C. United play?",
        "option_2": "1) NFL",
        "option_2__1": "2) MLS",
        "option_3": "3) NBA",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "The Capital City Go-Go are an affiliate of which D.C. sports team?",
        "option_2": "1) Wizards",
        "option_2__1": "2) Capitals",
        "option_3": "3) Nationals",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Ted Leonsis owns two D.C. sports franchises. Which two does he own?",
        "option_2": "1) Wizards & Redskins",
        "option_2__1": "2) Redskins & Nationals",
        "option_3": "3) Capitals and Wizards",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Which former Redskins QB was the first black QB to win a Super Bowl?",
        "option_2": "1) Donovan McNabb",
        "option_2__1": "2) Doug Williams",
        "option_3": "3) Robert Griffin III",
        "answer": 2,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Three of the four major franchises in D.C. use the same color scheme (Red, White and Blue). Which team does not?",
        "option_2": "1) Redskins",
        "option_2__1": "2) Wizards",
        "option_3": "3) Nationals",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "What was the name of the Washington baseball franchise before the Nationals?",
        "option_2": "1) Filibusters",
        "option_2__1": "2) Congressmen",
        "option_3": "3) Senators",
        "answer": 3,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "Ranking second all time in NHL history, how many 40-goal seasons does Alex Ovechkin have?",
        "option_2": "1) 11",
        "option_2__1": "2) 8",
        "option_3": "13) 12",
        "answer": 1,
        "category": "sports",
        "correct_count": 0
    },
    {
        "question": "What is the population of Washington, DC as of 2019?",
        "option_2": "1) 633,427",
        "option_2__1": "2) 711,571",
        "option_3": "3) 800, 331",
        "answer": 2,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "How many senators does Washington, DC.have?",
        "option_2": "1) One",
        "option_2__1": "2) Two",
        "option_3": "3) Zero",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "What two states border Washington, DC?",
        "option_2": "1) VA & DE",
        "option_2__1": "2) MD & WV",
        "option_3": "3) VA & MD",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "What is the street address of the White House?",
        "option_2": "1) 1600 Pennsylvania Ave.",
        "option_2__1": "2) 123 Capital St.",
        "option_3": "3) 1000 North Capital St.",
        "answer": 1,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "In which war were the Capital, Treasure, and White House burned down?",
        "option_2": "1) Civil War",
        "option_2__1": "2) War of 1812",
        "option_3": "3) World War I",
        "answer": 2,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "Which educational foundation maintains most museums in DC and keeps them free?",
        "option_2": "1) Peabody",
        "option_2__1": "2) Macarthur",
        "option_3": "3) Smithsonian",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "The ______ Center for Performing Arts is named after which former President?",
        "option_2": "1) Kennedy",
        "option_2__1": "2) Adams",
        "option_3": "3) Eisenhower",
        "answer": 1,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "Which university in Washington shares a name with the neighborhood in which it is located?",
        "option_2": "1) Howard University",
        "option_2__1": "2) Gallaudet University",
        "option_3": "3) Georgetown University",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "The National ___ houses many of DC's museums and institutions.",
        "option_2": "1) Park",
        "option_2__1": "2) Mall",
        "option_3": "3) Monument",
        "answer": 2,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "How tall is the Washington Monument?",
        "option_2": "1) 800 ft.",
        "option_2__1": "2) 555 ft.",
        "option_3": "3) 586 ft.",
        "answer": 2,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "Who was the first president to live in the White House?",
        "option_2": "1) John Adams",
        "option_2__1": "2) George Washington",
        "option_3": "3) John F. Kennedy",
        "answer": 1,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "The streets in D.C. that run diagonally are named after ____.",
        "option_2": "1) Numbers",
        "option_2__1": "2) Words",
        "option_3": "3) States",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "Which genre of music (combining hip-hop and live band music) originated in DC?",
        "option_2": "1) Slam Poetry",
        "option_2__1": "2) Go-Go",
        "option_3": "3) Emo",
        "answer": 2,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "Which \"letter\" street is missing in Washington, DC?",
        "option_2": "1) K",
        "option_2__1": "2) M",
        "option_3": "3) J",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "Which famous sci-fi movie character is featured as a gargoyle on the National Cathedral?",
        "option_2": "1) Capt. Picard",
        "option_2__1": "2) Darth Vader",
        "option_3": "3) Frodo Baggins",
        "answer": 2,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "What institution in the DC area has 17 miles of corridors?",
        "option_2": "1) Capital Building",
        "option_2__1": "2) National Archives",
        "option_3": "3) Pentagon",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "What DC institution houses the United States Constitution & Declaration of Independence?",
        "option_2": "1) National Archives",
        "option_2__1": "2) Library of Congress",
        "option_3": "1) White House",
        "answer": 1,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "How many bathrooms are in the White House?",
        "option_2": "1) 35",
        "option_2__1": "2) 10",
        "option_3": "3) 55",
        "answer": 1,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "The Reflecting Pool sits between the Washington Monument and The ____.",
        "option_2": "1) White House",
        "option_2__1": "2) Vietnam Memorial",
        "option_3": "3) Lincoln Memorial",
        "answer": 3,
        "category": "general",
        "correct_count": 0
    },
    {
        "question": "Which neighborhood, dating back to 1751, is the oldest part of the city?",
        "option_2": "1) Adams Morgan",
        "option_2__1": "2) Georgetown",
        "option_3": "3) Foggy Bottom",
        "answer": 2,
        "category": "general",
        "correct_count": 0
    }
]


for triv in trivia_data:
    triv = Trivia(question=triv['question'], option_1=triv['option_1'], option_2=triv['option_2'],
                  option_3=triv['option_3'], answer=triv['answer'], category=triv['category'], correct_count=0)
    triv.save()
