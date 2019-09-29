def sort_high_scores(high_score_file, current_score, player_name, add_entry_flag = False):
    """
    Desc:
        Opens, potentially adds a new entry, and writes sorted high scores.
    
    Input:
        high_score_file = path to high_score_file
        current_score = to be used, if adding a new entry
        player_name = to be used, if adding a new entry
        add_entry_flag = if set to True, add a new entry
    
    """
    with open(high_score_file, "r") as high_scores:
        all_scores = [entry.split() for entry in high_scores]
    
    if add_entry_flag:
        new_entry = []
        new_entry.append(str(current_score))
        new_entry.append(player_name)
        all_scores.append(new_entry)
    
    # Sorts all_scores in decreasing order.
    all_scores.sort(reverse=True)

    # Clears the high_score_file
    open(high_score_file, "w").close()
    
    # Writes the updated high_scores in high_score_file
    with open(high_score_file, "a+") as high_scores:
        for i in range(len(all_scores)):
            line_to_add = str(all_scores[i][0]) + " " + str(all_scores[i][1]) + "\n"
            high_scores.write(line_to_add)
    # print(all_scores)

def add_current_score(high_score_file, current_score, player_name):    
    sort_high_scores(high_score_file, current_score, player_name, add_entry_flag=True)
        



high_score_file = "high_score.txt"
player_name = "Test"
add_current_score(high_score_file, 5000, player_name)

