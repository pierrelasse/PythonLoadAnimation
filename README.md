
# Why
This "animation" gets often used in linux.
I wanted to make this since there was a funny background that
looked like some crazy hacker something like you see it in movies
that had this loading animation.

So i wanted to make an easy to use function (class) that you can use
to create an animation like this.

# How to use
Just download the loadanim.py file and put it in your project folder.
Then you can import it using `from <filename> import loadanim`.

To create the animation just put the code below wherever you want.
```
from loadanim import loadanim

[...]

loadanim(
    text1 = f"<text when loading> %c",
    text2 = f"<text when done>",

    time = 1,
    wait = 0.05
)
```
