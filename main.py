# Import statements
import cv2
import numpy as np

# Loads the input image
img = cv2.imread('original.png')

# Converts the image to HSV color space and performs color thresholding
# This step essentially allows us to isolate the color of the cones, and therefore isolate/mask the cones.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([170, 75, 100]) # lower red color threshold
upper_red = np.array([179, 255, 255]) # upper red color threshold
mask = cv2.inRange(hsv, lower_red, upper_red) # creates the mask of the color of the cones


# Finds the contours in the mask image - essentially finds all the locations on the image of where the mask says the cones are at
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# Defines a rectangular region of interest - cones are not on the top portion of the image so we should not look there for them
roi_x = 0  # x-coordinate of the top-left corner of the region
roi_y = 0   # y-coordinate of the top-left corner of the region
roi_width = 1816  # width of the region that we do want
roi_height = 604 # height of the region that we do not want

# Variable declarations that will hold y values of coordinates of top and bottom cones to draw line through
bottomLeftY = 1816 # max Y 
topLeftY = 0 # minimum Y
bottomRightY = 1816 # max Y 
topRightY = 0 # minimum Y

# Variable declarations that will hold x values of coordinates of top and bottom cones to draw line through
bottomLeftX = 0 
topLeftX = 0
bottomRightX = 0 
topRightX = 0

# We iterate over the contours (cone locations) and find the contour points within the region of interest 
# Here, we look for the contours with both the highest and lowest Y values within the region of interest
# When we find these, we keep track of their x and y values, as these represent the coordinates where
# we want to draw our line through
for contour in contours:
    for point in contour:
        x, y = point[0]  # Extract the x and y values of the point
        # We take the left and right halves of the images separately to allow us to draw both lines
        if (x >= roi_x and x < roi_width/2) and (y >= roi_height): # left half of the image
            if(y<bottomLeftY): # if currently lowest cone of the left side
                bottomLeftY = y
                bottomLeftX = x
            if(y>topLeftY): # if currently highest cone of the left side
                topLeftY = y
                topLeftX = x
        if (x >= roi_width/2 and x < roi_width) and (y >= roi_height): # right half of the image
            if(y<bottomRightY): # if currently lowest cone of the right side
                bottomRightY = y
                bottomRightX = x
            if(y>topRightY): # if currently highest cone of the right side
                topRightY = y
                topRightX = x

# We now have the highest and lowest cone coordinate on both the left and right sides of the image
# Now, we do math to determine where the line that passes through these cones would hit the edge of the image
# We do this in order to have the lines drawn across the entire image, not just through the cones.

# Slope and y-intercept of left line
leftSlope = (topLeftY - bottomLeftY) / (topLeftX - bottomLeftX)
leftY_intercept = topLeftY - (leftSlope * topLeftX)
# Left line coordinates of where the line hits the edges of the image
bottomLeftEdgeX = int(1) #far left of image
bottomLeftEdgeY = int(leftY_intercept)
topLeftEdgeY = int(1)  # top of image
topLeftEdgeX = int((topLeftEdgeY - leftY_intercept) / leftSlope)

# Slope and y-intercept of right line
rightSlope = (topRightY - bottomRightY) / (topRightX - bottomRightX)
rightY_intercept = topRightY - (rightSlope * topRightX)
# Right line coordinates of where the line hits the edges of the image
bottomRightEdgeX = int(1816)
bottomRightEdgeY = int(rightY_intercept) #int((rightSlope * bottomRightEdgeX) - rightY_intercept)
topRightEdgeY = int(1) # top of image
topRightEdgeX = int((topRightEdgeY - rightY_intercept) / rightSlope) + 20 # slight manual offset to account for floating point error

# Points for both lines to be used to draw the lines
point1 = (bottomLeftEdgeX, bottomLeftEdgeY)
point2 = (topLeftEdgeX, topLeftEdgeY)
point3 = (bottomRightEdgeX, bottomLeftEdgeY)
point4 = (topRightEdgeX, topRightEdgeY)

final_img = cv2.line(img, point1, point2, (0, 0, 255), 4) # draw first line on orignal image 
final_img = cv2.line(img, point3, point4, (0, 0, 255), 4) # draw second line on original image to give final answer image
cv2.imwrite('answer.png', final_img) # write the final image to the file as specified in challenge directions

# Uncomment these last three lines if you want to see the resulting image immediately when running
# Display the final resulting image with the red lines:

#cv2.imshow('Result', final_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


