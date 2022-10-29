###################################################
#Josue Cifuentes
#CIS 225
#1) Number of errors found:???
#2) Error Types: Syntax Error in first line misspelled authors
#                Syntax Error in seventh line missing () after print
#                Syntax Error in eighth line misplaced the second }
#############################################################
#Program Name: collection.py
# Purpose of a program:
# Create a collection of authors and the years they died using a dictionary.
# Print the collection in the following format:

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

#for key, value in authors.items():
#    print("%s" % key + " died in " + "%s." % value)
for author_date in authors:
    print("%s" % authors + " died in " + "%s." % date)

