# This code is merely one possible solution because we didn't specify details about the implementation of the functions in the processor module. 
# As long as the process_numbers() and process_names() functions fulfill the requirements in the previous unit, you're successful.

def process_numbers(unprocessed_list):
    
    processed_list = []
    if isinstance(unprocessed_list, list) == False:
        return processed_list
    
    for item in unprocessed_list:
        if isinstance(item, int):
            processed_list.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                converted_item = int(item)
                processed_list.append(converted_item)
    
    processed_list.sort()
    return processed_list


def process_names(unprocessed_list):
    
    processed_list = []

    if isinstance(unprocessed_list, list) == False:
        return processed_list
    
    for item in unprocessed_list:
        if isinstance(item, str):
            if item.isnumeric() == False:
                processed_list.append(item)
    
    processed_list.sort()
    return processed_list