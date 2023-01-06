# Exercise - Analysis (Part 1)

These sections are pair pieces of work, where you will use the approaches and
ideas from previous sections to analyse some specified functionality or
applications, then work out what you would want to do during an exploratory
testing session.

In the real world, planning test activities (while developers are implementing
something, for example) can be useful as you can be "ready to start running
tests" as soon as a testable application is made available, but also that it can
be useful to provide feedback to designers, product owners and developers on
materials such as a functional specification.

These exercises will give you the opportunity to practice or experiment with
skills such as:

* Analysing materials like specifications, wireframe diagrams, etc.
* Thinking ahead and planning
* Designing/creating test cases, determining steps/actions, thinking about
  required setup (such as environments or installed applications), preparing
  test data, etc.
* Discussing with other testers so that more ideas, approaches, etc. are brought
  into the planning

## Application

For this exercise, you will be working with materials relating to a banking
application that is (hypothetically!) going to be developed. You should work
through the exercise as if you were going to be testing the application later
on, but this is about preparation and thinking so there is no application to
look at, play with, nor to run tests against.

You will be given details similar to what might be included in a functional
specification i.e. what functionality the application should have. These will
have a focus on visible and usable things (such as login screens or actions a
user can carry out) rather than details on implementation (such as database
structure and HTTP requests/responses).

As such, you will need to make some assumptions as you go through the steps, in
order to be able to do the preparatory work, and you may have questions as you
progress as well. It's possible that whoever wrote the functional specification
didn't think of everything and may have introduced some unintentional ambiguity.

## Resources

[Banking application specification](04_resources/banking_specification.md) (and
other related resources).

## Steps

There is no one correct way of preparing for a testing activity such as
exploratory testing! Context matters, such as available resources through to the
thing to be tested itself. These are some example steps for you to follow, in
order to guide you through this first banking application exercise.

1. Start by doing an initial read through of the documents provided - in this
   case, there is some defined functionality and a couple of wireframes. Try to
   get a general understanding of the application so you know roughly what
   you're dealing with - it's OK if not everything makes sense yet.

2. Re-read the material(s), keeping notes as you go. Some structure could be
   helpful, so for this exercise sketch out a simple:
    * tree of test areas, which you can later break down into test cases
    * and a [state diagram](https://en.wikipedia.org/wiki/State_diagram) to
      represent the application's states (pages) and transitions (actions)

3. For each piece of defined functionality, consider asking yourself questions
   such as these (or others that you think are appropriate):
    * What a user should see and/or do?
    * What inputs, user interactions, actions can be taken and effects those may
      have?
    * What a user should/must not see or be able to?
    * What sorts of things it might mean from an implementation point of view?
    * Any assumptions you're having to make?
    * Any clarifying questions you might want to ask of whoever wrote the
      material?

Start with the first piece of defined functionality - the login page - but split
it into two parts. Firstly, the form itself, then later on what can be done with
it.

<details>
  <summary>If you'd like an example for analysing the form itself, click here for some detailed guidance.</summary>

The following is an example for that last step, for just the login form:

* User should be able to see a web form with fields of just username and
  password
* Username and password can be input, should be able to use the keyboard to type
  into the text areas or paste in some previously copied text; password should
  be obscured
* Logging in will change the page to some account/user information page
* User should not be able to see any account details, money amounts, any user
  information, etc. when not logged in
* User should not be able to log in without providing a valid username and
  password
* Password must be stored somewhere on the server associated with the username
* Username and password must be being sent to the server
* Assumptions: that there must be some sort of "Log in" button on the page; that
  there's no current plan to implement a "Forgot password?" button and
  functionality
* Questions: how are we storing the password details - is it done securely and
  properly, and how could a tester take a look to check?

There are a lot of details here just to illustrate the sort of things you could
be noting down. You might choose to write far fewer, you might have less to
write about, or even consider that a lot more detail is needed (for example if
some functional description seems very complex).

You can next repeat the steps above, now for the action of actually logging in
from the login page.
</details>

Once you've done the two parts of the login page, move on to do the same for the
other parts of specified functionality.

4. Spend some time considering what the highest risks could be with this
   particular banking application as specified. What might "quality" mean in the
   context of this application, and from whose perspective?

<details>
  <summary>Not sure what the risks could be? Not sure where quality comes into it? Perhaps these questions could help you...</summary>

* If you had an account with this bank, what would be most important to you? Is
  it functionality, security, something else?
* What are some important rules around how transactions work between bank
  accounts, purely in terms of quantities of money?
* If you were a malicious person, what might you want to obtain or steal in
  relation to this banking application? How might you go about it?
* What might the owner of the bank care about most, with their clients using it
  to have their money stored and moved between accounts?
</details>

5. With all the information gathered - a tree of test areas, a state diagram and
   notes on functionality - define what would be your first one hour long
   exploratory testing session with the banking application.
    * What functionality do you intend to cover? Would you look at everything,
      but only lightly looking into all the pages and only exploring happy
      paths, or perhaps would you focus on one particular area?
    * What test cases would you want to run on the functionality you're
      covering? For example, if you wanted to test transactions in some detail,
      what sorts of value of transactions would be valid cases, invalid cases
      (think: malicious users!), and how would those relate to the user's own
      account balance.

[Next Challenge](05_pair_test_analysis_more.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F04_pair_test_analysis.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F04_pair_test_analysis.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F04_pair_test_analysis.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F04_pair_test_analysis.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F04_pair_test_analysis.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
