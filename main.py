keyword = input('Do you have a birthday today? (please enter yes/no or may was...) ')
keyword = keyword.lower()
if keyword == 'yes':
    print('\nCONGRATULATIONS!!!!!')
    print('''☆•°*”˜˜”*°•.¸☆ ★ ☆¸.•°*”˜˜”*°•.¸
╔╗╔╦══╦═╦═╦╗╔╗ (¯`v´¯)
║╚╝║══║═║═║╚╝║ `•.¸.•'BIRTHDAY
║╔╗║╔╗║╔╣╔╩╗╔╝ ★ ¸.•´¸.•¨) ¸.•¨)
╚╝╚╩╝╚╩╝╚╝═╚╝ ♥(¸.•´ (¸.•´ (¸.•¨
☆•°*”˜˜”*°•.¸☆ ★ ☆¸.•°*”˜˜”*°•.¸''')
    print('''\nМій любий Романе,
в твій день народження бажаю тобі:
сміливості, відваги, мужності та рішучості!
Нехай швидкість, з якою ти рухатимешся до мрії буде космічною!
Домагайся поставленої мети, хоч би якою неможливою вона не здавалася!
А я готовий допомагати добрим словом та надихати тебе!)
Стань кращою версією себе за цей рік, 
щоб наступний день народження ми відзначали десь в Австралії чи Нью-Йорку
— там, де тобі приємніше!)''')
    print('\nЗ ДНЕМ НАРОДЖЕННЯ, ДРУЖЕЕЕЕЕЕЕ!!!!!!')
elif keyword == 'no':
    print('\nPlease wait for your birthday) and then enter "yes".\n\n')
    print('''░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▄██▄░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▄████▄░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░██░██░█▄░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█▀░░██░░▀█░░░░░░░░░░░░░░
░░░░░░░░░░░░░█▀░░░██░░░▀█░░░░░░░░░░░░░
░░░░░░░░░░░▄█▀░░▄▄██▄▄░░▀█░░░░░░░░░░░░
░░░░░░░░░░▄██▄█▀▀░██░▀▀█▄██▄░░░░░░░░░░
░░░░░░░░░▄██▀░░░░░██░░░░░▀██▄░░░░░░░░░
░░░░░░░░▄██▀░░░░░░██░░░░░░▀██▄░░░░░░░░
░░░░░░░████░░░░░░░██░░░░░░░███▄░░░░░░░
░░░░░░█▀░█░░░░░░░░██░░░░░░░░█░▀█░░░░░░
░░░░░█▀░░██░░░░░░░██░░░░░░░██░░▀█░░░░░
░░░▄█▀░░░░█▄░░░░░░██░░░░░░▄█░░░░▀█▄░░░
░░▄█▀░░░░░░█▄░░░░░██░░░░░▄█░░░░░░▀█▄░░
░▄█░░░░░░░░░▀▀█▄▄▄██▄▄▄█▀▀░░░░░░░░░█▄░
▄█▄▄▄▄▄▄▄▄▄▄▄▄▄████████▄▄▄▄▄▄▄▄▄▄▄▄▄█▄''')
    print('Do you know whose sign this is ??')
elif keyword == 'was':
    print('''\nOhh, I`m so sorry!!! 
I`m really forget your date birthday. 
Please don`t be upset!''')
    print('if this has already happened, restart and enter "yes".')
else:
    print('Please enter only "yes" or "no" or even "was"!')
input()