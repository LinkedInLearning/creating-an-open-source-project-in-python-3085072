# Create an Open-Source Project in Python
This is the repository for the LinkedIn Learning course Create an Open-Source Project in Python. The full course is available from [LinkedIn Learning][lil-course-url].

![Create an Open-Source Project in Python][lil-thumbnail-url] 

For open-source projects, it can be a challenge to ensure development coherence and avoid errors and bugs. In this course, Python community leader Cheuk Ting Ho guides you through the complete process of starting, building, testing, and maintaining an open-source project in Python. Cheuk introduces you to Poetry, a popular dependency management tool, and shows you how to use it in starting a Python project. She defines pytests and goes over how to write simple tests, test with multiple parameters, and test if an exception is raised. Cheuk covers fixtures and how to use them, as well as when it is okay to skip a test. She discusses using PEP 8, Black, linters like Flake8, and pre-commits to tidy up your code. Cheuk demonstrates how to use a tool called tox to standardize your testing, as well as how to set up a workflow on GitHub Action. Plus, she highlights some best practices for open-source projects.



## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

Cheuk Ting Ho 
                            


                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/cheuk-ting-ho).

[lil-course-url]: https://www.linkedin.com/learning/create-an-open-source-project-in-python?dApp=59033956&leis=LAA
[lil-thumbnail-url]: https://media.licdn.com/dms/image/C560DAQEh8rkWx4V2MQ/learning-public-crop_675_1200/0/1680032934598?e=2147483647&v=beta&t=ZyBS874h-9xHgvfC94nSfZcladv4Uz01ctcNk0UWJoY
