Python Calculator Application Using DevOps
1. Project Overview

This project is a simple Python-based Calculator Application developed using DevOps practices.

The calculator performs basic arithmetic operations such as Addition, Subtraction, Multiplication, Division, Modulus, and Power.

DevOps tools are used to automate testing, manage source code, and containerize the application.

2. Features
Addition
Subtraction
Multiplication
Division
Modulus
Power
Division-by-zero error handling
Automated unit testing
3. Technologies Used
Technology	Purpose
Python 3.12	Application development
VS Code	Code editor
Git	Version control
GitHub	Source code hosting
unittest	Automated testing
GitHub Actions	Continuous Integration
Docker	Containerization
4. Project Structure
text
Calculator-DevOps/
│
├── calculator.py
├── test_calculator.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
│
└── .github/
    └── workflows/
        └── python-app.yml

5. How to Run the Application
Run using Python
bash
python calculator.py

Run automated tests
bash
python -m unittest discover -v

6. Docker Implementation
Build Docker Image
bash
docker build -t python-calculator .

Run Docker Container
bash
docker run -it --rm python-calculator

Run Tests Inside Docker
bash
docker run --rm --entrypoint python python-calculator -m unittest discover -v

7. Automated Testing

The project uses Python unittest framework.

Eight test cases are implemented:

Addition
Subtraction
Multiplication
Division
Division by Zero
Modulus
Power
Negative Number Addition

Expected result: All 8 test cases should pass.

8. CI/CD Pipeline

GitHub Actions is configured to automatically execute unit tests whenever code is pushed to the main branch or a pull request is created.

Pipeline Steps
Checkout source code.
Set up Python 3.12.
Execute automated unit tests.
Display test results.
9. Expected Results
Calculator performs arithmetic operations correctly.
Automated unit tests execute successfully.
GitHub Actions verifies the application.
Docker image builds successfully.
Application runs inside a Docker container.
10. Challenges
Configuring Git and GitHub.
Setting up GitHub Actions.
Resolving Docker Engine startup issues.
Running automated tests inside Docker.
11. Conclusion

The Python Calculator project demonstrates the implementation of DevOps practices in a simple software application.

GitHub is used for version control, unittest for automated testing, GitHub Actions for continuous integration, and Docker for containerization.

This project demonstrates how automation improves software development, testing, and deployment processes.

12. Author

Project: Python Calculator Using DevOps Practices
