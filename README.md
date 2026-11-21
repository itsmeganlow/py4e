# py4e: learning Python from scratch

Hi, I'm Megan. I spent four years in commercial roles at Kimberly-Clark and Changi Airport Group, and in September 2026 I started learning to code, with the goal of becoming an AI engineer.

This repo is where I work through **Python for Everybody** (University of Michigan, Coursera). Everything in `course1/` and `course2/` is code I wrote myself as I went, sometimes with hints when I was stuck.

## What's inside

| Folder | Topic | What I practised |
| --- | --- | --- |
| `course1/` | Programming for Everybody (completed) | Variables, conditionals, `try`/`except`, functions, loops: pay calculator, grade checker, largest/smallest number |
| `course2/ch06/` | Strings | Indexing, slicing, string methods |
| `course2/ch07/` | Files | Opening files, reading them line by line, pulling values out of text |
| `course2/ch08/` | Lists | `split()`, building lists from a text file |
| `course2/ch09/` | Dictionaries | Counting with `dict.get()`, finding the most frequent item |

## Two I'm proud of

- **`course2/ch07/ch07_graded_assign_7.2.py`**: reads a real email log, finds every `X-DSPAM-Confidence:` line, pulls out the number and averages it across the file.
- **`course2/ch09/ch09_graded_assign_9.1.py`**: counts how many emails each sender sent using a dictionary as a tally sheet, then finds the most active sender.

## What I learned (usually by getting it wrong first)

- **A file handle isn't the file's contents.** `open()` gives you a way in; you still have to loop through it or call `.read()`.
- **Where a line sits changes everything.** Inside vs outside a loop, above vs below a `continue`: this was my most common bug.
- **`find()` gives a position, not the value.** Slice from that position, then convert with `float()`.
- **Counters start at zero before the loop** and get added to inside it.
- **`dict.get(key, 0) + 1`** is a tally sheet: look up the current count, add one, save it back.

## How to run

Each chapter folder includes the sample data files it needs.

    cd course2/ch09
    python3 ch09_graded_assign_9.1.py
    # press Enter to use mbox-short.txt

## What's next

Course 2 Chapter 10 (tuples), then pandas and SQL, then a data project on the Olist eCommerce dataset: exploring 100K orders and building a model to predict delivery delays.

I track my progress and mistakes in Notion, and use Claude as a study partner on a "hints first, not answers" rule.