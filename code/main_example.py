'''Module 3: count black and white pixels and compute the percentage of white pixels in a .jpg image'''

from termcolor import colored
import cv2
import numpy as np
import pandas as pd

# Image filenames
filenames = [
    r"/Users/megansullivan/Desktop/Comp BME/Sullivan-Hayden-Module-3-Fibrosis/images/MASK_SK658 Slobe ch010136.jpg",
    r"/Users/megansullivan/Desktop/Comp BME/Sullivan-Hayden-Module-3-Fibrosis/images/MASK_SK658 Slobe ch010129.jpg",
    r"/Users/megansullivan/Desktop/Comp BME/Sullivan-Hayden-Module-3-Fibrosis/images/MASK_SK658 Slobe ch010119.jpg",
    r"/Users/megansullivan/Desktop/Comp BME/Sullivan-Hayden-Module-3-Fibrosis/images/MASK_Sk658 Llobe ch010032.jpg",
    r"/Users/megansullivan/Desktop/Comp BME/Sullivan-Hayden-Module-3-Fibrosis/images/MASK_SK658 Slobe ch010113.jpg",
    r"/Users/megansullivan/Desktop/Comp BME/Sullivan-Hayden-Module-3-Fibrosis/images/MASK_SK658 Slobe ch010107.jpg",
]

# Depths corresponding to each image
depths = [9200, 3250, 8000, 200, 7300, 6300]

white_percents = [] # IMPROVEMENT: Only store the values we actually need

print(colored("Counts of pixel by color in each image", "yellow")) # Print a header for the output

# IMPROVEMENT: Use zip() instead of range(len(...)) indexing
# This makes the loop cleaner and avoids unnecessary indexing.
for filename, depth in zip(filenames, depths): # Loop through each filename and corresponding depth

    # Load image in grayscale
    img = cv2.imread(filename, 0) 

    # Convert to binary
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Count pixels
    # IMPROVEMENT: Process each image immediately instead of storing all images first
    white = np.sum(binary == 255)
    black = np.sum(binary == 0)
    # IMPROVEMENT: Compute total once instead of repeating calculation
    total = white + black

    white_percent = 100 * white / total
    white_percents.append(white_percent)

    # Print results
    print(colored(f"{filename}", "red"))
    print(colored(f"White pixels: {white}", "white"))
    print(colored(f"Black pixels: {black}", "black"))
    print(f"{white_percent:.2f}% White | Depth: {depth} microns\n")

# Save results to CSV
df = pd.DataFrame({
    "Filenames": filenames,
    "Depths": depths,
    "White percents": white_percents
})

df.to_csv("Percent_White_Pixels.csv", index=False) # Save the DataFrame to a .csv file without the index

print("The .csv file 'Percent_White_Pixels.csv' has been created.") # Print a message confirming that the .csv file has been created


##############
# LECTURE 2: UNCOMMENT BELOW

# # Interpolate a point: given a depth, find the corresponding white pixel percentage

# interpolate_depth = float(input(colored(
#     "Enter the depth at which you want to interpolate a point (in microns): ", "yellow")))

# x = depths
# y = white_percents

# # You can also use 'quadratic', 'cubic', etc.
# i = interp1d(x, y, kind='linear')
# interpolate_point = i(interpolate_depth)
# print(colored(
#     f'The interpolated point is at the x-coordinate {interpolate_depth} and y-coordinate {interpolate_point}.', "green"))

# depths_i = depths[:]
# depths_i.append(interpolate_depth)
# white_percents_i = white_percents[:]
# white_percents_i.append(interpolate_point)


# # make two plots: one that doesn't contain the interpolated point, just the data calculated from your images, and one that also contains the interpolated point (shown in red)
# fig, axs = plt.subplots(2, 1)

# axs[0].scatter(depths, white_percents, marker='o', linestyle='-', color='blue')
# axs[0].set_title('Plot of depth of image vs percentage white pixels')
# axs[0].set_xlabel('depth of image (in microns)')
# axs[0].set_ylabel('white pixels as a percentage of total pixels')
# axs[0].grid(True)


# axs[1].scatter(depths_i, white_percents_i, marker='o',
#                linestyle='-', color='blue')
# axs[1].set_title(
#     'Plot of depth of image vs percentage white pixels with interpolated point (in red)')
# axs[1].set_xlabel('depth of image (in microns)')
# axs[1].set_ylabel('white pixels as a percentage of total pixels')
# axs[1].grid(True)
# axs[1].scatter(depths_i[len(depths_i)-1], white_percents_i[len(white_percents_i)-1],
#                color='red', s=100, label='Highlighted point')


# # Adjust layout to prevent overlap
# plt.tight_layout()
# plt.show()
