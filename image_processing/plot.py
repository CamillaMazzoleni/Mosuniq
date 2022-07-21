import matplotlib.pyplot as plt

###this function is used to show more images at the same time, making a compare of them

def show(img1, img2, img3):
    # create figure
    fig = plt.figure(figsize=(12, 6))

    # setting values to rows and column variables
    rows = 1
    columns = 3


    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, 1)

    # showing image
    plt.imshow(img1)
    plt.axis('off') ##dont show the axis
    plt.title("Original image")
    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, 2)

    # showing image
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Algorithm")

    # Adds a subplot at the 3rd position
    fig.add_subplot(rows, columns, 3)

    # showing image
    plt.imshow(img3)
    plt.axis('off')
    plt.title("Available colors")
    plt.show()