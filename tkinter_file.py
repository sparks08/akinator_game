from tkinter import *
from tkinter import simpledialog
import pandas as pd
from colorama import Fore,Style,Back
import requests
from io import BytesIO
from PIL import Image, ImageTk
import cv2
import numpy as np
import sys


i_want_to_exit = 'No'
while i_want_to_exit != 'Yes':

    root = Tk()
    root.title("Desiapp.romrom")
    # set th background
    root.config(background='#EEF0E5')
    # set the configuration on gui window
    root.geometry("800x500")
    # create a welcome

    def buttons_work(question):
        result_var = None  # Variable to store the result

        def option_pressed(value):
            nonlocal result_var
            result_var = value
            root.quit()  # Stop the main loop when any button is pressed


        headlabel = Label(root, text="Hi, Welcome to our Desi App", fg='#3559E0', bg='#EEF0E5', font=('Helvetica', 20, 'bold'))
        question = Label(root, text=question, fg='#3559E0', bg='#EEF0E5', font=('Helvetica', 16,'bold'),width=55)
        #Use lambda to pass a parameter to the function
        option1 = Button(root, text="Yes", fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed("y"))
        option2 = Button(root, text="No", fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed("n"))
        option3 = Button(root, text="May be", fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed("May be"))
        option4 = Button(root, text="Don't know", fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed("Don't know"))
        exit_button = Button(root, text="❌", fg='red', bg='#B6BBC4', width=2, command=root.destroy)

        headlabel.grid(row=0, column=1, columnspan=1, pady=20)
        question.grid(row=1, column=1, columnspan=1, pady=10, sticky='w')
        option1.grid(row=2, column=1, columnspan=3, pady=10, sticky='w')
        option2.grid(row=3, column=1, columnspan=3, pady=10, sticky='w')
        option3.grid(row=4, column=1, columnspan=3, pady=10, sticky='w')
        option4.grid(row=5, column=1, columnspan=3, pady=10, sticky='w')
        exit_button.grid(row=0, column=3, columnspan=3, pady=10, sticky='w')

        root.mainloop()  # Start the main loop

        return result_var

    def image_show(photo, output):
        result_var = None  # Variable to store the result

        def option_pressed(value):
            nonlocal result_var
            result_var = value
            root.quit()  # Stop the main loop when any button is pressed

        root.config(background='#EEF0E5')
        headlabel = Label(root, text="I got you..", fg='#3559E0', width=70, bg='#EEF0E5',font=('Helvetica', 20, 'bold'))
        question = Label(root, text=str.capitalize(output), fg='#3559E0', bg='#EEF0E5', font=('Helvetica', 16,'bold'), width=55)

        #Use lambda to pass a parameter to the function
        image_label = Label(root, image=photo)
        option1 = Button(root, text="Yes", fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed("y"))
        option2 = Button(root, text="No", fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed("n"))
        # option3 = Button(root, text="Exit", fg='black', bg='lightblue', width=20, command=root.destroy)
        exit_button = Button(root, text="❌", fg='red', bg='#B6BBC4', width=2, command=root.destroy)

        headlabel.grid(row=0, column=1, columnspan=1, pady=20)
        question.grid(row=1, column=1, columnspan=1, pady=10, sticky='w')
        image_label.grid(row=2, column=1, columnspan=6, pady=10, sticky='w')
        option1.grid(row=3, column=1, columnspan=1, pady=10, sticky='w')
        option2.grid(row=3, column=2, columnspan=2, pady=10, sticky='w')
        # option3.grid(row=4, column=3, columnspan=1, pady=10, sticky='w')
        exit_button.grid(row=0, column=3, columnspan=3, pady=10, sticky='w')

        root.mainloop()  # Start the main loop
        return result_var


    def tk_start_game(choose, op1, op2, op3):
        result_var = None  # Variable to store the result

        def option_pressed(value):
            nonlocal result_var
            result_var = value
            root.quit()  # Stop the main loop when any button is pressed

        headlabel = Label(root, text="Hi, Welcome to our Desi App", fg='#3559E0', bg='#EEF0E5', font=('Helvetica', 20, 'bold'))
        question_label = Label(root, text=choose, fg='#3559E0', bg='#EEF0E5', font=('Helvetica', 16,'bold'), width=55)
        option1 = Button(root, text=op1, fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed(op1))
        option2 = Button(root, text=op2, fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed(op2))
        option3 = Button(root, text=op3, fg='black', bg='#B6BBC4',width = 20, command=lambda: option_pressed(op3))
        # option4 = Button(root, text=op4, fg='black', bg='white', width=20, command=lambda: option_pressed(op4))
        exit_button = Button(root, text="❌", fg='red',bg='#B6BBC4', width=2, command=root.destroy)

        headlabel.grid(row=0, column=1, columnspan=1, pady=20)
        question_label.grid(row=1, column=1, columnspan=1, pady=10, sticky='w')
        option1.grid(row=2, column=1, columnspan=3, pady=10, sticky='w')
        option2.grid(row=3, column=1, columnspan=2, pady=10, sticky='w')
        option3.grid(row=4, column=1, columnspan=3, pady=10, sticky='w')
        # option4.grid(row=5, column=1, columnspan=3, pady=10, sticky='w')
        exit_button.grid(row=0, column=3, columnspan=3, pady=10, sticky='w')

        root.mainloop()  # Start the main loop

        return result_var

    # Configure column weights to center the labels
    for i in range(3):
        root.columnconfigure(i, weight=1)


    animals = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri"
                          "-smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=522745683"
                          "&single=true&output=csv")
    characters = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri-smJi4jWa7hqt_PgsQRlNyxMUasSk'
                             'hR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=645902942&single=true&output=csv')

    others = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri'
                         '-smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=1796877773'
                         '&single=true&output=csv')
    # fruits = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri
    # -smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=55564916&single=true&output=csv")

    # Page1 - choose the options to start the game
    def choosing_option():
        return "Choose any one ..", "Character", "Animal", "Other"

    # Page2 - Let's start the game by deciding the dataset
    def game_start(start_game, characters, animals, others):

        start_game = str.capitalize(start_game)

        if start_game == 'Character':
            data = characters
            data_key = 'human'
        elif start_game == 'Animal':
            data = animals
            data_key = 'animal'
        elif start_game == 'Other':
            data = others
            data_key = 'object'
        # elif start_game == 'Fruit':
        #     data = fruits
        #     data_key = 'a fruit'

        else:
            print("Choose from mentioned options.")
        return data, data_key, start_game


    def data_filteration(data):
        counts_of_true = data.iloc[:, 2:].sum(axis=0).sort_values(ascending=False)
        count_index = counts_of_true.reset_index()
        count_index.columns = ['index', 'values']
        count_index = count_index[count_index['values'] != 0]
        sum_value_count = count_index['values'].max()
        count_index[count_index['values'] != sum_value_count]
        count_index_keys_list = count_index['index'].values
        # removing items from countIndex
        keys_left = [key for key in count_index_keys_list if key not in keys_used]
        return keys_left


    def question_generation(key, user_choice):
        if user_choice == 'other':
            return f"Is it {key}?"
        elif user_choice == 'fruit':
            return f"Is your fruit {key}?"
        else:
            return f"Is your character {key}?"

    def write_text_on_image_from_url(image_url, key_value):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_array = np.array(Image.open(BytesIO(response.content)))

            # Convert the image to grayscale
            image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

            # Resize the image
            resized_bgr_image = cv2.resize(image, (600,300), interpolation=cv2.INTER_AREA)
            rgb_image = cv2.cvtColor(resized_bgr_image, cv2.COLOR_BGR2RGB)
            image_pil = Image.fromarray(rgb_image)
            image_tk = ImageTk.PhotoImage(image_pil)
            return image_tk
        else:
            return f"Error: Unable"


    # startups
    final_answer = 'No'
    start = 0
    # data_key = 'human'
    # select_key = 'character'
    keys_used = []

    # calling 1st function of game code
    option_choose, option_1, option_2, option_3 = choosing_option()
    # calling 1st function of tkinter
    option_choose_final_value = tk_start_game(option_choose, option_1, option_2, option_3)

    # calling 2nd function of game code
    data, data_key, user_choice_data_name = game_start(option_choose_final_value, characters, animals, others)

    # starting 1 question asking
    question = ''
    if start == 0:
        question = question_generation(data_key,user_choice_data_name)
        key = data_key
        keys_used.append(key)
        start += 1

    ################################ looping start ######################
    final_answer = 0
    select_key = user_choice_data_name
    while final_answer != 1:
        if key =='a fruit':
            select_key = 'fruit'
        elif key == 'a appliance':
            select_key = 'object'

        value = buttons_work(question)

        if value == 'y':
            try:
                data = data[data[key] == True]
                print(data.name.sort_values().values, "   -->", len(data.name.sort_values().values))
                if data.shape[0] == 1:
                    final_value = data.values[0][0]
                    final_value_image = data['image'].values[0]
                    print(Fore.GREEN + f"I think of\n {str.capitalize(final_value)}")
                    root.config(background='lightblue')
                    # set the configuration on gui window
                    root.geometry("800x500")
                    photo = write_text_on_image_from_url(final_value_image, str.capitalize(final_value))
                    final_answer += 1
                    # image on tkinter
                    image_output = image_show(photo, final_value)
                    print(image_output)
                    break
                if data.shape[0] == 0:
                    print("OOPS .. we lost!")
                    break
                keys_used.append(key)
                keys_left = data_filteration(data)
                key = keys_left[0]
                question = question_generation(key, select_key)
                print(question)
            except:
                root.destroy()

                lost = Tk()
                lost.title("Desiapp.romrom")
                lost.config(background='lightblue')
                lost.geometry("800x500")

                ourMessage = '"OOPS .. we lost you buddy!! Try Again"'
                messageVar = Message(lost, text=ourMessage, width=500,font=('Helvetica', 30, 'bold'))
                messageVar.config(bg='lightgreen')
                tr_again = Button(lost, text="Try Again", fg='black', bg='white', width=20)
                exit_button = Button(lost, text="❌", fg='red', width=2, command=lost.destroy)

                messageVar.grid(row=0, column=1, columnspan=1, pady=30, sticky='w')
                tr_again.grid(row=4, column=2, columnspan=3, pady=50, sticky='w')
                exit_button.grid(row=0, column=3, columnspan=3, pady=10, sticky='w')
                for i in range(3):
                    lost.columnconfigure(i, weight=1)
                lost.mainloop()
                # lost.destroy()
                final_answer += 1


        elif value == 'n':
            try:
                data = data[data[key] != True]
                print(data.name.sort_values().values,"   -->", len(data.name.sort_values().values))
                if data.shape[0] == 1:
                    final_value = data.values[0][0]
                    final_value_image = data['image'].values[0]
                    print(Fore.GREEN + f"I think of\n {str.capitalize(final_value)}")

                    photo = write_text_on_image_from_url(final_value_image, str.capitalize(final_value))
                    final_answer += 1
                    # image on tkinter
                    image_output = image_show(photo, final_value)
                    break
                keys_used.append(key)  # update the key
                keys_left = data_filteration(data)  # finding keys to be used for question in each filtered data
                key = keys_left[0]  # taking first key for generating question
                question = question_generation(key, select_key)
                print(question)
            except:
                root.destroy()

                lost = Tk()
                lost.title("Desiapp.romrom")
                lost.config(background='lightblue')
                lost.geometry("800x500")

                ourMessage = '"OOPS .. we lost you buddy!! Try Again"'
                messageVar = Message(lost, text=ourMessage, width=500,font=('Helvetica', 30, 'bold'))
                messageVar.config(bg='lightgreen')
                tr_again = Button(lost, text="Don't know", fg='black', bg='white', width=20)
                exit_button = Button(lost, text="❌", fg='red', width=2, command=lost.destroy)

                messageVar.grid(row=0, column=1, columnspan=1, pady=30, sticky='w')
                tr_again.grid(row=4, column=2, columnspan=3, pady=50, sticky='w')
                exit_button.grid(row=0, column=3, columnspan=3, pady=10, sticky='w')
                for i in range(3):
                    lost.columnconfigure(i, weight=1)
                lost.mainloop()
                # lost.destroy()
                final_answer += 1


        else:
            try:
                keys_used.append(key)  # first update the key in database
                keys_left = [key for key in keys_left if key not in keys_used]  # find unique keys based on keys_used
                key = keys_left[1]  # taking the next key for next question
                keys_used.append(key)  # again update the recent used key in database
                question = question_generation(key, select_key)
            except:
                root.destroy()

                lost = Tk()
                lost.title("Desiapp.romrom")
                lost.config(background='lightblue')
                lost.geometry("800x500")

                ourMessage = '"OOPS .. we lost you buddy!! Try Again"'
                messageVar = Message(lost, text=ourMessage, width=500,font=('Helvetica', 30, 'bold'))
                messageVar.config(bg='lightgreen')
                tr_again = Button(lost, text="Try Again!", fg='black', bg='white', width=20)
                exit_button = Button(lost, text="❌", fg='red', width=2, command=lost.destroy)

                messageVar.grid(row=0, column=1, columnspan=1, pady=30, sticky='w')
                tr_again.grid(row=4, column=2, columnspan=3, pady=50, sticky='w')
                exit_button.grid(row=0, column=3, columnspan=3, pady=10, sticky='w')
                for i in range(3):
                    lost.columnconfigure(i, weight=1)
                lost.mainloop()
                # lost.destroy()
                final_answer += 1


    # root.mainloop()
    root.destroy()