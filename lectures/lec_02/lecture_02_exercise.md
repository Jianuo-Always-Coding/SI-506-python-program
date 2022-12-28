# SI 506 lecture 02

## Terminal/VS Code in-class exercise

### Directory structure

From your home directory `/Users/< your account name >` (macOS) or `c/Users/< your account name >`
(Windows) you will create the following directory structure to hold SI 506 content.

```commandline
Documents/
    umich/
        courses/
            SI504/
            SI506/
                assignments/
                    le_01
                    ps_01
                lectures/
                    lec_02/
                        lecture_02_exercise.md
                        lecture_02.md
                        study_time.py
```

## 1.0 Open terminal

Open `Terminal.app` (macOS) or `Git Bash` (Windows). The terminal session should start in your
home directory (confirm with `pwd`).

:bulb: `Terminal.app` (macOS) can be found in `Applications/Utilities`.

## 2.0 Terminal: command line exercise

### 2.1 Challenge 01

1. Print the working (i.e., current) directory path.

2. List the directory contents (long format) including all hidden files.

3. Clear the screen.

4. Navigate (i.e., change) to the `~/Documents` directory.

5. List the directory contents (long format) including all hidden files.

6. Create a directory named `umich`.

7. Navigate to the `umich` directory.

8. Create a subdirectory named `courses`.

9. Create a subdirectory named `courses/SI506`.

10. Create a sibling subdirectory named `courses/SI504`.

### 2.2 Challenge 02

1. Navigate to the `courses/SI504` directory.

2. Oops. Navigate to the "adjacent" `SI506` directory.

3. Create a subdirectory named `lectures`.

4. Create a sibling subdirectory named `assignments`.

5. Create a sibling subdirectory named `notes`.

6. Oops. Remove directory named `notes` (don't need it).

7. List the directory contents of the `SI506` directory (long format) including all hidden files.

8. Navigate to the `lectures` directory.

9. Create a subdirectory named `lec_02`.

10. Navigate to the `assignments` directory.

11. Create a subdirectory named `le_01`.

12. Create a subdirectory named `ps_01`.

### 2.3 Challenge 03

1. Navigate to the `~/Downloads` directory or other directory location where you downloaded today's
   lecture files.

2. Copy `lecture_02.md` from `Downloads` (or other location) to the `lec_02` directory created
   previously.

3. Copy `lecture_02_exercise.md` from `Downloads` (or other location) to the `lec_02` directory
   created previously.

4. Copy `study_time.py` from `Downloads` (or other location) to the `lec_02` directory created
   previously.

5. Navigate to the `lec_02` directory employing _a single command_ to traverse the
   directory path.

6. List the directory contents (long format) including all hidden files.

7. Check the Python version that your terminal session recognizes.

8. Check the Python install location.

9. Print a list of environment variables that govern your terminal session.

10. Clear the screen.

11. Run `study_time.py` from the terminal. Respond to the request for input by providing a numeric
    value that represents the number of hours that you plan to devote to weekly readings,
    assignments, Slack conversations, and office hour visits.

### 2.4 Challenge 04

Open VS Code.

1. Navigate `SI506` folder (_File -> Open..._).

2. Create a Workspace (_File -> Save Workspace As..._). Save `SI506.code-workspace` file in the
   `SI506` directory.

3. Create new folder `lab_exerise_01` in the `si506/assignments` folder.

4. Create new folder `problem_set_01` in the `si506/assignments` folder.

5. Open `study_time.py` in editor pane.

6. Click the triangular run button (upper right) and start a terminal session. `study_time.py` will
   prompt you for input in the terminal pane.

FINIS
