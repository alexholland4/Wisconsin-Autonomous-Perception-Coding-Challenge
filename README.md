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

I used NumPy as a way to create arrays to hold to HSV values that I needed to perform color thresholding. I chose to use these as opposed to python lists as NumPy arrays are faster and more compact than Python lists.

## Methodolgy
I began by 

## What I tried and why I think it did not work
From the start, I thought that based on the cones being a relatively unique color to the image, I would be able to simply use color thresholding to isolate/mask them from the image, and then just use the mask/contours to draw a line through them. During this implementation, I ran into a few key issues:
1. The image also had some other objects similar in color to the cones (the couch, the exit signs, the door being illuminated by the light in the back right, etc), so I ran into an issue with false positives when trying to mask the cones. To solve this, I used Trackbars to be able to more accurately shoten the range of the HSV values that the cones represented.
2. I initially thought to outline the cone objects using the Canny algorithm, but realized after implementing it that I was actually overcomplicating things for this project by drawing out the edges of the cones, as I actually did not need to do this at all to draw the boundary lines.
3. I also initially thought that I would simply be able to use the cv2.line() method to draw the lines through the top and bottom cones, but quickly found out that this method is only able to draw line segments, not entire lines, and hence I had to do math to find out where these lines would intersect the edges of the picture, and implement this manually. 
4. I finally had some slight issues with the fact that the line method would only let me pass tuples of ints, and not floats, to represnt the locations that I wanted to draw the lines through, and this made the precision of the lines drop a bit. To combat this, I added a slight manual offset to one of the line's points, as the loss of precision was the same every time. 
