# Tools

Before we go any further, let's briefly introduce the tools we'll be using throughout the book.

## Python

**Python** is a programming language, whose development is led by the [Python Software Foundation](XXX). The official Python organization website is [https://www.python.org].

Python - and most programming languages - are updated over time. As changes are made, these updates are released to the public. In this book, we assume that everyone has either **Python 3.6 or 3.7**. Now, if you have an older version, a lot of this content will apply. If you have a newer version, most of this content should work perfectly fine!

Python comes with what is referred to as the **standard library**. This includes a set of packages available by default with every python install. However, there is an extensive ecosystem of third party packages. In this book, we'll rely almost exclusively on the standard library; however, we'll introduce some helpful third party packages toward the end of the book. 

## Jupyter Notebooks

When it comes to programming, there are *many* different ways in which you can approach learning. Here, we take a notebook-based approach. People who have been programming for a while will have an opinion about this approach - some people think they're a great learning tool; others think notebooks confuse new programmers. In my experience, teaching primarily students who are *not* interested in becoming software engineers, but who will instead use code for end-user programming (to carry out analyses, generate visualizations, etc.), notebooks are a great tool from which to learn. 

As such, we're going to use **[Jupyter](http://jupyter.org/) notebooks** throughout. In fact, most chapters of this book (any where code is presented) will be written in Jupyter notebooks. These notebooks are then compiled into the book you're reading. The reason notebooks are helpful is because they provide a way to intermix code, the output from the code, and plain text. This allows for code to be right alongside the needed explanation of that code. 

In the next chapter, we'll introduce the ins-and-outs of Jupyter Notebooks.

## Anaconda Distribution

If you do not already have python and Jupyter notebooks downloaded, we'll want to do that now. The easiest way to do that is to [download the **Anaconda** distribution](https://www.anaconda.com/download/). This includes python and its standard library *and* additional external packages that we will introduce and use toward the end of the book.

Note that if you are using a Mac you have a native installation of Python. However, this installation could be out-of-date and will not include the extra packages we'll use toward the end of the course. When you install Anaconda, a separate independent installation of Python will be installed, leaving your native install untouched.

If you are on Windows or Unix machine, Python will typically *not* be pre-installed. 
