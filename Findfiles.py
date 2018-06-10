import os
from datetime import datetime
base_list = ['doc', 'docx', 'xls', 'xlsx', 'pdf']

###################################################
############ Creating folder for files ############
###################################################
now = datetime.now()
datetime = str("%02d:%02d:%02d") % (now.hour, now.minute, now.second)
shell_mkdir = "mkdir ./search_"
file_location = shell_mkdir + datetime
os.system(file_location)

print ''' ***This script is to locate files of specific types on a computer running Linux***

print Do you want to add more extensions to the base list?
The current list is:
'''

for base_list in base_list:
    print('.' + base_list)

print '''
Type "1" to add more
Type "2" to keep the base extension list
'''
new_items = []
add_extension_selection = raw_input('Your selection: ')
if add_extension_selection == '1':
    print '''Enter each file extension that you want to look for. When you are done type "done".'''
    add_to_array = "1"
    while add_to_array != 'done':
        add_to_array = raw_input('What is the file extension to add? Do not add the ".": ')
        new_items.append(add_to_array)
        print(new_items)
    else:
        new_items.pop()
        print 'Current extensions:'
        print base_list

elif add_extension_selection == '2':
    print "Using only the base list"
    pass
elif add_extension_selection == '':
    print 'no selection - Using the base list'
    pass

base_list = ['doc', 'docx', 'xls', 'xlsx', 'pdf']
merge_list = base_list + new_items

print "Starting to look for items of the selected file extensions - This could take a while"

for merge_list in merge_list:
    print merge_list
    print_to_file = "./" + "search_" + datetime + "/" + merge_list + ".txt"
    find_interpolation = ("find / -type f -name *.'%s'") % (merge_list)
    combined_ptf_fi = find_interpolation + ">" + print_to_file
    os.system(combined_ptf_fi)



print '''

Look in the directory of which the script was launched. There is a folder called "search_%s" in the directory where the script is, which contains a list of the files with the extensions requested.''' % (datetime)
