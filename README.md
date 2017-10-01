[![Build Status](https://travis-ci.org/gr1d99/user_class.svg?branch=develop)](https://travis-ci.org/gr1d99/user_class)  [![Code Climate](https://codeclimate.com/github/gr1d99/user_class/badges/gpa.svg)](https://codeclimate.com/github/gr1d99/user_class)  [![Issue Count](https://codeclimate.com/github/gr1d99/user_class/badges/issue_count.svg)](https://codeclimate.com/github/gr1d99/user_class)  ![Coverage](https://github.com/gr1d99/user_class/blob/develop/coverage.svg)

# user_class
Is a project that contains a minimal Python OOP implementation of a `user` class, contributions are welcomed.

## Prerequisites

- Python3 [Installation](https://www.python.org/downloads/)
- Git [Installation](https://git-scm.com/downloads)


## Project setup
- Clone this repo.
  ```bash
    $ git clone https://github.com/gr1d99/user_class.git
  ```
- Change your current directory such that you are inside the cloned project.
  ```bash
    $ cd user_class
  ```
- Create a virtual environment.
  ```bash
  $ virtualenv --python=python3 env
  ```
 
 - Activate the virtual environment.
   ```bash
      $ source env/bin/activate
   ```
 - Install dependencies of the project.
   ```bash
      $ pip install -r requirements.txt
   ```

## Tests
- To run tests you have followed the project setup procedures.
- Testing tools for this project are [coverage](), [nose]() and [pytest]().
- Run tests
  ```bash
    $ py.test
  ```
