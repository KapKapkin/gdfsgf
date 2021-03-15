import time

item1 = False
item2 = False
last_room = 1
room = 1
print("И снова лабиринт... Так не хотелось его делать, ну да ладно)")
print("Этот лабиринт - вообще не лабиринт. Это просто квадрат 3х3. "
      "\n\t 9\n  8     6\n7 \t 5 \t  3 \n  4     2\n\t 1\nНумерация комнат\n"
      "Перемещаться можно только между соседними комнатами. "
      "То есть из 1 комнаты нельзя переместиться в 5. Только во 2 или 4.\n"
      "При перемещении персонаж будет разворачиваться в сторону "
      "вашего движения.\n"
      "Вам всегда будет выводиться 4 варианта движения, по этому "
      "ориентируйтесь по карте.")
print('Вы попали в начало лабиринта')
while last_room:
    choice = 0
    if room == 1:
        print(1)
        choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')
    elif 2 == room:
        print("2\nВы заходите в комнату\n "
              "Рядом - углубление в стене. Напротив, на другой  "
              "стене - странная кнопка.\n "
              "Неожиданно для вас, стены начинают двигаться, а дверь "
              "за вами закрылась. "
              "Надо быстро принять решение, или они вас раздавят.\n"
              "Залезть в углубление(1) или нажать на кнопку(2)? "
              "У вас есть 12 секунд ")
        flag = True
        flag1 = True

        for i in range(1):
            start = time.time()
            answer = int(input())
            while answer != 1 or answer != 2:
                if time.time() - start >= 12:
                    print('Вы не успели и вас расплющило.')
                    flag = False
                    break
                elif answer == 1:
                    print(
                        "Вы залезли в углубление и смогли спастись. "
                        "Но к сожалению стены замуровали вас здесь навсегда.")
                    flag1 = False
                    break
                elif answer == 2:
                    print("Вы нажали на кнопку, и стены остановились. "
                          "Вы живы")
                    break
                else:
                    print("Повторите попытку ввода. Неправильный ответ.")
                    answer = int(input())
        if not flag1:
            print("Игра окончена.")
            break
        elif flag:
            choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')
    elif room == 3:
        print(3)
        print("На вас напал заяц! 10 раз напишите и введдите букву \"G\","
              " чтобы отбиться.")
        count = 0
        flag = True
        while count != 10:
            G = input()
            if G != "G":
                print("Вы ввели не ту букву и вас съел заяц. Конец.")
                flag = False
                break
            elif G == "G":
                count += 1
        if not flag:
            break
        elif flag:
            print("Вы отбились от зайца. Можно идти дальше.")
            choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')

    elif room == 4:
        print(4)
        food = input('Вы вошли в третью комнату. Здесь вас встречает '
                     'Сфинкс и говорит, если вы ответите на его вопрос,\n'
                     'то он пропустит вас дальше, а если нет... '
                     'Сами понимаете).\n'
                     'Вопрос следующий \"Кто проживает на дне океана?\" '
                     'Спанч Боб или Дуэйн Джонсон ')
        if food == "Спанч Боб":
            print("Ответ правильный")
            choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')
        elif food == "Дуэйн Джонсон":
            print("Вы ответили неправильно. Вас целиком съедает Сфинкс.."
                  "Игра окончена")
            break
    elif room == 5:
        print(5)
        while not item1 or not item2:
            item = int(input("На столе лежит верёвка(1) и ключ(2). "
                             "Что возьмём? "))
            if item == 1:
                item1 = True
                break
            elif item == 2:
                item2 = True
                break
            else:
                print("Неккоректный ввод")
        choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')

    elif room == 6:
        print(6)
        print("Просто пустая комната")
        choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')

    elif room == 7:
        print(7)
        print("Просто пустая комната.")
        choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')

    elif room == 8:
        if not item2:
            print("Дверь в следующую комнату заперта, а у вас нет ключа, чтобы"
                  " открыть её.\n "
                  "Сзади вас куча голодных медведей. Видимо, сегодня не ваш "
                  "день... Конец.")
            break
        elif item2:
            print(8)
            print("Вы бежите от медведей и открываете дверь в комнату "
                  "найденным ключом.")

        choice = input('Куда пойдём (обратно, прямо, направо, налево)? ')

    elif room == 9:
        print(9)
        print("Вы открыли дверь и чуть не упали в пропасть. "
              "Вы находитесь на отвесной скале и надо как-то спуститься вниз")
        if item1:
            print("К счастью у вас была веревка, и вы спокойно спускаетесь "
                  "вниз. Вы выбрались. Конец.")
            break
        else:
            print("Вы очень осторожно спускаетесь вниз по скале, "
                  "но нога соскальзывает "
                  "и вы падаете вниз, понимая, что надо было взять "
                  "верёвку. Конец.")
            break

    if choice != "прямо" and choice != "обратно" and choice != "направо" and \
            choice != "налево":
        print("Тут небольшой недочёт и ввести это здесь или "
              "сейчас нельзя. Попробуйте ввести что-нибудь другое.")
        break
    elif choice == "обратно":
        last_room, room = room, last_room
    elif choice == "прямо" or choice == "направо" or choice == "налево":
        if choice == "прямо":
            last1_room = last_room
            last_room = room
            if room == 3:
                if last1_room == 2:
                    room += 3
                elif last1_room == 6:
                    room -= 1
            elif room == 7:
                if last1_room == 4:
                    room += 1
                elif last1_room == 8:
                    room -= 3
            elif room == 5:
                if last1_room == 2:
                    room += 3
                elif last1_room == 4:
                    room += 1
                elif last1_room == 6:
                    room -= 1
                elif last1_room == 8:
                    room -= 3
            elif room == 1 and last1_room != 1:
                if last1_room == 2:
                    room += 3
                elif last1_room == 4:
                    room += 1
            else:
                print(
                    "Тут небольшой недочёт и ввести это здесь или сейчас"
                    " нельзя. Попробуйте ввести что-нибудь другое.")
                continue

        elif choice == "направо" and room != 7 and room != 3:
            if room == 4:
                if last_room == 5:
                    last_room = room
                    room += 3
                elif last_room == 7:
                    last_room = room
                    room -= 3
                elif last_room == 1:
                    last_room = room
                    room += 1
            elif room == 8:
                if last_room == 7:
                    last_room = room
                    room -= 3
                elif last_room == 5:
                    last_room = room
                    room += 1
            elif room == 6:
                if last_room == 3:
                    last_room = room
                    room += 3
                elif last_room == 5:
                    last_room = room
                    room -= 3
            elif last_room > room:
                last_room = room
                room -= 1
            elif room >= last_room:
                last_room = room
                room += 1

            else:
                print(
                    "Тут небольшой недочёт и ввести это здесь или "
                    "сейчас нельзя. Попробуйте ввести что-нибудь другое.")
                continue
        elif choice == "налево" and room != 7 and room != 3:
            if room == 5:
                if last_room == 2:
                    last_room = room
                    room -= 1
                elif last_room == 4:
                    last_room = room
                    room += 3
                elif last_room == 6:
                    last_room = room
                    room -= 3
                elif last_room == 8:
                    last_room = room
                    room += 1
            elif room == 8:
                if last_room == 7:
                    last_room = room
                    room += 1
                elif last_room == 5:
                    last_room = room
                    room -= 1
            elif room == 2:
                if last_room == 3:
                    last_room = room
                    room -= 1
                elif last_room == 5:
                    last_room = room
                    room += 1
                elif last_room == 1:
                    last_room = room
                    room += 3
            elif room == 6 and last_room == 3:
                last_room = room
                room -= 1
            elif last_room > room:
                last_room = room
                room -= 3
            elif room >= last_room:
                last_room = room
                room += 3