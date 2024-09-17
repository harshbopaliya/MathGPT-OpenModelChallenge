# 📄 Model Submission Details

- Welcome to the **MathGPT-OpenModelChallenge**! Below are the guidelines for submitting your models to the platform. Please ensure that you follow these instructions carefully to avoid submission errors and ensure compatibility with our system.

---

## 🎯 Model Submission Guidelines

- Your model should adhere to the following structure for input/output to ensure it can be evaluated correctly by the platform.

### 1. **Input Format**
- The input to the model will be a JSON object representing the mathematical problem. Example:

```json
{
  "problem": "integrate x^2 dx"
}
```
- problem: A string representing the mathematical problem. This could be an algebraic equation, calculus problem, or other types of mathematical queries.

### 2. **Output Format**
- The model must return a JSON object containing the solution to the problem. Example:

```json
{
  "solution": "x^3 / 3 + C"
}
```
- solution: A string representing the solution to the mathematical problem.


### 3. **Error Handling**
- If the model encounters an invalid input or cannot solve the problem, it should return an error response in the following format:

```json
{
  "error": "Invalid input or unsolvable problem"
}
```
- error: A string describing the nature of the issue.


#### 4. **Model Interface**
- Your model should include a single function (e.g., solve_problem) that takes the input JSON and returns the output JSON.

```python
def solve_problem(problem_json):
    # Extract the problem from the input JSON
    problem = problem_json.get("problem")

    # Perform the calculation or solution
    solution = perform_calculation(problem)

    # Return the solution in the required format
    return {"solution": solution}
```

## 🚀 Steps for Model Submission
1. Step 1: Fork the Repository
Fork the MathGPT-OpenModelChallenge repository on GitHub.
Clone your forked repository to your local machine:

``` bash
git clone https://github.com/<your-username>/MathGPT-OpenModelChallenge.git
```

2. Step 2: Develop Your Model
- Implement your model following the structure and input/output format described above.
Your model should be able to read the JSON input, process the mathematical problem, and return the correct solution in JSON format.

- Test your model locally using the provided test dataset (/data/sample_problems.json).

3. Step 3: Create a README.md for Your Model
- Your submission should include a README.md file that explains:
- Your approach and methodology.
- Any specific frameworks, libraries, or tools you used.
- Instructions on how to run the model locally (dependencies, environment setup, etc.).

4. Step 4: Submit a Pull Request (PR)
- Once you are satisfied with your model, commit your code to your forked repository.
- Create a Pull Request (PR) to the main repository.
- The PR should include:
- Your model code (placed in the models/ directory).
- The README.md with details about your model.
- Any other supporting files needed to run your model.

5. Step 5: Automatic Testing
Once your PR is submitted, the platform will automatically:

Run your model against a set of mathematical problems.
Rank it based on its accuracy, speed, and efficiency.
You can check the results on the Leaderboard.

## 📦 Directory Structure for Submission
Your submitted model should follow the directory structure below:

```bash
MathGPT-OpenSource/
├── models/
│   └── your_model.py         # Your model code
│   └── README.md             # Description of your model
├── data/
│   └── sample_problems.json   # Sample problems for local testing
└── test_model.py              # Script to locally test your model
```

## 📊 Evaluation Criteria
Your model will be evaluated based on three key criteria:

Accuracy: Does the model return correct solutions to mathematical problems?
Speed: How quickly does the model return a solution?
Efficiency: How much computational power (CPU/memory) does the model consume?



## 🛠 Local Testing
Before submitting, ensure that your model works locally by using the sample dataset provided. To test your model:

Install the dependencies from requirements.txt:

``` bash
pip install -r requirements.txt
```
Run the local test script:

```bash
python test_model.py
```
This will evaluate your model on a few sample problems to ensure it meets the platform's requirements.

## 🤝 Contributions and Support
If you encounter any issues or have suggestions, feel free to open an issue on GitHub or contact the project maintainers at demo@gmail.com.

We look forward to seeing your innovative solutions!