def get_max_length(s):
    if not s:return 0
    cur_len = 0
    max_len = 0
    cur_list = []
    for x in s:
        cur_len += 1
        if x in cur_list:
            while x in cur_list:                
                cur_list.pop(0)
                if len(cur_list)+1 > max_len:max_len = len(cur_list)+1
            cur_list.append(x)
        else:            
            cur_list.append(x)
            if len(cur_list) > max_len:max_len = len(cur_list)
    return max_len
