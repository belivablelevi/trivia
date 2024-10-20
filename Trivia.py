import random

questions = [
    # Pop Culture
    {
        "question": "What is the name of the fictional city where Batman resides?",
        "options": ["Metropolis", "Gotham", "Central City", "Star City"],
        "answer": "Gotham"
    },
    {
        "question": "Who played Jack Dawson in 'Titanic'?",
        "options": ["Johnny Depp", "Leonardo DiCaprio", "Brad Pitt", "Matthew McConaughey"],
        "answer": "Leonardo DiCaprio"
    },
    {
        "question": "What year did the TV show 'Friends' first premiere?",
        "options": ["1994", "1996", "2000", "2002"],
        "answer": "1994"
    },
    {
        "question": "Which artist is known for the hit song 'Thriller'?",
        "options": ["Prince", "Michael Jackson", "Madonna", "Elton John"],
        "answer": "Michael Jackson"
    },
    {
        "question": "What is the name of the fictional continent in 'Game of Thrones'?",
        "options": ["Middle-earth", "Narnia", "Westeros", "Arrakis"],
        "answer": "Westeros"
    },
    {
        "question": "Who won the first season of 'American Idol'?",
        "options": ["Kelly Clarkson", "Carrie Underwood", "Jennifer Hudson", "Fantasia Barrino"],
        "answer": "Kelly Clarkson"
    },
    {
        "question": "What is the name of the fictional school in 'Harry Potter'?",
        "options": ["Hogwarts", "Nevermore Academy", "Sunnydale High", "Ravenclaw"],
        "answer": "Hogwarts"
    },
    {
        "question": "Which artist painted the 'Mona Lisa'?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the highest-grossing film of all time?",
        "options": ["Titanic", "Avatar", "Star Wars: The Force Awakens", "Avengers: Endgame"],
        "answer": "Avatar"
    },
    {
        "question": "Who is known as the 'Queen of Pop'?",
        "options": ["Lady Gaga", "Beyoncé", "Madonna", "Ariana Grande"],
        "answer": "Madonna"
    },
    
    # Pasta
    {
        "question": "Which type of pasta is shaped like small rice grains and is often used in soups?",
        "options": ["Fusilli", "Orzo", "Penne", "Fettuccine"],
        "answer": "Orzo"
    },
    {
        "question": "What pasta is often used in lasagna?",
        "options": ["Penne", "Fusilli", "Lasagna noodles", "Spaghetti"],
        "answer": "Lasagna noodles"
    },
    {
        "question": "What type of pasta is shaped like little ears?",
        "options": ["Orecchiette", "Fusilli", "Penne", "Linguine"],
        "answer": "Orecchiette"
    },
    {
        "question": "Which sauce is traditionally served with spaghetti?",
        "options": ["Alfredo", "Marinara", "Pesto", "Bolognese"],
        "answer": "Marinara"
    },
    {
        "question": "What is the Italian term for 'pasta with cheese'?",
        "options": ["Pasta al formaggio", "Pasta con pomodoro", "Pasta al pesto", "Pasta fritta"],
        "answer": "Pasta al formaggio"
    },
    {
        "question": "What does 'al dente' mean when cooking pasta?",
        "options": ["Soft", "Firm to the bite", "Overcooked", "Saucy"],
        "answer": "Firm to the bite"
    },
    {
        "question": "What type of pasta resembles a bow tie?",
        "options": ["Fusilli", "Farfalle", "Penne", "Linguine"],
        "answer": "Farfalle"
    },
    {
        "question": "What is the name of the pasta that resembles spaghetti but is thicker?",
        "options": ["Bucatini", "Fusilli", "Ziti", "Penne"],
        "answer": "Bucatini"
    },
    {
        "question": "What type of pasta is often used in pasta salad?",
        "options": ["Fusilli", "Penne", "Orzo", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Which type of pasta is hollow and often used in baked dishes?",
        "options": ["Ziti", "Fusilli", "Spaghetti", "Tagliatelle"],
        "answer": "Ziti"
    },

    # History
    {
        "question": "Who was the first President of the United States?",
        "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
        "answer": "George Washington"
    },
    {
        "question": "Who was known as the 'Iron Lady'?",
        "options": ["Angela Merkel", "Margaret Thatcher", "Indira Gandhi", "Golda Meir"],
        "answer": "Margaret Thatcher"
    },
    {
        "question": "What year did the Berlin Wall fall?",
        "options": ["1987", "1989", "1991", "1993"],
        "answer": "1989"
    },
    {
        "question": "What ancient civilization built the pyramids?",
        "options": ["Egyptians", "Mayans", "Greeks", "Romans"],
        "answer": "Egyptians"
    },
    {
        "question": "Who was the first person to walk on the moon?",
        "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "John Glenn"],
        "answer": "Neil Armstrong"
    },
    {
        "question": "In what year was the Declaration of Independence signed?",
        "options": ["1776", "1787", "1791", "1801"],
        "answer": "1776"
    },
    {
        "question": "Who was the last ruler of the Aztec Empire?",
        "options": ["Moctezuma II", "Cortez", "Atahualpa", "Pizarro"],
        "answer": "Moctezuma II"
    },
    {
        "question": "What famous battle took place in 1066?",
        "options": ["Battle of Hastings", "Battle of Agincourt", "Battle of Waterloo", "Battle of Gettysburg"],
        "answer": "Battle of Hastings"
    },
    {
        "question": "Who was the first female Prime Minister of the UK?",
        "options": ["Margaret Thatcher", "Theresa May", "Angela Merkel", "Indira Gandhi"],
        "answer": "Margaret Thatcher"
    },
    {
        "question": "What was the name of the ship that sank in 1912?",
        "options": ["Lusitania", "Titanic", "Britannic", "Carpathia"],
        "answer": "Titanic"
    },

    # Geography
    {
        "question": "Which river is the longest in the world?",
        "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "Nile River"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Canberra", "Melbourne", "Brisbane"],
        "answer": "Canberra"
    },
    {
        "question": "Which mountain range separates Europe and Asia?",
        "options": ["Himalayas", "Rockies", "Alps", "Ural Mountains"],
        "answer": "Ural Mountains"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Gobi Desert", "Arabian Desert", "Kalahari Desert"],
        "answer": "Sahara Desert"
    },
    {
        "question": "Which country has the most natural lakes?",
        "options": ["Canada", "United States", "Russia", "Brazil"],
        "answer": "Canada"
    },
    {
        "question": "What river runs through Egypt?",
        "options": ["Nile", "Amazon", "Tigris", "Mississippi"],
        "answer": "Nile"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Nauru", "Vatican City", "San Marino"],
        "answer": "Vatican City"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Ottawa", "Vancouver", "Montreal"],
        "answer": "Ottawa"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    },

    # STEM
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Pb", "Fe"],
        "answer": "Au"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Quartz"],
        "answer": "Diamond"
    },
    {
        "question": "What is the main gas found in the Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Nitrogen"
    },
    {
        "question": "What is the chemical formula for water?",
        "options": ["H2O", "O2", "CO2", "NaCl"],
        "answer": "H2O"
    },
    {
        "question": "What is the process by which plants make their food?",
        "options": ["Photosynthesis", "Respiration", "Digestion", "Fermentation"],
        "answer": "Photosynthesis"
    },
    {
        "question": "What is the term for an organism's complete set of DNA?",
        "options": ["Chromosome", "Genome", "Allele", "Gene"],
        "answer": "Genome"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "answer": "Albert Einstein"
    },
    {
        "question": "What is the unit of electrical resistance?",
        "options": ["Volt", "Ampere", "Ohm", "Watt"],
        "answer": "Ohm"
    },
    {
        "question": "What is the study of living organisms called?",
        "options": ["Chemistry", "Physics", "Biology", "Geology"],
        "answer": "Biology"
    },
    {
        "question": "What type of bond involves the sharing of electron pairs?",
        "options": ["Ionic bond", "Covalent bond", "Hydrogen bond", "Metallic bond"],
        "answer": "Covalent bond"
    },

    # Sports
    {
        "question": "In which sport would you perform a slam dunk?",
        "options": ["Basketball", "Volleyball", "Football", "Baseball"],
        "answer": "Basketball"
    },
    {
        "question": "What sport is known as 'the king of sports'?",
        "options": ["Basketball", "Soccer", "Cricket", "Baseball"],
        "answer": "Soccer"
    },
    {
        "question": "Who holds the record for most goals in World Cup history?",
        "options": ["Pele", "Ronaldo", "Marta", "Diego Maradona"],
        "answer": "Marta"
    },
    {
        "question": "In which sport do you perform a 'triple axel'?",
        "options": ["Figure skating", "Gymnastics", "Ice hockey", "Skiing"],
        "answer": "Figure skating"
    },
    {
        "question": "What country won the first FIFA World Cup in 1930?",
        "options": ["Brazil", "Argentina", "Italy", "Germany"],
        "answer": "Uruguay"
    },
    {
        "question": "Who is considered the greatest basketball player of all time?",
        "options": ["Michael Jordan", "LeBron James", "Kobe Bryant", "Larry Bird"],
        "answer": "Michael Jordan"
    },
    {
        "question": "How many rounds are there in a standard boxing match?",
        "options": ["10", "12", "15", "20"],
        "answer": "10 or 12"
    },
    {
        "question": "In which sport is the Ryder Cup contested?",
        "options": ["Golf", "Tennis", "Rugby", "Cricket"],
        "answer": "Golf"
    },
    {
        "question": "Who won the Tour de France in 2021?",
        "options": ["Tadej Pogačar", "Chris Froome", "Egan Bernal", "Lance Armstrong"],
        "answer": "Tadej Pogačar"
    },
    {
        "question": "What is the national sport of Japan?",
        "options": ["Baseball", "Soccer", "Sumo", "Judo"],
        "answer": "Sumo"
    }
]

def play_game():
    score = 0
    total_questions = len(questions)

    # Shuffle questions for randomness
    random.shuffle(questions)

    for idx, q in enumerate(questions):
        print(f"\nQuestion {idx + 1}/{total_questions}:")
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        
        user_answer = input("Your answer (type the option number): ")

        # Check if the input is valid
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(q["options"]):
            selected_option = q["options"][int(user_answer) - 1]
            if selected_option == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}")
        else:
            print("Invalid input. Please enter a number corresponding to your choice.")

    print(f"\nGame Over! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    play_game()

