# pylint: disable-msg=too-many-function-args
from parking_lot_system.interactive_app import InteractiveApp

if __name__ == "__main__":
    print('Welcome to automated Parking Ticketing System !!')
    print('Provide the commands. Press Enter to exit..')
    input_command = ''
    interactive_app = InteractiveApp()

    while True:
        input_command = input()
        if input_command == '':
            break
        if input_command.startswith('create_parking_lot'):
            interactive_app.create_parking_lot(input_command)
        elif input_command.startswith('park'):
            interactive_app.park(input_command)
        elif input_command.startswith('leave'):
            interactive_app.leave(input_command)
        elif input_command.startswith('status'):
            interactive_app.status()
        elif input_command.startswith('registration_numbers_for_cars_with_colour'):
            interactive_app.registration_numbers_for_cars_with_colour(input_command)
        elif input_command.startswith('slot_numbers_for_cars_with_colour'):
            interactive_app.slot_numbers_for_cars_with_colour(input_command)
        elif input_command.startswith('slot_number_for_registration_number'):
            interactive_app.slot_number_for_registration_number(input_command)
