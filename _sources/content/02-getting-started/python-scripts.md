# Writing and Running Python Scripts

**Pre-requisite**: You should have finished the [command line](/02-getting-started/commandline.md) guide.

In the previous section, we learned how to use the Python interpreter to run Python code interactively. While this is useful for testing small pieces of code, it is not practical for writing and running large programs. In this section, we will learn how to write Python scripts and run them from the command line.

## Writing Python Scripts

A Python script is a file containing Python code. You can write Python scripts using any text editor, such as Notepad (Windows), TextEdit (Mac), or Visual Studio Code. What makes a file a Python script isn't the program you use to write it - it's the file extension. Instead of ending in `.txt` or `.docx`, a Python script's file name ends in `.py`. That `.py` ending is a signal - to Python and to other programmers - that the file contains Python code.

To create your first Python script, follow these steps:

1. Open your command line (Powershell on Windows; Terminal on Mac or Linux).

2. Navigate to the directory where you want to store your script. This is a great chance to practice the commands you just learned! For example, you could create a new directory and then move into it:

```
mkdir python_practice
cd python_practice
```

3. Create a new file called `first_script.py`:

```
touch first_script.py
```

````{admonition} Using Windows Powershell? Click here!
:class: dropdown

As noted in the command line section, `touch` is not a built-in command in Windows Powershell. If you get an error, use Powershell's `New-Item` command instead:

```
New-Item first_script.py
```
````

4. Open the file you just created in your text editor and type in the following code:

```python
print('Hello, World!')
print('This is my first Python script!')
```

5. Save the file. That's it - you've written a Python script!

A quick note on naming your scripts: use short, descriptive, all-lowercase names, separating words with underscores (`_`) rather than spaces (for example, `first_script.py`, not `First Script.py`). File names with spaces in them are a pain to work with on the command line, so programmers avoid them.

## Running Python Scripts

Now for the fun part - running your script! From the command line, make sure you are in the same directory as your script (`pwd` and `ls` can help you check), then type the following and press `Enter`:

```
python first_script.py
```

You should see the following output:

```
Hello, World!
This is my first Python script!
```

When you run this command, you are asking the Python interpreter to open your file and execute the code inside it, line by line, from top to bottom. Once the last line has been run, Python exits, and you are returned to your command prompt.

**Note**: On some machines (particularly Macs), you may need to type `python3` instead of `python`. If one doesn't work, try the other!

### Scripts are not interactive

There is one important difference between a script and the interactive interpreter. In the interpreter, when you typed `2 + 2` and pressed `Enter`, Python displayed `4` right away. In a script, Python only displays what you explicitly tell it to `print`. To see this for yourself, go ahead and add the following two lines to the end of `first_script.py`, save the file, and run it again:

```python
2 + 2
print(2 + 2)
```

The first line runs - Python calculates the sum - but nothing is displayed. The second line prints `4` to your command line. Keep this in mind as you start writing scripts: if you want to see it, `print` it.

## Scripts, the Interpreter, & Jupyter Notebooks

At this point, you've now seen three different ways to run Python code, and each has its place:

- **The interpreter** is great for quick, throwaway calculations and testing small pieces of code. Nothing is saved, so when you close the window, your code is gone.

- **Scripts** are files, so your code is saved, can be run again and again, and can be shared with others. Scripts are how most Python programs out in the world are written and run.

- **Jupyter notebooks** combine code, text, and output in a single document, which makes them wonderful for learning, exploring data, and sharing your thinking alongside your code.

Throughout the rest of this book, we will primarily use Jupyter notebooks. But, everything you learn in the chapters that follow works exactly the same in a Python script, so you can always take your code from a notebook and put it in a script - something you may find yourself doing more and more as your programs grow!
