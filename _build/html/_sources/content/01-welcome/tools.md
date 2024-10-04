# Tools

Before we go any further, let's briefly introduce the tools we'll be using throughout the book.

## Python

### What is Python

**Python** is a programming language, whose development is led by the [Python Software Foundation](XXX). The official Python organization website is [https://www.python.org].

Python - and most programming languages - are updated over time. As changes are made, these updates are released to the public. In this book, we assume that everyone has either **Python 3.6 or 3.7**. Now, if you have an older version, a lot of this content will apply. If you have a newer version, most of this content should work perfectly fine!

### Why Python

![Python XKCD Comic](https://imgs.xkcd.com/comics/python.png)

Python, if the above comic did not excite you already, is one of the most versatile and easy to learn programming language that exists today. Lets consider another popular introductory language, Java.

If I were to create a [Hello World](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) program in Java, it would look something like this:

```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

After you've written this in a file, lets call it `HelloWorld.java`, open a terminal(macOS) or terminal(windows), then run the following commands:

```
javac HelloWorld.java
java HelloWorld
```

Now on your terminal, you would see the message `Hello, World!`.

Now, lets consider the same program in Python:

```
print("Hello, World!")
```

After you've written this in a file, lets call it `HelloWorld.py`, open a terminal(macOS) or command prompt(windows), then run the following command:

```
python HelloWorld.py
```

Yet again, you would see the message `Hello, World!`.

The difference in the amount of code required to print a simple message is staggering. This is one of the reasons why Python is so popular. It is easy to learn and easy to read (it is also potentially easier to install but more on that soon!).

Additionally, Python is one of the most versatile programming languages. It is used in a variety of fields, including web development, data science, machine learning, and artificial intelligence. Learning Python enables you to explore a variety of applications and opens up numerous career opportunities. Whether you want to build websites, analyze data, create intelligent systems, or develop cutting-edge technologies, Python provides a solid foundation to pursue your goals. Its simplicity, readability, and extensive library ecosystem make it a popular choice among developers worldwide.

Python comes with what is referred to as the **standard library**. This includes a set of packages available by default with every python install. We will be focus on these packages within this book and will explore some others in the later chapters.

## Jupyter Notebooks

When it comes to programming, there are _many_ different ways in which you can approach learning. Here, we take a notebook-based approach. People who have been programming for a while will have an opinion about this approach - some people think they're a great learning tool; others think notebooks confuse new programmers. In my experience, teaching primarily students who are _not_ interested in becoming software engineers, but who will instead use code for end-user programming (to carry out analyses, generate visualizations, etc.), notebooks are a great tool from which to learn.

As such, we're going to use **[Jupyter](http://jupyter.org/) notebooks** throughout. In fact, most chapters of this book (any where code is presented) will be written in Jupyter notebooks. These notebooks are then compiled into the book you're reading. The reason notebooks are helpful is because they provide a way to intermix code, the output from the code, and plain text. This allows for code to be right alongside the needed explanation of that code.

In the next chapter, we'll introduce the ins-and-outs of Jupyter Notebooks.

## Anaconda Distribution

If you do not already have python and Jupyter notebooks downloaded, we'll want to do that now. The easiest way to do that is to [download the **Anaconda** distribution](https://www.anaconda.com/download/). This includes python and its standard library _and_ additional external packages that we will introduce and use toward the end of the book.

Note that if you are using a Mac you have a native installation of Python. However, this installation could be out-of-date and will not include the extra packages we'll use toward the end of the course. When you install Anaconda, a separate independent installation of Python will be installed, leaving your native install untouched.

If you are on Windows or Unix machine, Python will typically _not_ be pre-installed.
