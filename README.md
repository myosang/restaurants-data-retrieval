# Intro
This project shows how to get and filter the first 10 data entries from API endpoint of the Just Eat Takeaway UK restaurants.

# Assumptions
1. The provided API is publicly accessible and doesn't require the authentication or there is a strict rate limit in request.
2. The API supports the standard REST API grammars and support HTTP GET request.
3. No official API documentation is provided, so the response structure is inferred from the returned JSON format.
4. The target user of this project is the developers, who would like to use this project as a prototype for data retrieval using API. Therefore, correctness of data and run efficiency is prioritized.
# How to run
1. Install the necessary libraries. If using pip, type the following in command line.
```
pip install -r requirements.txt
```
2. Run main script in command line.
```
python3 main.py
```
3. Expected output will show in command line.
# How to test
1. You need 'pytest' library which is already installed if you followed the procedure how to run.
2. Run following in the command line.
```
pytest
```
# Design choice and Architecture
Headers and API call is defined in api script, and parser for getting data and filtering is defined in parser script. Orchestration happens in main script. Display happens in the command line for the run efficiency. 

# Challenges and Solution Approach
1. Purpose of this project was not clear which made it difficult to define the scope and complexity. I defined the target user of this project as described in assumptions section, then it became clear to prioritize parts.
1. Getting the data without the API key was new to me, I searched the reason why my 'get' request is access denied (status code: 403). The reason was not giving the correct headers and I collected the values from endpoint in web browser using DevTools in Chrome.
2. I learned how to build the test script. Previously I did run the tests but they were not developed by me so it was a learning experience to build unit test and define the scope/edge case of it.
3. Choice of data display method between command line and web interface was on a debate. I focused on the scope of this coding exercise, which doesn't give a weights on the display interface therefore, run efficiency is prioritized than building a strong frontend.
4. It was not clear whether a postcode should be given as user input or not, however, I chose to provide a postcode in the code, since the instruction expected candidates to choose single postcode. Making the user input function can overcomplicate the project.
# Improvement
If the scope of the project is extended,
* The function to allow the user inputs and multiple endpoints with different postcode can be implemented. 
* Also, data can be displayed in separate web interface for better user experience. If the returned data should become an input of other function, data completeness can be checked and only return the instances with complete fields (e.g., if 'rating' is missing, then skip this instance and return the next one). 
* Save ouput to files such as csv can be also implemented if the data should become an input of other function or shared for dashboard creation of business' team. 

# Use of AI
I used AI - ChatGPT Go version -as an assistant.

* Debugging: When API get request or pytest initial run was not successful, I copy-pasted my code and Error message to find failure reason and break points.
* Boiler Plate: Using new libraries such as rich and pytest, I asked for code snippet to start implementation.
* Requirements and syntax check: Before the finalizing project, I double checked the codes by giving the coding exercise instructions and my codes to check whether there's no missing requirements or syntax error.
* Readability: Enhanced the readability for README.md by asking AI to make it easy-reading and grammatically correct.