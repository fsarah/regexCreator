import matplotlib.pyplot as plt

Matches1 = ['A1234', 'C3456', 'D4567', 'F6789', 'G7890', 'H8901', 'I9012', 'J0123', 'K1234', 'B2345']
NonMatches1 = []
WrongMatches = 1 #B2345
WrongNonMatches = len(NonMatches1)

Matches2 = ['A1234', 'C3456', 'D4567']
NonMatches2 = ['F6789', 'G7890', 'H8901', 'I9012', 'J0123', 'K1234', 'B2345']
WrongMatches2 = 0
WrongNonMatches2 = len(NonMatches2)

matches = [WrongMatches, WrongMatches2]
nonmatches = [WrongNonMatches, WrongNonMatches2]
plt.title('Wrong matches/wrong non-matches:')
plt.xlabel('Wrong matches')
plt.ylabel('Wrong non-matches')
plt.plot(matches, nonmatches, 'ro')
plt.axis([-1, 5, -1, 8])
plt.grid(True)
plt.savefig('wrong_matches.png')