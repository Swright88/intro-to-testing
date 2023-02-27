# What is Quality?

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/quality_engineering/intro_to_testing/phase1/workshops/quality.x.md)_

Your coach(es) will be running a session on this. Here is some accompanying
course material, but there's no need to read this before the session.

## Definitions

We could start by going for an official definition of quality within software,
and for that we can look towards the [ISO/IEC
25000](https://iso25000.com/index.php/en/iso-25000-standards) standard which
states:

> The quality of a system is the degree to which the system satisfies the stated
> and implied needs of its various stakeholders, and thus provides value.

But what does that mean in practice? What do we need to be thinking about as
testers, or anyone else in an organisation who cares about quality? And what is
this "value" at the end?

Take a moment to think about an application, website, program, etc. you use
regularly. Think about your interactions with it, what's important to you, how
do you feel when you use it.

Would you rate is as "high quality"? And, why?

## Not Just Testing

It's not uncommon to find job titles like "QA Engineer" (Quality Assurance
Engineer) or "Software Tester" overlapping or used for the same thing. There are
debates out there as to what people should be called, pros and cons, and
particularly around the "assurance" part of the terminology.

But if we move away from job titles into roles or even responsibilities, we can
think of activities around quality engineering as looking to improve quality -
and testing is one of those activities.

Quality Engineering is much more than just "doing testing", but that's not to
say that testing (and testers!) doesn't have a huge part to play in helping
contribute to higher quality.

## Software Development Life Cycle

While we will come back to the Software Development Life Cycle (SDLC) at a later
stage along with different development processes/methodologies, it's useful to
have some idea of where projects or products start and what their journey can
look like.

There are different numbers of steps depending on which person or organisation
you ask, but a rough flow could look something like this, with the earlier
activities defined at the top:

* Planning
* Designing
* Developing
* Testing
* Deploying

In what some consider to be an ideal world, testers or quality engineers are
involved at all stages, including those at the start. This could involve
providing feedback on the accuracy of early use cases in functional
requirements, or planning test cases and ideas from the beginning in order to be
better prepared later on or even to work with developers on building more
comprehensive unit testing.

# Black Box & White Box

Your coach(es) will be running a session on this. Here is some accompanying
course material, but there's no need to read this before the session.

Two terms that are commonly seen in courses on software testing are "black box"
and "white box". As the names suggest, they are totally different to each other,
and describe knowledge of a product under test from the perspective of the test
engineer.

## White Box

We'll start with the term white box because it relates to the sorts of tests
you've been writing in earlier units. When tests are written with knowledge of
the code, such as class and method implementation, this is called "white box
testing" because there's full visibility of how it works. Note that this
includes things like TDD unit testing where the tests are written with just the
example implementation written out, through to other forms of testing where the
tester is able to inspect the code itself.

White box testing is more commonly in the domain of developers who have
familiarity and/or visibility of the code, but if a tester is able to look at
the code to see how it works, this can be a beneficial thing when it leads to a
different approach to testing which may reveal different defects. For example,
knowing the architecture of the system might lead to trying [SQL
injection](https://owasp.org/www-community/attacks/SQL_Injection), or knowing
how a function is written might lead to trying particular combinations of input
values.

We refer to it as a *white box* because we are imagining that the box is
clear/transparent, and we can see what's happening inside it.

## Black Box

On the other side we have the term black box - in this situation, there is no
knowledge of the planned implementation nor actual implementation, through any
means. There's no possibility of reading the code to learn more about how it is
doing things and so "black box testing" only works from things like
expectations, requirements, use cases, etc. That's not to say black box testing
is impossible - you may have many resources such as functional specifications
through to the outputs from the program or product itself to guide you when
thinking up test ideas or running tests.

Black box testing is a common situation that's much more in the domain of people
like test engineers. It can also have its own benefits over white box testing,
for example there are no assumptions about what should work and how, and a
tester going in won't have the same bias as someone who has already seen the
implementation.

We refer to it as a *black box* because the box is too dark to see inside, so we
have no knowledge of its internal workings.

<img src="./images/black_box_white_box.png" />

[Next Challenge](02_risks.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase1%2F01_quality.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase1%2F01_quality.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase1%2F01_quality.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase1%2F01_quality.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase1%2F01_quality.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
