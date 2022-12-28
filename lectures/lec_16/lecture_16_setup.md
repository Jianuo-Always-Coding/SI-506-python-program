# SI 506 Lecture 16 setup

## 1.0 Get files

Lecture files are available in Canvas Modules and Canvas Files. Download the files to your
`~/Downloads` directory.

## 2.0 Copy/move lecture files using the terminal

:exclamation: if you have yet to create the suggested SI 506 directory structure see Appendix A
below. If you opt for your own directory structure you will need to adjust the paths listed below
accordingly.

1. Open your terminal (either Terminal.app or Git Bash)
2. Issue the following terminal commands:

``` commandline
cd Downloads
mkdir ../Documents/umich/courses/SI506/lectures/lecture_16/
cp lecture_16_setup.md lecture_16.md lecture_16.py whc-sites-2022.csv ../Documents/umich/courses/SI506/lectures/lecture_16/
cd ../Documents/umich/courses/SI506/lectures/lecture_16/
ls
```

The above commands perform the following operations:

1. Change directory from your home directory to `~/Downloads` directory.

   :bulb: recall that `~/` is shorthand for your home directory.

2. Create a new subdirectory directory in your SI 506 `lectures` directory named `lecture_16`.

3. Copy (`cp`) the downloaded files to the `lecture_16` directory.

   :bulb: You can copy the files one at a time but that’s less efficient.

   :exclamation: You can also move (`mv`) the files but the copy operation is safer in the sense that
   if you move the files to the wrong target directory, you will have to figure out where you moved
   them, then change directories, and move them from their new location. I recommend that you
   copy (`cp`) the files rather than move them. If you accidently copy the files to the wrong
   directory, you can reissue the the copy command again from your `~/Downloads` directory with
   an updated path.

4. Navigate (`cd`) to your `lecture_16` directory.

5. Confirm "that the contents of the `lecture_16` directory are as expected (i.e., it contains
   copies of today’s lecture files).

## 3.0 VS Code

Open your SI 506 workspace in VS Code.

:exclamation: If VS Code does not open your SI 506 workspace, click the blue "Open folder" button
and navigate to your `~/Documents/umich/courses/SI506` directory.

1. Hover over `lecture_16.md`, right-click, and select "Open Preview".
2. Hover over `lecture_16.py`, right-click, and select "Open to the Side".
3. Click on the files icon in the left-side activity bar to close the file viewer pane.

:exclamation: If you have yet to create a VS Code "workspace" now would be a good time to do so.
Click on _File -> Save Workspace As..._ and change the default filename from
`workspace.code-workspace` to `SI506.code-workspace`. Make sure you save the file to
your `~/Documents/umich/courses/SI506` directory.

## Appendix A. SI 506 directory structure

From your home directory `/Users/< your account name >` (macOS) or `c/Users/< your account name >`
(Windows) create the following directory structure to hold SI 506 content.

```commandline
Documents/
    umich/
        courses/
            SI506/
                assignments/
                lectures/
```

Issue the following commands from the terminal:

```commandline
mkdir -p Documents/umich/courses/SI506/assignments/
mkdir -p Documents/umich/courses/SI506/lectures/
cd Documents/umich/courses/SI506/lectures/
```

:bulb: the `mkdir` `-p` command option or flag will create all required intermediate directories on
the specified path.
