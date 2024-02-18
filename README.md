# Mosuniq - The Mosaic Robot

The purpose of my project was to automate the process of creating mosaics by developing a software tool that can process images into a mosaic image and then designing and building a machine that is capable of picking and placing tiles to recreate it. This  project involved different disciplines, like informatics, statistics, mechanics, electronics and control system.
I developed a library in Python of an optimized clustering algorithm to process the image and designed an efficient and cost-effective mechanical system in Solidworks. The project also included the electrical design, schematics and PCBs for the control of mechanical components.

## General Framework
The customer uploads an image and the process automatically starts: the image is processed in Python, using machine learning algorithms to analyze the image and to select the best matching colors from the available tile set. The processed image, represented as a string of colors is then passed through serial comunication to Arduino, which dictates the movement of the mechanical system and the positioning of the tiles on a self-adhesive mesh of 50x50 cm. The mosaic is then ready to be trasported and it will be then installed on site, putting fresh tile grout on it.
![General workflow](Images)

