from random import shuffle, choice  # подключаем рандом
from snowman import*


# перемешиваем слова и выбираем одно
words = ['автомастерская', 'авторазгрузчик', 'любознательный','благосостояние','вознаграждение  ']  # список слов
tmp = choice(words)  # выбираем случайное слово
zagadannoe_slovo = []
for let in tmp:
    zagadannoe_slovo.append(let)
len_of_word = len(zagadannoe_slovo)  # длина случайного слова
count_of_wrong = 0  # счетчик снеговика
count_of_right = 0  # счетчик правильных букв
is_game = True

slovo_kotoroe_nado_otgadat = list()  # пустой список
for let in zagadannoe_slovo:  # запускается цикл
    slovo_kotoroe_nado_otgadat.append('[*]')  # в списке появляются звездочки вместо букв

# запускаем цикл
while is_game == True:

    print('ТЕКУЩЕЕ СЛОВО', end=': ')  # выводится текущее слово
    for let in slovo_kotoroe_nado_otgadat:  # запуск цикла
        print(let, end=' ')
    print()

    user_let = input("enter a letter: ")

    if user_let in zagadannoe_slovo:
        index = zagadannoe_slovo.index(user_let)
        zagadannoe_slovo[index] = '*'
        slovo_kotoroe_nado_otgadat[index] = user_let
        count_of_right += 1
    else:
        count_of_wrong += 1
        if count_of_wrong == 1:
            circle_bottom()
        elif count_of_wrong == 2:
            circle_center()
        elif count_of_wrong == 3:
            circle_top()
        elif count_of_wrong == 4:
           nose()
        elif count_of_wrong == 5:
            eye_left()
        elif count_of_wrong == 6:
            eye_right()
        elif count_of_wrong == 7:
            mouth()
        elif count_of_wrong == 8:
            button_1()
        elif count_of_wrong == 9:
            button_2()
        elif count_of_wrong == 10:
            button_3()
        elif count_of_wrong == 11:
            button_4()
        elif count_of_wrong == 12:
            left_hand()
        elif count_of_wrong == 13:
            right_hand()
        elif count_of_wrong == 14:
            bucket()



    print("\nКоличество разгаданных букв:", count_of_right, '\n')
    print("\nКоличество неправильных букв:", count_of_wrong, '\n')

    if count_of_wrong == 14:
        # количество зависит от количества частей снеговика
        print("u r lose")
        is_game = False
        # проверка отгаданного слова (счетчик)
    if count_of_right == len_of_word:
        print('Верно! Ты победил!')
        is_game = False

#####################################################################
	#### PLAN ###
	
# # ввод пользователя
# 	user_letter = input("Введи букву:\n>>>")
	
# 	# если буква правильна, то записываем в консоль
# 	if user_letter in zagadannoe_slovo:
# 		pass
# 		# найти индекс буквы в current_word
# 		# заменить * на букву
# 		# увеличить счетик на 1
		   
# 	# иначе рисуем часть снеговика
# 		# увеличить счетик на 1
# 		# рисуем +1 часть снеговика
	
# 	# проверка всего снеговика (счетчик)
# 	if count_of_wrong == 14:
# 		# количество зависит от количества частей снеговика
# 		print("u r lose")
# 		is_game = False
# 	# проверка отгаданного слова (счетчик)
# 	if count_of_right == len_of_word:
# 		print('Верно! Ты победил!')
# 		is_game = False









