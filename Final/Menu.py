def calc_menu():
    stop_work = False
    while(stop_work != True):
        print("Какую операцию Вы хотите произвести?")
        print("1_+; 2_-; 3_*; 4_/; 5_x_выход ?")
        user_input = int(input())
        if(user_input == 1 ):
            from Final.Addition import Addit
            ad = Addit
            print(ad)
            print('')
        elif(user_input == 2):
            from Final.Substraction import Substract
            sub = Substract
            print(sub)
            print('')
        elif(user_input == 3):
            from Final.Multiplication import Multi
            mult = Multi
            print(mult)
            print('')
        elif(user_input == 4):
            from Final.Division import Div
            di = Div
            print(di)
            print('')
        elif(user_input == 5):
            print("Завершение работы")
            stop_work = True
        else:
            print("Введено некорректное значение")

calc_menu()