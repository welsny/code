SCORE = {'A': 4,
        'A-':3.66667,
        'B+':3.33333,
         'B':3,
        'B-':2.66667,
        'C+':2.33333,
         'C':2}

data = open('grades').read()

raw = data.split('\n')[1:-1]

print raw

total_credits = sum(int(row.split(',')[0]) for row in raw)
total_points  = sum(SCORE[row.split(',')[1]]*int(row.split(',')[0]) for row in raw)

print total_points / total_credits

