# Psychology

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/quality_engineering/intro_to_testing/phase3/workshops/psychology.x.md)_

While your coach(es) will be running a session on this, here is some
accompanying course material.

Software testing and quality engineering overlap with a huge range of related
and less-obviously related areas, an important one of which is psychology.

While we won't go into the huge breadth of the science of psychology, thinking
about it within our context can be very useful, both in terms of our
interactions with other people and with the software itself. How we think,
react, learn, and so on can be important to consider:

* In everyday communication
* In how we work with others in the workplace
* In examining our emotions (as we test!)
* etc.

## People

While many of your interactions will be with software, whether that's testing
it, planning to test it, checking it or many other things, a significant number
of interactions will be with people as well. Here's a non-exhaustive list of
people and roles a few ex-Makers testers have worked closely with:

* Developers
* Product Managers
* End users/customers
* Other testers
* Customer support
* Marketing
* etc.

Much like you would in any other profession, being professional, considerate,
etc. with anyone you work with - internally and externally - is going to be
important, but there are some particular relationships to highlight.

### Developers

Put yourself into your shoes from a few weeks ago, after you'd worked through a
particularly complex challenge or exercise, and imagine you'd received some
feedback like the following:

"Your program is completely broken - why have you made it return the wrong
answer when the input is a string?"

It's one sentence, but there's a lot to pick apart from this that's not good -
we can list a few things pretty quickly:

* Accusatory ("why")
* Personal ("Your", "you")
* Over-exaggerating ("completely broken")

and there's plenty more in there before we get onto technical things like a lack
of detail on things like what a "wrong answer" is.

A good way to approach these situations is to come with the assumption that
everyone involved is trying to do a good job. When you're working with a
developer who has built something that they think satisfies what they were asked
to do and works the way it should, you should consider the person who is going
to receive your feedback, on their work.

Sticking to observations and avoiding making any feedback personal, is an
excellent starting point.

To change our example from above, another way of putting it might be:

"When the input is a string, the program returns an answer I wasn't
expecting..."

There are lots of articles out there on giving (and receiving!) feedback, and
for testers it's a useful skill - both from the technical perspective that we've
touched upon before regarding useful details to put into bugs or other feedback,
but also from the personal side too.

### Stakeholders & Decision Makers

A lot of the interpersonal skills from working with Developers translates into
here (and with anyone else) as well, but with stakeholders and decision makers
there's a different relationship.

Often, these two roles are held by the same person at the same time - it's
certainly common to think of anyone who is making a decision, such as whether a
product is ready to be released to the customers, as having a "stake" in the
project as well.

Stakeholders may be dealing with many projects, may not have as detailed and/or
as technical an understanding of the project, and may themselves have time
pressures such as impending release dates and demanding customers. When you're
providing them with information on test activities, aim to keep it:

* Factual - give supporting evidence such as observations or references to bug
  tickets
* Frequent - give regular updates so they stay informed, rather than batching
  everything up to the last minute
