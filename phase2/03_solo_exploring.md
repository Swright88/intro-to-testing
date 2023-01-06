# Exercise - Exploring (Part 1)

These sections are solo pieces of work, where you will use the processes in
previous sections to set up then run an exploratory testing session on some
functionality or applications.

## Application

For this exercise, you will be testing a sample sign-up web form. Specifically,
one field in that form - the email address field.

You've probably encountered numerous web forms with optional and mandatory
fields, some of which are checked to see whether they are unexpectedly blank
(and need to be filled in) or don't conform to some set of pre-defined rules
(and they need to be modified).

In this sample sign-up form, someone has implemented email address validation
and the stakeholder for the product to which this sign-up form relates wants to
know more about how it's working before it goes live!

Frankly, you've heard rumblings from various people that the validator is in a
bit of a bad state at the moment, so you're expecting to find some problems and
you're expected to be reporting back on what works and what doesn't to the
concerned stakeholder.

## Location

[Resources for this exercise](03_resources).

One way to open the form is to browse to the folder on disk, then double-click
`myform.html` to open that in your default browser.

## Steps

Work through each of the steps below in turn, using what you learned earlier
about exploratory testing. The timings given are just suggestions - you should
choose how long you want to spend on each section, noting you should give
yourself 1 hour for this exercise at most.

1. Read up on what it is you're going to explore - that's the Application as
   written above (max 5 minutes)
2. Think about what you're going to test, how and why (e.g. 20 minutes)
    * Decide how to divide your time i.e. how long you want to spend planning,
      exploring then writing things up
    * Read up on email address syntax and think about what's considered to be
      acceptable or unacceptable; for example,
      https://en.wikipedia.org/wiki/Email_address#Syntax has some details
    * Start writing down some email addresses that you might want to test -
      perhaps your own could be the first on a "valid" list (don't worry -
      you're not accidentally signing up to anything in reality!)
    * Consider how you might group the email address ideas you already have -
      perhaps they're all valid ones at the moment (and you need some invalid
      ones as well) or perhaps you're currently focusing on what's written
      before the "@" symbol
    * Write up some top-level categories of your email address ideas, then break
      each of those down (and break those down again if appropriate) - there's
      an example of this, below; you don't have to follow this exact pattern -
      there are no single correct approach
    * Lastly, come up with email addresses for the ideas on your broken-down
      "tree" of areas and categories

Perhaps you start with:
```
- valid cases
- invalid cases
```

Then work on expanding the valid cases category first:
```
- valid cases
  - before "@"
  - after "@"
- invalid cases
```

And a bit further on one of those:
```
- valid cases
  - before "@"
    - letters
    - digits
    - special characters
    - [...]
  - after "@"
- invalid cases
```

And so on. You could then add email addresses for each of the "letters",
"digits" and "special characters" broken down areas, for example.

3. Use the email addresses you've prepared to explore the sign-up web form (e.g.
   20 minutes)
    * Write notes as you go! What have you tried, what did it show / what was
      the outcome, etc?
    * Be guided by your instincts and what you find - you don't have to
      rigorously stick to the email addresses you generated before; remember,
      you are exploring and learning about it as you go
    * When you find behaviour that looks wrong, try to determine what's the most
      simplistic and easy to understand email address that demonstrates the
      observation
4. Write up a report on what you did and what you found (e.g. 10 minutes)
    * This doesn't need to be a formal report, but imagine this is something you
      would email to the stakeholder who wants to know more about the email
      validation
    * Think about what's important to the stakeholder - what do they need to
      know? How could you get that information across clearly and concisely?

[Next Challenge](04_notes_and_mindmaps.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F03_solo_exploring.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F03_solo_exploring.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F03_solo_exploring.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F03_solo_exploring.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase2%2F03_solo_exploring.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
