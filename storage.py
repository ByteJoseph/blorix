import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
# def fixed_max_storage(unit):
#     switch = {
#         'B': "Bytes - Smallest unit of data.",
#         'KB': "Kilobytes - Often used for small files.",
#         'MB': "Megabytes - Used for medium-sized files.",
#         'GB': "Gigabytes - Suitable for large files like videos.",
#         'TB': "Terabytes - Massive storage capacity for servers."
#     }
    # return switch.get(unit, "Unknown unit!")
def used_storage():
    max_bytes = 1073741824
    used_bytes = get_directory_size(os.getcwd())
    used_storage = format_size(get_directory_size(os.getcwd()))
    used_percentage = round((used_bytes/max_bytes)*100,2)
    #used_percentage = 56
    return used_storage,used_percentage


#print(get_directory_size(os.getcwd()))