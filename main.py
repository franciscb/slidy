import os,data,sys

presentation = data.presentation

def clear_screen():
    '''clear the console'''
    os.system('clear')

def get_current_slide(current_index):
    '''from a list, return element by index'''
    return presentation[current_index]

def show_title_bar(slide):
    print("===================" + slide['title'] + "==================", '\n')

def get_title(current_slide):
    return current_slide['title']

def get_text(current_slide):
    return current_slide['text']

def show(slide):
    for text_line in slide['text']:
        print(text_line)

def get_action():
    return input("< back | fw >")

def get_index_by_action(user_action):
    presentation_length = len(presentation) - 1

    if user_action == 'q':
        sys.exit()

    if user_action == '>' and current_index < presentation_length:
        return current_index + 1
    elif user_action == '>' and current_index == presentation_length:
        return 0
    elif user_action == '<' and current_index == 0:
        return presentation_length
    elif user_action == '<' and current_index < presentation_length:
        return current_index - 1
    else:
        return 0

def presentation_started():
    return True


current_index = 0

while presentation_started():

    clear_screen()

    current_slide = get_current_slide(current_index)

    show_title_bar(current_slide)

    show(current_slide)

    user_action = get_action()

    current_index = get_index_by_action(user_action)

