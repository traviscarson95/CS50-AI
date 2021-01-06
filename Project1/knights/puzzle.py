from Project1.knights.logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# => And(AKnight, AKnave)
knowledge0 = And(
    # Rules of Knights and Knaves
    Or(
        And(AKnight, Not(AKnave)), 
        And(Not(AKnight), AKnave)
    ), 
    # If A is a knight, their statement will be true OR if A is a knave their statement will be false
    Or(
        And(AKnight, And(AKnight, AKnave)), 
        And(AKnave, Not(And(AKnight, AKnave)))
    )
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
# A says => (AKnight & (AKnave & BKnave)) || (AKnave & ~(AKnave & BKnave))
knowledge1 = And(
    # A is a knight or a knave, and B is a knight or a knave
    And(
        # A is a knight or a knave, but not both
        Or(
            And(AKnight, Not(AKnave)), 
            And(Not(AKnight), AKnave)
        ),
        # B is a knight or a knave, but not both
        Or(
            And(BKnight, Not(BKnave)), 
            And(Not(BKnight), BKnave)
        )
    ),     
    Or(
        And(AKnight, And(AKnave, BKnave)), 
        And(AKnave, Not(And(AKnave, BKnave)))
    )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# A says => (AKnight && BKnight) || (AKnave && BKNave)
# B says => (AKnight && BKnave) || (AKnave && BKnight)
knowledge2 = And(
    # A is a knight or a knave, and B is a knight or a knave
    And(
        # A is a knight or a knave, but not both
        Or(
            And(AKnight, Not(AKnave)), 
            And(Not(AKnight), AKnave)
        ),
        # B is a knight or a knave, but not both
        Or(
            And(BKnight, Not(BKnave)), 
            And(Not(BKnight), BKnave)
        )
    ),     
    And(
        Or(
            And(AKnight, 
                Or(
                    And(AKnight, BKnight), 
                    And(AKnave, BKnave)
                )
            ), 
            And(AKnave, 
                Not(
                    Or(
                        And(AKnight, BKnight), 
                        And(AKnave, BKnave)
                    )
                )
            )
        ),
        Or(
            And(BKnight, 
                Or(
                    And(AKnight, BKnave), 
                    And(AKnave, BKnight)
                )
            ),
            And(BKnave, 
                Not(
                    Or(
                        And(AKnight, BKnave), 
                        And(AKnave, BKnight)
                    )
                )
            )
        )
    )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# A says => AKnight || AKnave
# B says => AKnave
# B says => CKnave
# C says => AKnight
knowledge3 = And(
    # A is a knight or a knave, B is a knight or a knave, and C is a knight or a knave
    And(
        # A is a knight or a knave, but not both
        Or(
            And(AKnight, Not(AKnave)), 
            And(Not(AKnight), AKnave)
        ),
        # B is a knight or a knave, but not both
        Or(
            And(BKnight, Not(BKnave)), 
            And(Not(BKnight), BKnave)
        ),
        # C is a knight or a knave, but not both
        Or(
            And(CKnight, Not(CKnave)), 
            And(Not(CKnight), CKnave)
        )
    ), 
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
