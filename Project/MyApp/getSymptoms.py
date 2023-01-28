import operator
import pandas as pd


def is_in(full_str, sub_str):
    if operator.contains(full_str, sub_str):
        return 0
    else:
        return -1


def feed_back_choice(input_info_from_user): # input: skin, pain

    """
    get the input from users and give them possible choices to choose of symptoms.
    :param input_info_from_user: user type the keywords of symptoms in the blank (type: list,separate with comma)
    :return: possible/suggested choices of symptoms from the database.
    """
    testing_file = pd.read_csv("Testing.csv")
    testing_file = testing_file.drop(['prognosis'], axis=1)
    symptoms = list(testing_file.columns)

    symptom_list = []
    for name in symptoms:
        symptom_list.append(name.replace('_', ' '))

    input_list = input_info_from_user.split(',')

    # provide possible choices of symptoms to the users to choose.
    feedback_choice = []
    for input_sym in input_list:
        for symptom in symptom_list:
            if is_in(symptom, input_sym) == 0:
                feedback_choice.append(symptom)
    return feedback_choice, symptom_list


def get_symptoms(input_choices_from_user, symptom_list):
    """
    pass the symptom choices to the decision tree.
    :param input_choices_from_user: symptom choices (type: list,separate with comma)
    :param symptom_list: all symptoms from the database. to form the matrix of symptoms
    :return: matrix passed to decision tree.
    """
    chose_symptom = input_choices_from_user.split(',')
    final_input = pd.DataFrame(columns=symptom_list, index=[1]).fillna(0)
    for i in chose_symptom:
        for column in final_input.columns:
            if i == column:
                final_input[column] = 1
    symptom = []
    for name in symptom_list:
        symptom.append(name.replace(' ', '_'))
    final_input.columns = symptom
    return final_input


### Using of the functions
# feedback_choice, symptom_list = feed_back_choice(input_info_from_user)
# final_input = get_symptoms(input_choices_from_user, symptom_list)

