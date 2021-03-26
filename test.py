import xlsxwriter
# ЭТО ТОЖЕ УБЕРИ
from sys import stdin


def export_check(text):
    # ''.join(text).split('---') замени на text.split('---')
    text = [i.split('\n') for i in ''.join(text).split('---')]
    workbook = xlsxwriter.Workbook('res.xlsx')
    data = {}
    worksheet = workbook.add_worksheet()
    for i in range(len(text)):
        copy = [j.split('\t') for j in text[i] if j != '']
        copy.sort(key=lambda x: [x[0], int(x[2])])
        text[i] = list(map(lambda x: '\t'.join(x), copy))
        for j in text[i]:
            word = j.split('\t')
            if word != ['']:
                if word[0] + '\t' + word[1] not in data:
                    data[word[0] + '\t' + word[1]] = [float(word[1]), float(word[2])]
                else:
                    data[word[0] + '\t' + word[1]][1] += float(word[2])

        for key in range(len(data.keys())):
            ind = list(data.keys())[key]
            worksheet.write(key, 0, ind.split('\t')[0])
            worksheet.write(key, 1, data[ind][0])
            worksheet.write(key, 2, data[ind][1])
            worksheet.write(key, 3, f'=B{key + 1}*C{key + 1}')

        worksheet.write(f'A{len(data) + 1}', 'Итого')
        worksheet.write(f'D{len(data) + 1}', f'=SUM(D1:D{len(data)})')

        if i != len(text) - 1:
            data = {}
            worksheet = workbook.add_worksheet()

    workbook.close()


# УБЕРЕШЬ
export_check(stdin.readlines())

