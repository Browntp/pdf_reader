import random


"""
Need to split the file into chunks, each chunk being texts from the pdf of random length between 400 and 600 characters. 
"""

def split_string(text):
    character_amnt = len(text)
    min_random = 400
    max_random = 600
    random_number = random.randint(min_random, max_random)
    max_gpt_requests = character_amnt/random_number
    list_of_strings = []
    requests = 0

    while requests <= max_gpt_requests:
        requests += 1
        min_cutoff = (requests - 1) * random_number
        max_cutoff = requests * random_number
        final_str = text[min_cutoff:max_cutoff]
        if requests + 1 >= max_gpt_requests:
            final_str = text[min_cutoff:]
            list_of_strings.append(final_str)
            break
        list_of_strings.append(final_str)
    return list_of_strings
        