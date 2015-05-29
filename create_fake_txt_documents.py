import os, random, requests

# constants
num_files = 10
words_in_file = 700
line_lengh = 10
vocab_size = 10000

unique_words = set()

# get words
word_site ="http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
word_list = response.content.splitlines()
ignore_word_file = "ignore_words.txt"
ignore_words = open(ignore_word_file).read().splitlines()

# create list of words to pull from when writeing files
words = random.sample(word_list, vocab_size)

# create directory
directory = "./{}_files_for_test".format(num_files)

if not os.path.exists(directory):
    os.makedirs(directory)
else: # remove all files recreate directory
    import shutil
    shutil.rmtree(directory)
    os.makedirs(directory)

def reset(percent=20):
    return random.randrange(100) < percent

# create files in directory
for i in range(num_files):
    with open(directory + "/{}.txt".format(i + 1), 'w') as f:
        for i in range(words_in_file):

        # create newlines
        if ((i+1) % line_lengh) == 0:
            f.write("\n")
        #create paragraphs
        if reset():
            f.write("\n")

        # write  word to file
        word = random.choice(words).decode("utf-8")
        f.write(" " + word)
        if word not in ignore_words:
            unique_words.add(word)

        # write text file with total number of unique words in all other files
        with open("./unique_words_in_{}_file_run.txt".format(num_files), 'w') as f:
            f.write(str(len(unique_words)) + \
                " unique words in {} files".format(num_files))
