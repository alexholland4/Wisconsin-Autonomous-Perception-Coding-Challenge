# Wisconsin Autonomous Perception Coding Challenge - Alex Holland's Solution
This repository contains the code/my solution for the perception team coding challenge on the Wisconsin Autonomous team application.

[Challenge Description](https://github.com/WisconsinAutonomous/CodingChallenges/blob/master/perception/README.md)
 
 
## answer.png
Below is my final "answer.png", the final image produced with OpenCV as specified by the coding challenge description:

Original Image            |  My answer.png
:-------------------------:|:-------------------------:
![Original Image](https://github.com/alexholland4/Wisconsin-Autonomous-Perception-Coding-Challenge/blob/7132ba4b6baad104d500948a0e667701ba5d9267/original.png)  |  ![My Solution Image](https://github.com/alexholland4/Wisconsin-Autonomous-Perception-Coding-Challenge/blob/7132ba4b6baad104d500948a0e667701ba5d9267/answer.png)

## Libraries used
I only used two libraries in my solution: **cv2** (OpenCV), and **NumPy**. 

I used cv2 to allow me to perform the image processing/computer vision tasks necessary for this project - finding the cones, creating the mask, and drawing the lines.

I used NumPy as a way to create arrays to hold to HSV values that I needed to perform color thresholding. I chose to use these arrays as opposed to python lists as NumPy arrays are faster and more compact than Python lists.

## Methodolgy
I began this project by considering a few different ways that I could go about detecting the cones. The first that I considered was an object classification/detection model that could detect a cone, find all of them, and then draw the lines. The second, and solution that I ended up implementing, was a color thresholding approach where, using the fact that the cones had a relatively unique color to the image, to be able to find and classify them. My solution essentially had 4 main sections:
1. Read the image in, and use OpenCV to detect and mask the cones.

In this step, I used OpenCV to read the image in, converted its values to a HSV color space (in contrast to the BGR default), and used color thresholding of the HSV values to draw a mask image. 
```
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([170, 75, 100]) # lower red color threshold
upper_red = np.array([179, 255, 255]) # upper red color threshold
mask = cv2.inRange(hsv, lower_red, upper_red) # creates the mask of the color of the cones
```
2. Using the contours produced by the mask, iterate through them to find the ones highest and lowest in the image on each side.

In this step, I essentially found the top left, bottom left, top right, and bottom right cones. I will later be using these value to draw the line through. To make this implementation more consistent, I defined a region of interest that made up aproximately the bottom 3/4 of the image to eliminate some false positives from the top of the image.

3. Use the positions of the top and bottom cones to do math and determine where the lines would intersect the edges of the image.

Because I want to draw these boundary lines across the entirety of the image, and not simply from the top cones to bottom cones, I must use math to determine where these lines that I want to draw would intersect the edges of the image, and then draw the lines to those points on the edges. To do this, I found the slope/y-intercept that we would have for both the left and right lines, and then just used the dimensions of the image to determine what x/y points the lines would hit on the edge.

4. Draw the lines and write the image to the output file

This step was quite straightforward and only required a few lines of code. I drew each of the two red lines through the points I found in the previous step, over top of the original image, and wrote this final image to answer.png as outlined in the challenge description.
```
final_img = cv2.line(img, point1, point2, (0, 0, 255), 4) 
final_img = cv2.line(img, point3, point4, (0, 0, 255), 4) 
cv2.imwrite('answer.png', final_img)
```

## What I tried and why I think it did not work
From the start, I thought that based on the cones being a relatively unique color to the image, I would be able to simply use color thresholding to isolate/mask them from the image, and then just use the mask/contours to draw a line through them. During this implementation, I ran into a few key issues:
1. The image also had some other objects similar in color to the cones (the couch, the exit signs, the door being illuminated by the light in the back right, etc), so I ran into an issue with false positives when trying to mask the cones. To solve this, I used Trackbars to be able to more accurately shorten the range of the HSV values that the cones represented, as well as implemented a region of interest to eliminate false positives.
2. I initially thought to outline the cone objects using the Canny algorithm, but realized after implementing it that I was actually overcomplicating things for this project by drawing out the edges of the cones, as I actually did not need to do this at all to draw the boundary lines.
3. I also initially thought that I would simply be able to use the cv2.line() method to draw the lines through the top and bottom cones, but quickly found out that this method is only able to draw line segments, not entire lines, and hence I had to do math to find out where these lines would intersect the edges of the picture, and implement this manually. 
4. I finally had some slight issues with the fact that the line method would only let me pass tuples of ints, and not floats, to represnt the locations that I wanted to draw the lines through, and this made the precision of the lines drop a bit. To combat this, I added a slight manual offset to one of the line's points, as the loss of precision was the same every time. 

Overall, by working through each of these issues, I was able to learn more about color thresholding, OpenCV, and image processing as a whole. As a result, I believe my final implementation to be a solution that is understandable, reliable, rigid, and scalable. My solution accurately solves the challenge, and does so in a way that it could theoretically also be implemented to an image with more/changing cones. If I were to work on this further, I would also add support for videos, which because of the way I implemented my code, would essentially be as simple as taking in a video stream instead of an image. 

I greatly enjoyed working on this project and, if given the opportunity, hope to be able to continue working on projects such as this with the perception team of Wisconsin Autonomous. Thank you for your consideration for this role!