* Fair - don't exaggerate or catastrophize, don't bake in assumptions or make
  guesses (they might base important decisions on things that aren't true)

You can also think of the decision maker as being a sort of gatekeeper - they're
the one who decides whether or not something (e.g. a product) passes through
(e.g. gets released). As that decision is frequently associated with the
question "is it ready?" it's not uncommon for the testers to be involved, but
also have the question "is it ready?" directed at them. In that situation,
suddenly the tester or a test team become the gatekeepers and this is not a good
thing.

Here are some reasons why testers should actively avoid becoming gatekeepers of
software:

* Testers become a bottleneck - e.g. everyone is waiting on test to "finish
  testing" and there's a perception they're holding up the project
* Testing is imperfect and has no guarantee of something being ready, bug free,
  etc. - this is for many reasons, such as test activities being non-exhaustive
  or a simple lack of time
* Testers end up being solely responsible - when something goes wrong later on,
  blame can (although shouldn't) be cast around

The last point is a key one - think back to the earlier discussions around
quality being everyone's responsibility, and you'll see why test slipping into a
gatekeeping role sets the wrong mindset across the organisation in terms of
testers' responsibilities and quality. Helping ensure everyone understands their
roles in terms of quality, and getting testers involved early, mitigates the
risk of testers becoming decision makers.

### Customers & Support Team

Having a better understanding both of how your customers use the products and
what sorts of problems they encounter can be very powerful information for a
tester. If you have more idea of real world use cases, perhaps you can update
how or what you're testing. If you see more of their pain points or the sorts of
errors you're encountering, perhaps you can modify the focus of some of the
testing you're doing.

As testers are frequently not customer-facing members of staff, it can be tricky
to understand exactly what value your product has for those working with it, so
when opportunities arise - whether that's through the support team or even
something like a user conference - consider taking the chance to learn more and
empower your testing.

It's also worth noting that the relationship works both ways! Sometimes testers
make very good allies for customer support team members, as they're able to
suggest workarounds or already know of upcoming fixes.

## Testing

We all have biases - it's impossible not to - but knowing our biases can help us
avoid or mitigate them in what we do.

For example: realising where emotion can rule over reasoning could make us
better testers.

### Emotions & Mathematics

Your brain can trick itself. Being aware of how and when, might mean you can
have mitigation strategies to avoid those tricks when testing.

Here's one example:

```
Imagine that there's a deadly disease that's infected 1 in 1000 people. There's a test released for the disease that's 99% accurate. You take the test... and find out it's positive.
```

Oh dear. But what - what's the probability you're actually infected?

* Assume 1,000,000 people take the test
* So that means around 1,000 are infected
* Of them, 990 get positive results
* But for the uninfected people, and there are 999,000 of them...
* ...9,990 get positive results despite the fact they aren't infected

So it's much more likely that we aren't infected - what a relief. But our
emotions can kick in quickly and rule over our ability to reason effectively,
including thinking through some mathematics.

<!-- OMITTED -->

<!-- OMITTED -->

<!-- OMITTED -->

### Diagnoses & The Conjunction Effect

When we're testing, we can encounter behaviour which we think is "bad" in some
way - perhaps the application crashes, or just doesn't show what we were
expecting. Diagnosing what we did and/or what state it had to initially be in
for that behaviour to occur can sometimes be surprisingly difficult. It's one of
the reasons why we keep notes during things like exploratory testing sessions.

There can be lots of factors involved, from other things happening on a server
to the current date and it's not always clear which factors are important and
which are not. It's also possible that the actions leading up to the observation
have put the application into a particular "bad" state, or equally that they
were all irrelevant and the single, final action we did is the only important
bit.

<!-- OMITTED -->

Extra variables and potential effects makes something appear more plausible but
in reality, makes it less probable.

This is called the Conjunction Effect (and although it has some criticism i.e.
Misinterpretation Hypothesis) and it's worth being aware of it and its effect on
you when you're doing things like diagnosing some behaviour and attempting to
find the reproduction steps.

The effect can be mitigated through a more careful review and evaluation of
probabilities.

### Confirmation Bias

<!-- OMITTED -->

Confirmation bias is a situation where we are primed by this bias regarding what
to expect. Let's look at a hypothetical situation - a new piece of functionality
has been developed and has just landed on your desk for a review and some
testing.

How would we feel about the upcoming testing session if:

* The developer who had implemented it is a Principal Engineer, very experienced
  and had been working there for years? What if the developer is a new starter
  fresh out of university?
* The developer has a history of making errors and code where lots of bugs are
  found? What if the developer was much more reliably producing "good" code?
* The specification for the functionality was really vague and little more than
  a single user story? What if it was instead fully defined with no ambiguity?
* The new functionality was an extension to an existing product that's
  well-established and has been well-tested in the past? What if it's totally
  new and unrelated to anything that's gone before?

In some cases, we might expect there to be more issues than in others. And while
this might ultimately be true, if we ourselves go into a piece of work with an
expectation, we're more likely to find what we're looking for (e.g. whether many
or very few bugs) - this is a confirmation bias.

### Correlation

Our brains are excellent at spotting patterns. Ben Goldacre, the author of “Why
Clever People Believe Stupid Things”, discusses how our minds try to trick us –
they:

* See patterns in random noise
* See causal relationships where there are none
* Overvalue confirmatory information for a hypothesis
* Seek out confirmatory information to support a hypothesis
* Assess quality of data based on previous beliefs

We can’t stop being human! The problem with this is that we can leap to an
incorrect assumption that there's a relationship in some data when one doesn't
really exist.

<!-- OMITTED -->

The problem is that correlation doesn't mean causation. We need to be aware that
just because it looks like, for example when we change variable X we see outcome
Y change similarly, it doesn't automatically mean changes to X causes changes to
Y.

Some ways to lessen the impact of confirmation bias are by simply starting off
by being aware of your biases, re-running certain tests (maybe the pattern goes
away) or even something like discussing with your peers to see if they see a
pattern as well.

### Critical Thinking

Dual Process Theory is a concept that, although sometimes disputed, suggests our
thinking can be broken into System 1 and System 2 thinking:

| System 1 Thinking                  | System 2 Thinking    |
|------------------------------------|----------------------|
| Automatic/non-conscious            | Manual/conscious     |
| Fast                               | Slow                 |
| Cheap                              | Expensive            |
| Best guess/Uses shortcuts          | Aware of bias, etc.  |
| Easy                               | Difficult            |
| Instinctual – kept ancestors alive | A process/rule based |

<!-- OMITTED -->

While "creative thinking" can be thought of as divergent, "critical thinking" is
convergent (J.P. Guilford, 1956). Whereas creative thinking can come up with
many possible solutions, convergent thinking is solving a problem with a single
selected solution.

Here's a nice testing example - generate many test ideas (divergent), determine
which are appropriate and prioritise (convergent).

While intuition and feelings about something we're about to test are great, it's
sensible to analyse why we feel that way about it as that can help us determine
more about ourselves, the product and to better plan what and how we’ll test.

### Dopamine

A fun question to finish on - can testing be addictive?

Fruit machines are designed to give random payouts. When we win, dopamine is
created in the brain and that in turn causes us a pleasurable feeling. But
that's not the whole story! Dopamine neurons cause our brains to try to predict
patterns... including in the randomness of a fruit machine's payouts. When
bigger random unpredictable events occur, we get bigger surprises, bigger
amounts of dopamine, and a bigger desire to try to find that same pattern again.

Professor Wolfram Shultz found 3-4 times more excitement from random events, for
the dopamine neurons, than predictable ones.

Whether one considers finding a bug as a positive event or not is can be
somewhat debatable, but ultimately knowing that these bugs exist is beneficial
to the business. Just because we haven't found them doesn't mean they aren't
there - our discovery of them isn't the cause of their existence! So when we
test, if we happen across bugs unexpectedly - say from exploratory testing
rather than pre-defined script-lead testing in a predictable area - the
resulting dopamine creation might suggest that we can become addicted to
discovering bugs, and therefore testing.

[Next Challenge](02_terminology.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F01_psychology.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F01_psychology.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F01_psychology.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F01_psychology.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F01_psychology.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
