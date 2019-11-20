from manager import edit_main


def start():
    print('Vhosts Helper - Stiles-X\n')
    print('ServerName, DocumentRoot and Port No. MUST be edited in Config/config.yaml')
    print('You are RECOMMENDED to read the templates and MUST edit them to suit your needs')
    print('Reading through the readme.md file and config.yaml RECOMMENDED before using the program')
    print('Note: You MUST run program with Administrator rights. Reason: Hosts File')
    print('Note: You MUST run program from within App directory. Reason: Relative Path')
    print('\nDo you accept that all responsibilties is solely yours?')
    input('And that you have read through the readme.md?')
    print('Program is starting ...')
    data = edit_main()
    print('\n', data)
    print('\nProgram is successfully executed')
    print('No guarantee that program executed successfully')
    input('Press anything to exit the program ...\n')


def main():
    start()
    #main_menu()


if __name__ == '__main__':
    main()