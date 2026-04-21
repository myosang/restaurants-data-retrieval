# 📖 Introduction
This project demonstrates how to retrieve restaurant data from the Just Eat Takeaway UK API and extract the first 10 restaurant entries. The data is filtered to include only relevant fields and displayed in a structured format.
# 🧠 Assumptions
1. The API is publicly accessible and does not require authentication or has no strict rate limits.
2. The API follows standard REST conventions and supports HTTP GET requests.
3. No official API documentation is provided, so the response structure is inferred from the returned JSON.
4. The target users are developers who want a simple prototype for API-based data retrieval. Therefore, correctness and simplicity are prioritized over building a complex interface.
# 📂 Project Structure
```
main.py          # Orchestration (API call → parsing → display)
api.py           # Handles API requests
parser.py        # Extracts and transforms restaurant data
display.py       # Handles console output (Rich table)
tests_parser.py  # Unit tests for parsing logic
requirements.txt
```
# 🚀 How to run
1. Install dependencies:
```
pip install -r requirements.txt
```
2. Run the application:
```
python3 main.py
```
3. The output will be displayed in the console.
# 🧪 How to test
1. Install dependencies (includes pytest):
```
pip install -r requirements.txt
```
2. Run tests:
```
pytest
```

# 🔧 Design choice and Architecture
The project follows a simple separation of concerns:
* API layer (`api.py`): Handles HTTP requests
* Parsing layer (`parser.py`): Extracts and formats required data fields
* Display layer (`display.py`): Presents data in a readable format using a console table
* Main (`main.py`): Coordinates the workflow

The console-based interface was chosen to keep the solution lightweight and focused on data processing rather than frontend development.

# 🔥 Challenges and Solution Approach
### 1. Unclear scope
The task description was open-ended, especially regarding the interface. I defined the target user as a developer and focused on building a clean, functional prototype.
### 2. API access (403 error)
Initial requests failed due to missing headers.
I resolved this by inspecting browser requests (Chrome DevTools) and replicating required headers.
### 3. Writing unit tests
I had prior experience running tests but not creating them.
This project helped me understand:
* how to structure unit tests
* how to define edge cases (e.g., missing fields)
### 4. Choosing display methods
I considered both web and console interfaces. Then I chose a console-based solution to keep the implementation simple and focused on the core requirement: data retrieval and display.
### 5. Postcode input 
It was unclear whether user input was required.
I used a fixed postcode to align with the instruction but designed the code so it can be easily extended to accept user input.
# 📈 Improvement
If the project were extended:

* Allow user input for postcode and support multiple queries
* Add a web interface for better user experience
* Filter out incomplete data entries (e.g., missing rating)
* Export results to CSV for further analysis or reporting
* Improve project structure with dedicated folders for scalability
# 🤖 Use of AI
I used ChatGPT as an assistant during development:

* Debugging: Helped identify issues with API requests and test execution
* Boiler plate: Provided initial code snippets for libraries like Rich and pytest
* Validation: Checked requirements coverage and syntax before submission
* Readability: Improved clarity and grammar of this README