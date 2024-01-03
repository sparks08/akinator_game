import pandas as pd
from colorama import Fore,Style,Back
import requests
from io import BytesIO
from PIL import Image
import cv2
import numpy as np

animals = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri-smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=522745683&single=true&output=csv")
characters = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri-smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=645902942&single=true&output=csv')
appliances = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri-smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=1796877773&single=true&output=csv')
fruits = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri-smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=55564916&single=true&output=csv")
actors = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTiTmNtEVri-smJi4jWa7hqt_PgsQRlNyxMUasSkhR96cWx5MjB0RCbcL2ot3pcIb1FLGLB4G7d0mnz/pub?gid=1357857810&single=true&output=csv')

def akinator_game():
    value = ''
    start = 0
    unique_keys = []
    keys_used = []

    print("Choose any one ..\n")
    print("Character \nAnimal \nAppliance \nFruit \nActor")
    user_choice = str.capitalize(input(""))
    
    if user_choice == 'Character':
        data = characters
        data_key = 'human'
    elif user_choice == 'Animal':
        data = animals
        data_key = 'animal'
    elif user_choice == 'Appliance':
        data = appliances
        data_key = 'appliance'
    elif user_choice == 'Fruit':
        data = fruits
        data_key = 'fruit'
    elif user_choice == 'Actor':
        data = actors
        data_key = 'male'
    else:
        print("Choose from mentioned options.")
    
    def data_filteration(data):
        counts_of_true  = data.iloc[:,2:].sum(axis=0).sort_values(ascending=False)
        count_index = counts_of_true.reset_index()
        count_index.columns =['index', 'values']
        count_index = count_index[count_index['values'] != 0]
        sum_value_count = count_index['values'].max()
        count_index[count_index['values'] != sum_value_count]
        count_index_keys_list = count_index['index'].values
    
        # removing items from countIndex
        keys_left = [key for key in count_index_keys_list if key not in keys_used]
        # key = keys_left[0]     # taking the key for next question
        # update the key 
        # key = key
        # print(Fore.RED +f"Is your character {key}?")
        # return key
        return keys_left

    def question_generation(key, user_choice):
        if user_choice == 'Appliance' or user_choice == 'Fruit':
            print(Fore.RED +f"Is your item {key}?")
        else:
            print(Fore.RED +f"Is your character {key}?")

    def yes_no_correction(option):
        option = str.lower(option)
        if str(option).startswith('y'):
            value = "Yes"
        elif str(option).startswith('n'):
            value = "No"
        else:
            value = "No"
        return value

    def write_text_on_image_from_url(image_url, key_value):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_array = np.array(Image.open(BytesIO(response.content)))
            
            # Convert the image to grayscale
            image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
            resized_image = cv2.resize(image, (600,300), interpolation=cv2.INTER_AREA)
            
            height, width = resized_image.shape[:2]
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            key_on_image_position = (width // 2, 50)
            font_scale = 1
            text_color = (255, 255, 255)
            yes_option_on_image_position = (width // 3, height - 20)
            no_option_on_image_position = (width - width // 3, height - 20)
            
            font_scale = 1
            text_color = (0, 0, 255)  # Red
            
            
            cv2.putText(resized_image, key_value, key_on_image_position, font, font_scale, text_color, 2, cv2.LINE_AA)
            cv2.putText(resized_image, "Yes", yes_option_on_image_position, font, font_scale, text_color, 2, cv2.LINE_AA)
            cv2.putText(resized_image, "No", no_option_on_image_position, font, font_scale, text_color, 2, cv2.LINE_AA)
            
            # plt.imshow(image)
            cv2.imshow("Modified Image", resized_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print(f"Error: Unable")


    final_answer = "No"
    # Question-answer rounds
    while final_answer != 'Yes':
        if start == 0:
            question_generation(data_key,user_choice)
            # print(Fore.RED +f"Is your character {data_key}?")
            key = data_key
            keys_used.append(key)
            start += 1
            
        value = input("Your response: ")
    
        if value == 'y':
            data = data[data[key] == True]
            print(data.name.sort_values().values)
            if data.shape[0] == 1:
                final_value = data.values[0][0]
                final_value_image = data['image'].values[0]
                print(Fore.GREEN +f"I think of\n {str.capitalize(final_value)}")
                write_text_on_image_from_url(final_value_image, str.capitalize(final_value))
                break
                # user_final_response = input("")
                # user_final_response = yes_no_correction(user_final_response)

                # if user_final_response == "Yes":
                #     break
                # else:
                #     break
                    
            keys_used.append(key)
            keys_left = data_filteration(data)
            key = keys_left[0]
            question_generation(key, user_choice)

    
        elif value.startswith('n'):
            data = data[data[key] != True]
            print(data.name.sort_values().values)
            if data.shape[0] == 1:
                final_value = data.values[0][0]
                final_value_image = data['image'].values[0]
                print(Fore.GREEN +f"I think of\n {str.capitalize(final_value)}")
                write_text_on_image_from_url(final_value_image, str.capitalize(final_value))
                break
                # user_final_response = input("")
                # user_final_response = yes_no_correction(user_final_response)

                # if user_final_response == "Yes":
                #     break
                # else:
                #     break
            
                # break
            keys_used.append(key)    # update the key
            keys_left = data_filteration(data)   # finding keys to be used for question in each filtered data
            key = keys_left[0]     # taking first key for generating question
            question_generation(key, user_choice)   

        else:
            print(data.name.sort_values().values)
            keys_used.append(key)          # first update the key in database
            keys_left = [key for key in keys_left if key not in keys_used] # find unique keys based on keys_used
            key = keys_left[1]   # taking the next key for next question
            keys_used.append(key)   # again update the recent used key in database
            question_generation(key, user_choice)
            
akinator_game()