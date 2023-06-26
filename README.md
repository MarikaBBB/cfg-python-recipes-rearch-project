# CFG Recipe Search Project

A recipe search program that uses Python and the Edamam API to find and print recipes according to the user's chosen ingredient(s) and other search criteria, including preferred cuisine type (e.g. British, Italian, Indian), dietary requirements (e.g. vegan, vegetarian, gluten-free), and maximum calories.

This project was presented alongside Sharmila Soudiah Rajendran and Laura Jimenez Hernandez as part of our final group project for the Code First Girls 8-week Introduction to Python Programming course (December 2022 - January 2023).

Requirement: Sign up at Edamam API for app id and key.

### What was the original plan for the project?
#### Required Tasks
Read the Edamam API documentation https://developer.edamam.com/edamam-docs-recipe-api

- Ask the user to enter an ingredient that they want to search for
- Create a function that makes a request to the Edamam API with the required ingredient as part of the search query (also included your - Application ID and Application Key
- Get the returned recipes from the API response

#### Ideas for Extending the Project
- Save the results to a file
- Order the results by weight or another piece of data
- Ask the user additional questions to decide which recipe they should choose
- Cross-reference the ingredient against the Edamam nutrition analysis API
- Use a different searchable API (suggestions in useful resources)


### What does the project actually do?
The code asks the user to input an ingredient that they want to search for. The research for the requested ingredient is through the Edamam API for which we created a function called run(). The user can choose to filter the research by answering further questions. The result will appear on the interface as a list of 10 recipes ordered by kcal in ascending order. This list is saved on a CSV file and if the user wants to search for a second ingredient this can be added to the previously saved research in the CSV file.

 
### One thing that you learned during the project
Lambda 
function https://realpython.com/python-lambda/ https://www.educative.io/answers/how-to-sort-a-list-of-tuples-in-python-using-lambda

Zip()
https://www.programiz.com/python-programming/methods/built-in/zip

Slicing a list(nested list or list of tuples)
https://www.geeksforgeeks.org/how-to-iterate-through-a-nested-list-in-python/

join() function
https://pythonbasics.org/join/ 
https://www.geeksforgeeks.org/python-string-join-method/

Sorting
https://docs.python.org/3/howto/sorting.html 
https://www.educative.io/answers/how-to-sort-a-list-of-tuples-in-python-using-lambda

os.path.isfile() method
https://www.geeksforgeeks.org/python-os-path-isfile-method/amp/

While loop
https://realpython.com/python-while-loop/

### A brief explanation of an interesting piece of code in the project: End of code and while loop
- While loop allows the user to search for new recipes ( with a new ingredient).
- If the user replies 'yes' to the question  ̈Would you like to search for something else), then the condition of the if statement is satisfied.
- Within this 'if' statement we call the function read_recipe_from_file. This allows the user to input a new ingredient and quickstart the search process.
- The results of the second ingredient ( the second list of recipes) will be appended to the pre-existing list of recipes ( in the CSV file).
- If the user does not want to search for another ingredient, the else part of our while loop prints the pre-existing results reading from the CSV file.

 
### A difficult part of the project that you solved
Merged all the pieces of code from the team in the main code project. Understand how other teammates worked on their tasks.
While loop for 1. Continue searching and 2. Exit Application
Write outputs in a user-friendly format (using tabulate)

### What would you do if they had more time on the project?
Cross-reference the ingredient against the Edamam nutrition analysis API Ask more questions to the user but in the form of multiple choice
Include pictures of the recipes



