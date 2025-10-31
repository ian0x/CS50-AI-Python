from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Set the base baseknoledge for Knight and Knave game
baseKnoledge = And(
    # Can't be both knight and knave at same time
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    # Must be only or knight or knave
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
)

# Puzzle 0
# A says "I am both a knight and a knave."

a_says = And(AKnight, AKnave)
knowledge0 = And(
    baseKnoledge,
    Implication(AKnight, a_says), 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
a_says = And(AKnave, BKnave)
knowledge1 = And(
    baseKnoledge,
    Implication(AKnight, a_says),
    Implication(AKnave, Not(a_says)) 
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
a_says = And(AKnight, BKnight)
b_says = Not(a_says)
knowledge2 = And(
    baseKnoledge,
    
    Implication(BKnight, b_says), 
    Implication(BKnave, Not(b_says)) 
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
a_says = Or(AKnight, AKnave)
b_says = Implication(AKnight, BKnight)
b_says2 = CKnave
c_says = AKnight

knowledge3 = And(
    baseKnoledge,
    
    Implication(BKnight, b_says2),
    Implication(AKnave, Not(a_says)),
    Implication(CKnave, Not(c_says))
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
