# Scale Builder is a program created to help musicians generate any scale in any key they need and wish to know.

def scale_builder(musical_notes):
    '''This function is the option number 1 and generates any scale on the key specified by the user'''
    note_list = []
    # User chooses the note and mode to generate
    note = input('Note: ').upper()
    mode = input('Mode: ').title()
    # Selects all 12 intervals from the chosen note and adds them to "note_list" list.
    for i in range(musical_notes.index(note), musical_notes.index(note, (musical_notes.index(note) + 1))):
          note_list.append(musical_notes[i])
    # Verifies the chosen scale by the user and modifies "note_list[]" to leave only the intervals used by the scale
    if mode == 'Aeolian':
                note_list.pop(11)
                note_list.pop(9)
                note_list.pop(6)
                note_list.pop(4)
                note_list.pop(1)
                for _ in note_list:
                    print(_)
    elif mode == 'Locrian':
                note_list.pop(11)
                note_list.pop(9)
                note_list.pop(7)
                note_list.pop(4)
                note_list.pop(2)
                for _ in note_list:
                    print(_)  
    elif mode == 'Ionian':
                note_list.pop(10)
                note_list.pop(8)
                note_list.pop(6)
                note_list.pop(3)
                note_list.pop(1)
                for _ in note_list:
                    print(_)     
    elif mode == 'Dorian':
                note_list.pop(11)
                note_list.pop(8)
                note_list.pop(6)
                note_list.pop(4)
                note_list.pop(1)
                for _ in note_list:
                    print(_)      
    elif mode == 'Phrygian':
                note_list.pop(11)
                note_list.pop(9)
                note_list.pop(6)
                note_list.pop(4)
                note_list.pop(2)
                for _ in note_list:
                    print(_)        
    elif mode == 'Lydian':
                note_list.pop(10)
                note_list.pop(8)
                note_list.pop(5)
                note_list.pop(3)
                note_list.pop(1)
                for _ in note_list:
                    print(_)     
    elif mode == 'Mixolydian':
                note_list.pop(11)
                note_list.pop(8)
                note_list.pop(6)
                note_list.pop(3)
                note_list.pop(1)
                for _ in note_list:
                    print(_) 

import random
def scale_quizz(musical_notes):
    '''This function is the option number two and creates a quizz with the note and scale given by the user'''
    note_list = []
    note_dict = {}
    values = ['Tonic', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh']
    # User chooses the note
    note = input('Note: ').upper()
    # Selects all 12 intervals from the chosen note and adds them to "note_list" list.
    for i in range(musical_notes.index(note), musical_notes.index(note, musical_notes.index(note) + 1)):
          note_list.append(musical_notes[i])
    # User chooses the scale
    scale = input('Select a scale: ').title()
    # Verifies the chosen scale by the user and modifies "note_list[]" to leave only the intervals used by the scale
    # Adds keys and values to "note_dict" using "note_list[]" and "values[] lists"
    if scale == 'Aeolian':
        note_list.pop(11)
        note_list.pop(9)
        note_list.pop(6)
        note_list.pop(4)
        note_list.pop(1)
        for n, v in zip(note_list, values):
          note_dict[n] = v
        random_note, random_value = random.choice(list(note_dict.items()))
        answer = input(f'What is the {random_value} of {note} in {scale} scale?: ').upper()
        if answer == random_note:
          print('Correct')
        else:
          print('Incorrect')
    elif scale == 'Locrian':
        note_list.pop(11)
        note_list.pop(9)
        note_list.pop(7)
        note_list.pop(4)
        note_list.pop(2)
        for n, v in zip(note_list, values):
             note_dict[n] = v
        random_note, random_value = random.choice(list(note_dict.items()))
        answer = input(f'What is the {random_value} of {note} in {scale} scale?: ').upper()
        if answer == random_note:
             print('Correct')
        else:
             print('Incorrect')
    elif scale == 'Ionian':
        note_list.pop(10)
        note_list.pop(8)
        note_list.pop(6)
        note_list.pop(3)
        note_list.pop(1)
        for n, v in zip(note_list, values):
             note_dict[n] = v
        random_note, random_value = random.choice(list(note_dict.items()))
        answer = input(f'What is the {random_value} of {note} in {scale} scale?: ').upper()
        if answer == random_note:
             print('Correct')
        else:
             print('Incorrect')
    elif scale == 'Dorian':
        note_list.pop(11)
        note_list.pop(8)
        note_list.pop(6)
        note_list.pop(4)
        note_list.pop(1)
        for n, v in zip(note_list, values):
             note_dict[n] = v
        random_note, random_value = random.choice(list(note_dict.items()))
        answer = input(f'What is the {random_value} of {note} in {scale} scale?: ').upper()
        if answer == random_note:
             print('Correct')
        else:
             print('Incorrect')
    elif scale == 'Phrygian':
        note_list.pop(11)
        note_list.pop(9)
        note_list.pop(6)
        note_list.pop(4)
        note_list.pop(2)
        for n, v in zip(note_list, values):
             note_dict[n] = v
        random_note, random_value = random.choice(list(note_dict.items()))
        answer = input(f'What is the {random_value} of {note} in {scale} scale?: ').upper()
        if answer == random_note:
             print('Correct')
        else:
             print('Incorrect')
    elif scale == 'Lydian':
        note_list.pop(10)
        note_list.pop(8)
        note_list.pop(5)
        note_list.pop(3)
        note_list.pop(1)
        for n, v in zip(note_list, values):
             note_dict[n] = v
        random_note, random_value = random.choice(list(note_dict.items()))
        answer = input(f'What is the {random_value} of {note} in {scale} scale?: ').upper()
        if answer == random_note:
             print('Correct')
        else:
             print('Incorrect')
    elif scale == 'Mixolydian':
        note_list.pop(11)
        note_list.pop(8)
        note_list.pop(6)
        note_list.pop(3)
        note_list.pop(1)
        for n, v in zip(note_list, values):
             note_dict[n] = v
        random_note, random_value = random.choice(list(note_dict.items()))
        answer = input(f'What is the {random_value} of {note} in {scale} scale?: ').upper()
        if answer == random_note:
             print('Correct')
        else:
             print('Incorrect')
        
def main(): 
    musical_notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
    print('\nWelcome To "Scale Builder"')
    keep_playing = input('Start [Yes/No]: ')
    while keep_playing.title() != 'No':
        print('\nOptions: \n(1) Generate a scale (2) Scale Quizz (3) Exit')
        option = input('\nPlease, select an option: ')
        if option == '1':
            scale_builder(musical_notes)
            keep_playing = input('Keep playing [Yes/No]: ')
        elif option == '2':
            scale_quizz(musical_notes)
            keep_playing = input('Keep playing [Yes/No]: ')
        elif option == '3':
            break
        else: 
            print('\nInvalid option, try again')  
    print('Exited succesfully') 
    

if __name__ == '__main__':
    main()