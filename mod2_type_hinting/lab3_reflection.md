# Lab3 Reflection
## Vienna LaRose

1. Can you access _name directly using channel._name outside the class?
    Yes I can access _name directly using channel._name outside of the class because this method of "protecting" an attribute is just a convention. This tells the programmer not to make changes to this, but the code itself doesn't see a difference and has no embeded error system to detect changing a "protected" attribute. 


2. Can you access __video_count directly using channel.__video_count? What exception (if any) is raised? How can you access it using name mangling? Show the syntax and test it in main().
    When trying to access __video_count directly I raise an AttributeError in my code.

    To use name mangling I just have to know that python internally changes the name of this attribute to be _YouTubeChannel__video_count. As you will notice that makes it just like my _name attribute, meaning it can be accessed outside of my class when I call it using the new name that python automatically assigns to it. 