# Name: Nafiz Ahmed

# Defining histogram function
def histogram(image): # creates and returns a histogram of a grayscale image.
    counter = 0 # Will see how many times a value appears
    newlist = []
    for h in range(256):    # from 0 to 255
        for i in image:
            for j in i:
                if j == h:
                    counter += 1
        newlist.append(counter)
        counter = 0 # reset the counter
    return newlist

# Defining flip function takes flips images either horizontally or vertically
def flip(image, orientation):
    index = 0
    template = [] # Will be used to append a copy 
    if orientation == 'horizontal':
        for i in range(len(image)):
            template = [] # will reset the template
            for j in range(len(image[i])-1, -1, -1): # start from end
                template.append(image[i][j])
            for value in range(len(template)):
                image[index][value] = template[value] # Template to original
            index += 1
    if orientation == 'vertical':
        copy = image[::-1]  # reverses the list and assigns it to 'copy'
        for i in range(len(image)):
            image[i] = copy[i]  # set the index of copy equal to original
                                # which allows for in place modification
# Defining the rotate function
def rotate(image):
    image[::-1] = image # reverses the list
    value = 0 # value of the value in the iteration
    if image != []: # cant be empty list
        for i in range(len(image)):
            for j in range(len(image[i])):
                value = image[i][j] # The current iteration value
                
                if j > i: # This is because the first value isn't changed
                    image[i][j] = image[j][i]   # set that value as the 
                    
                    image[j][i] = value # make sure the other value changes

# Defining the crop function that returns a cropped tile 
# out of a color image without altering the input in any way.
def crop(image, origin, height, width):
    final = [] # The list I will return
    start = image[origin[0]][origin[1]] # The origin of the list, the start
    for i in range(origin[0], origin[0] + height): # sets boundaries for rows
        template = []
        for j in range(origin[1],origin[1] + width): # boundaries for columns
            template.append(image[i][j]) # put in my list so I can append
        final.append(template)
    
    return final

# Defining the color2gray function
def color2gray(image):
    final = []
    avg = 0
    for i in range(len(image)):
        template = []   # resets the list 
        for j in range(len(image[i])):
            avg = sum(image[i][j]) // len(image[i][j]) # computes average
            template.append(avg)
        final.append(template)  # puts what is in template in final
    return final

# Define extract layer function
def extract_layer(image, color):
    final = []
    for i in range(len(image)):
        template = []   # resets the list
        for j in range(len(image[i])):
            if color == 'red': # conditionals depending on color
                template.append(image[i][j][0])
            if color == 'green':
                template.append(image[i][j][1])
            if color == 'blue':
                template.append(image[i][j][2])
        final.append(template) # put template in final
    return final

# Defining the scale function
#def scale(image, factor):
# I could't figure out how to do it

# Defining the compress function
def compress(image):
    final = []
    for i in range(len(image)):
        total = 0 # Counter, will get appended after counting
        template = [] # used to collect the matchings for one list
        compare = True # Be used to compare with value
        value = None # Used to check which color and allows for differentiating
        for j in range(len(image[i])):
            if image[i][j] < 128:  # If it is black
                value = True
            else:
                value = False
            if value == compare: # Did the same color match?
                total += 1
            else:
                compare = value # allows for counting
                template.append(total) # enters the accumulated total
                total = 1
        template.append(total)
        final.append(template)
        
    return final

# Defining the median filter function
def median_filter(image):
    final = [] # List that will get appended
    if image != []:
        for i in range(len(image) - 2):# iterate only first two rows for 3x3s
            mvalue = [] # Will collect the medians
            for j in range(len(image[i]) - 2):# Iterates only first two columns 
                                                                    #for the 3x3s
                template = [] # Will get the 3x3 lists
                for k in range(0,3): # Finds which row must iterate through
                    for l in range(0,3): # Finds which column must iterate through
                        template.append(image[i + k][j + l]) # [row][column] 
                template.sort() # least to greatest
                mvalue.append(template[4]) # 4th index will always be the median
                                            # since list is always a len of 9
            final.append(mvalue)  # Appends the median value for each 3x3 list
    return final




