#While loop
def game():
    name = raw_input('\nWhat is your name?\n\n').title()

    while name == '':
        name = raw_input('\nWhat is your name?\n\n').title()
        
    print '\nWelcome', name , 'enjoy,  your adventure!\n'.title()

game()