
def progress_bar(count_value, total):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '█' * filled_up_Length + ' ' * (bar_length - filled_up_Length)
    print(f'{percentage}%|{bar}|', end="\r")
