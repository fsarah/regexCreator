import matplotlib.pyplot as plt

# re.compile('[0-9A-Z]+')
threshold1 = 1
matches1 = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570', 'GRG170DX', 'RG1527', 'JEM555', 'RG7620', 'JEM555', 'RG560', 'RGR320EX', 'SA260FM', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'RG270DX', 'S5470', 'JEM7V', 'RG3550MZ', 'SZ320', '4003SW', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63']
nonmatches1 = ['1993Plus', '4004Cii5']

# re.compile('[5A-Z][4A-Z][0-9M][0-9S][0-9]?[0-9A-Z]?[A-Z]?[Z]?')
threshold2 = 2
matches2 = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570', 'RG1527', 'JEM555', 'RG7620', 'JEM555', 'RG560', 'SA260FM', 'RG270DX', 'JEM7V', 'RG3550MZ', 'SZ320']
nonmatches2 = ['GRG170DX', 'RGR320EX', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'S5470', '4003SW', '1993Plus', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63', '4004Cii5']

# re.compile('[5A-Z][4A-Z][0-9M][0-9S][0-9]?[0-9A-Z]?[A-Z]?[Z]?')
threshold3 = 3
matches3 = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570', 'RG1527', 'JEM555', 'RG7620', 'JEM555', 'RG560', 'SA260FM', 'RG270DX', 'JEM7V', 'RG3550MZ', 'SZ320']
nonmatches3 = ['GRG170DX', 'RGR320EX', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'S5470', '4003SW', '1993Plus', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63', '4004Cii5']

# re.compile('[5A-Z][4A-Z][0-9M][0-9S]?[0-9]?[017A-Z]?[A-Z]?[Z]?')
threshold4 = 4
matches4 = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570', 'RG1527', 'RG7620', 'RG560', 'SA260FM', 'RG270DX', 'JEM7V', 'RG3550MZ', 'SZ320']
nonmatches4 = ['GRG170DX', 'JEM555', 'JEM555', 'RGR320EX', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'S5470', '4003SW', '1993Plus', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63', '4004Cii5']

# re.compile('[5RJSM][4A-Z][0-9M][0-9S]?[1072]?[017MQED]?[HMXZ]?[Z]?')
threshold5 = 5
matches5 = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570', 'RG1527', 'RG7620', 'RG560', 'RG270DX', 'SZ320']
nonmatches5 = ['GRG170DX', 'JEM555', 'JEM555', 'RGR320EX', 'SA260FM', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'S5470', 'JEM7V', 'RG3550MZ', '4003SW', '1993Plus', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63', '4004Cii5']

# re.compile('[5RJSM][4GPZET][0-9M][0-9S]?[1072]?[017MQED]?[HMXZ]?[Z]?')
threshold6 = 6
matches6 = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570', 'RG1527', 'RG7620', 'RG560', 'RG270DX', 'SZ320']
nonmatches6 = ['GRG170DX', 'JEM555', 'JEM555', 'RGR320EX', 'SA260FM', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'S5470', 'JEM7V', 'RG3550MZ', '4003SW', '1993Plus', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63', '4004Cii5']

# re.compile('[5RJSM][4GPZET][357801M][215703S]?[1072]?[017MQED]?[HMXZ]?[Z]?')
threshold7 = 7
matches7 = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570', 'RG1527', 'SZ320']
nonmatches7 = ['GRG170DX', 'JEM555', 'RG7620', 'JEM555', 'RG560', 'RGR320EX', 'SA260FM', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'RG270DX', 'S5470', 'JEM7V', 'RG3550MZ', '4003SW', '1993Plus', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63', '4004Cii5']

# -----------------------------------------------------------------------------------
shouldmatch = ['RG1570', 'RG321MH', 'JPM100', 'SZ520QM', 'RG350EX', 'JEM77', 'MTM2', 'RG350DXZ', 'S470', 'RG8570Z', 'RG350DX', 'RG550', '540S', 'RG7321', 'RG8570',
'GRG170DX', 'RG1527', 'JEM555', 'RG7620', 'JEM555', 'RG560', 'RGR320EX', 'SA260FM', 'GSA60', 'XPT700', 'RGR321EX', 'GAX70', 'RG270DX', 'S5470', 'JEM7V', 'RG3550MZ', 'SZ320']

shouldntmatch = ['4003SW', '1993Plus', '330', '33012', '340', '34012', '360', '4003S', '4003FL', '381V69', '38112V69', '33012W', '325C58MG', '35012V63', '4004Cii5']


matchlists = [matches1, matches2, matches3, matches4, matches5, matches6, matches7]
true_pos_list = []
false_pos_list = []
for matchlist in matchlists:
    true_pos = 0
    false_pos = 0
    for match in matchlist:
        for istruepos in shouldmatch:
            if match == istruepos:
                true_pos += 1
                break
        for isfalsepos in shouldntmatch:
            if match == isfalsepos:
                false_pos += 1
                break
    true_pos_list.append(true_pos)
    false_pos_list.append(false_pos)

nonmatchlists = [nonmatches1, nonmatches2, nonmatches3, nonmatches4, nonmatches5, nonmatches6, nonmatches7]
true_neg_list = []
false_neg_list = []
for nonmatchlist in nonmatchlists:
    true_neg = 0
    false_neg = 0
    for nonmatch in nonmatchlist:
        for istrueneg in shouldntmatch:
            if nonmatch == istrueneg:
                true_neg += 1
                break
        for isfalseneg in shouldmatch:
            if nonmatch == isfalseneg:
                false_neg += 1
                break
    true_neg_list.append(true_neg)
    false_neg_list.append(false_neg)

# print(true_pos_list)
# print(false_pos_list)
# print(true_neg_list)
# print(false_neg_list)

prec_list = []
rec_list = []

for i in range(len(true_pos_list)):
    prec = true_pos_list[i] / (true_pos_list[i] + false_pos_list[i])
    rec = true_pos_list[i] / (true_pos_list[i] + false_neg_list[i])
    prec_list.append(prec)
    rec_list.append(rec)

f1_list = []
for i in range(len(true_pos_list)):
    f1 = 2 * (prec_list[i] * rec_list[i]) / (prec_list[i] + rec_list[i])
    f1_list.append(f1)

nonmatches = [len(nonmatches1), len(nonmatches2), len(nonmatches3), len(nonmatches4), len(nonmatches5), len(nonmatches6), len(nonmatches7)]
thresholds = [1,2,3,4,5,6,7]
plt.title('F1 score/Threshold')
plt.xlabel('Threshold')
plt.ylabel('F1 score')

# plt.plot(thresholds, f1_list, marker='o') # f1 score plot
#plt.plot(rec_list, prec_list, marker='o')
#plt.plot(nonmatches, thresholds, 'ro')

# plt.axis([1, 7, 0.6, 1]) # f1 score plot

#for i in thresholds:
#    plt.annotate(str(i), xy=(rec_list[i-1], prec_list[i-1]), xytext=(rec_list[i-1] + 0.01, prec_list[i-1] + 0.01))

plt.grid(True)
# plt.savefig('f1scores.png') # f1 score plot
plt.show()
