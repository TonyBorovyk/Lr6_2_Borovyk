import sys


# Функція перевірки, щоб провірити, чи поточний колір правильний  для вершины v і чи його потрібно змінит
# За

def checkVersh(versh, color, col):
    for i in range(len(create_matrix_sumizh())):
        if matrix_sum[versh][i] == 1:
            if color[i] == col:
                return False
    return True


# Якщо всім вершинам присвоєно колір повернути True # Перевіряє чи наступна вершина має колір
def graphColorCheck(MaxlenOfColors, color, versh):
    if versh == len(create_matrix_sumizh()):
        return True
        # Присвоює кольори,якщо залишились вершини без кольора
    for col in range(1, MaxlenOfColors + 1):
        if checkVersh(versh, color, col) == True:
            color[versh] = col
            if graphColorCheck(MaxlenOfColors, color, versh + 1) == True:
                return True
            color[versh] = 0


def WershToColor(MaxlenOfColors):
    # Ініціалізуємо всі вершини(їх коляр дорівнює 0)
    color = [0] * len(create_matrix_sumizh())
    # Перевіряємо чи колір присвоєний для інших вершин графа
    if graphColorCheck(MaxlenOfColors, color, 0) == None:
        return False
    versh = 1
    print("Хроматичне число дорівнює: %s" % max(color))
    for col in color:
        print("%s вершина має колір: %s" % (versh, col))
        versh += 1
    return True


def create_matrix_sumizh():
    file = open('File.txt')
    info = file.readline()
    info_size = info.split(" ")
    if ((int(info_size[0]) == 0) and (int(info_size[1]) == 0)) or (int(info_size[0]) == 0):
        sys.exit("Помилка! Оскільки кількість вершин дорівнює нулю!")
    else:
        matrix_sumizh = [[0] * int(info_size[0]) for x in range(int(info_size[0]))]
        for i in range(int(info_size[1])):
            info_versh = file.readline()
            info_versh_arr = info_versh.split(" ")
            matrix_sumizh[int(info_versh_arr[0]) - 1][int(info_versh_arr[1]) - 1] = 1
            matrix_sumizh[int(info_versh_arr[1]) - 1][int(info_versh_arr[0]) - 1] = 1
        file.close()
        return matrix_sumizh


matrix_sum = create_matrix_sumizh()
MaxlenOfColors = len(create_matrix_sumizh())  # Максимальна к-сть кольорів
WershToColor(MaxlenOfColors)
