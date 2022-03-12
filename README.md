# 3-dimensional "Monte Carlo" method to approximate Pi
*My contribution to the Pi-Day 2022*

##  Demonstration
https://youtu.be/STZtSVNZxlg

The program uses SM3DWFRPG (Super Minimal 3D Wireframe Renderer in Pygame) you can't find the documentation to that [here](about:blank)

## Try it yourself!

1. Clone the repository or download the source code

2. As the `pygame` pygame package is mandatory to launch the program you have to install that using e. g. `pip install pygame`.

3. To launch the program run `sphere_and_cube.py`


## The maths behind it

It looks quite cool thats for sure. But how does it actually work? Why does the ratio between 
all points and the points in the sphere times 6 equal pi? I'm going to answer all of that here.

### The "Monte Carlo" method

Imaging you are playing darts. You have a dart board and a bounding square behind it.

![](https://i.imgur.com/KYp3yO1.png)

So now, let's throw 3 random darts.

![](https://i.imgur.com/P2slYHZ.png)

As we can see, the 2 darts on the board are coloured green and the one outside is cyan. 
So now, let's imagine you are throwing infinitely many darts on this board (or the bounding square).

![](https://i.imgur.com/PUXyE7F.png)

Now the whole area of the board if covered in green and the rest in cyan. So we can say that the 
amount of all darts in the circle if equal to the area of the circle which has the formula:

![](https://i.imgur.com/YSJPtOl.png)

Applying this logic to every dart in the square (and the circle, because the circle is in the square) 
we can just use the formula for the area of a square which would in this case be:

![](https://i.imgur.com/MuWQb6y.png)

So if we would now calculate the ratio between the area of the circle (points in the circle) and the area 
of the square (all points), we'd get this:

![](https://i.imgur.com/KNBWlep.png)

Now lets rearrange this formula with a multiplication by 4 so that pi is isolated:

![](https://i.imgur.com/ps2qF6G.png)

Remember the 3 darts from earlier? We can use the above formula now to approximate pi:

![](https://user-images.githubusercontent.com/87434959/158021245-4fe9d787-65cf-4cd5-ada2-c4a8101e2718.png)


### Bringing it to the third dimension

If you understood the basics of the "Monte Carlo" method, bringing it to the third dimension is fairly easy. 
Instead of a circle and a bounding square, imagine their three-dimensional counterparts, a sphere and a cube.

![](https://user-images.githubusercontent.com/87434959/158021973-91aa0b22-113a-47d1-9c88-82b214346d57.png)

Now we can use the formulas for the volume of a sphere and for the volume of a cube to calculate the ratio between these:

![](https://user-images.githubusercontent.com/87434959/158024061-34c91fd5-f6f3-4857-a36b-8b7f6f2c254a.png)

Applying this to an example with 2 points inside the sphere and 4 points in total we get:

![](https://i.imgur.com/V1RhtqE.png)

![](https://user-images.githubusercontent.com/87434959/158024354-79c0e5dd-d768-459c-9fa8-82eebd982d4b.png)


