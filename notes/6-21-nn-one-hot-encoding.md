# Encoding

*One Hot Encoding* is part of pre-preprocessing when it comes to AI. Encoding is a way to change data to a format that makes it easier to process. There are different ways of encoding data with more formal methods like *Label Encoding* or *One Hot Encoding*. 

## Label Encoding

Label Encoding is basically just changeing a text field to numeric. For example, different categories such as type of car or breed of animal where each distinct category is given a numeric value.

The problem with Label Encoding is that the numerical categories that are assigned to each class are ordered. Computers naturally treat higher order numbers as higher numbers. That is to say, it will give higher numbers more weight.

*Imagine if you had 3 categories of foods: apples, chicken, and broccoli. Using label encoding, you would assign each of these a number to categorize them: apples = 1, chicken = 2, and broccoli = 3. But now, if your model internally needs to calculate the average across categories, it might do do 1+3 = 4/2 = 2. This means that according to your model, the average of apples and chicken together is broccoli.* 

## One Hot Encoding



### Sources

 https://medium.com/@michaeldelsole/what-is-one-hot-encoding-and-how-to-do-it-f0ae272f1179 