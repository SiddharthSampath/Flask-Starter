
def get_dict_tuples(k_v_pair, key_list, same_var_names=True):

    if same_var_names:
        return tuple(k_v_pair.get(key) for key in key_list)
    else:
        values = []
        for item in key_list:
            values.append(k_v_pair.get(item))
        return values

