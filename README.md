# 3-dimensional "Monte Carlo" method to approximate Pi
*My contribution to the Pi-Day 2022*

##  Demonstration
https://i.imgur.com/4j4lNz3.mp4

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

$$
A_{\text{circle}} = \pi r^2
$$



Applying this logic to every dart in the square (and the circle, because the circle is in the square) 
we can just use the formula for the area of a square which would in this case be:

$$
A_{\text{square}} = (2r)^2 = 4r^2
$$


So if we would now calculate the ratio between the area of the circle (points in the circle) and the area 
of the square (all points), we'd get this:

$$
\text{ratio} = \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi r^2}{4r^2} = \frac \pi 4
$$


Now lets rearrange this formula with a multiplication by 4 so that pi is isolated:

$$
\pi = ratio * 4
$$


Remember the 3 darts from earlier? We can use the above formula now to approximate pi:

$$
\frac{2 \text{ points in the circle}}{3 \text{ total points}} * 4 = 3.0
$$


### Bringing it to the third dimension

If you understood the basics of the "Monte Carlo" method, bringing it to the third dimension is fairly easy. 
Instead of a circle and a bounding square, imagine their three-dimensional counterparts, a sphere and a cube.

![](https://user-images.githubusercontent.com/87434959/158021973-91aa0b22-113a-47d1-9c88-82b214346d57.png)

Now we can use the formulas for the volume of a sphere and for the volume of a cube to calculate the ratio between these:

$$
\text{ratio} = \frac{V_{\text{sphere}}}{V_{\text{cube}}} = \frac{\frac 43 \pi r^3}{(2r)^3} = \frac{4 \pi r^3}{24r^3} = \frac{\pi}6
$$


Applying this to an example with 2 points inside the sphere and 4 points in total we get:

![](https://i.imgur.com/V1RhtqE.png)

$$
\pi = \text{ratio} * 6 = \frac{2 \text{ points in the sphere}}{4 \text{ total points}} *6 = 3.0
$$
