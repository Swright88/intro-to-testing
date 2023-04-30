# Challenge - Exploring (Part 2)

Like the previous exercise, this is a solo piece of work. For this challenge,
you will submit materials so your coach(es) can provide feedback.

## Introduction

During test-driven development, a developer would create unit tests individually
before implementing code that passes them each in turn. Sometimes testers find
themselves with only a program description or a more formal specification from
which to work, whilst the developer is writing unit tests and implementing code
to pass them, before a more fully-functional program is passed to the tester for
review.

In this challenge, you should time-box your work at each of the different
stages, deciding what you think is appropriate for each stage. For the recorded
submission of your exploratory testing (more details on that recording are
written below), you should **spend no more than 1 hour**.

### Planning Testing

Using approaches from test-driven development - thinking through examples of how
a program might be used and what it might produce - you will plan out a set of
test cases to exercise a program's functionality, based on a program description
alone. You should try to think of test cases that cover a range of different
ideas and potentially problematic situations. By thinking through your own given
inputs and what you might expect the outputs to be, you will create examples you
can test to see how the program behaves, to help determine if you think what
it's doing is an issue or not.

N.B. your test cases will almost never be "complete" or "perfect" but they are
there to give you a starting point from which to explore the program.

### Reporting Testing

Remember that you should be taking notes while you are exploring and running
tests, so that you can summarise the testing after the session is complete.

The process for this - note-taking during testing and reporting after testing -
is mostly the same as you've done in previous exercises. In this challenge,
along with your test report, you will also write up one bug report. You should
choose the most interesting observation you've made that you believe to be a
problem, and fill out any details which you think might be important to include
in a bug report (hint: consider your audience(s)!).

## Challenge

This is a process feedback challenge. That means you should record yourself
doing it and submit that recording to your coach for feedback. [How do I do
this?](../pills/process_feedback_challenges.md)

In this hypothetical scenario, a program description was written up and provided
to a developer who is writing the code and unit tests. You will work from the
same description and produce test cases while the code is in development, in
order to plan some of your work. Once the code becomes available, you will use
your test cases to explore the developer's program, noting any issues you
observe. At the end, you will record your findings so that they can be passed
back to the team for review.

1. Read through the program description below, making your own notes as you go
2. Prepare 5 different test cases - an example test is shown below the program
   description; don't worry, you're not looking for "perfection" when doing
   this, just giving yourself examples you can use later
3. Start recording your challenge work at this point - record for a **maximum of
   1 hour**
4. Acquire the developer's program, available alongside this file
5. Run the developer's program, using your test cases to explore its behaviour,
   making notes as you test; N.B. you are not limited to only running the 5 test
   cases you prepared, they are starting points for you to begin exploring
6. Stop the recording
7. Summarise your findings by writing up a report including what you found with
   your test cases and a one-line summary of each of the issues observed
8. Choose one of the issues and write a paragraph or two explaining it in more
   detail, and include this in your report
9. Submit your recording, test cases and report

Remember: you are not supposed to be implementing the program!

[After you're done, submit your recording, test cases and
report](https://airtable.com/shrNFgNkPWr3d63Db?prefill_Item=itt_as01).

### Program Description

A "wrap_it" program must take a quantity of English text and add new lines to it
so that it subsequently conforms to having no more than a maximum number of
characters on every line, and has a special marker "--END OF FILE--" denoting
the end of the output. For example, with an input of "a quick brown fox jumps
over the lazy dog" and a maximum wrapping limit of 26, the output would be:

```
a quick brown fox jumps
over the lazy dog
--END OF FILE--
```

The first line of the output above has 24 characters, so is below the limit. The
next word, "over", and subsequent words are moved onto a new line. This second
line is also below the limit and is everything left from the input text, so the
special marker is output after that.

The program therefore takes two inputs - a string of the text to be wrapped and
an integer representing the maximum wrapping limit. It outputs text to the
console.

The program is run at the command line, as shown in the following example, with
the first argument as the wrap limit, followed by the text:

```
$ python3 wrap_it.py 26 "a quick brown fox jumps over the lazy dog"
a quick brown fox jumps
over the lazy dog
--END OF FILE--
```

### Location

[Resources for this exercise](05_resources).

> Please don't open the file to read the code. The idea of this exercise is that
> you're testing it _without_ knowing how it has been implemented.

### Example Test

The following is an example of how you should write your test cases. Test cases
can take many forms, but you should follow this layout for the 5 you create for
this challenge.

```
Test purpose:

See whether the example in the program description produces the output it says it should

Text input:

a quick brown fox jumps over the lazy dog

Wrap limit:

26

Expected output:

a quick brown fox jumps
over the lazy dog
--END OF FILE--
```

[Next Challenge](06_materials.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F05_solo_exploring_more.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F05_solo_exploring_more.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F05_solo_exploring_more.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F05_solo_exploring_more.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F05_solo_exploring_more.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
