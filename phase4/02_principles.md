# Principles of Software Testing

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/quality_engineering/intro_to_testing/phase4/workshops/principles.x.md)_

There is a commonly used list of seven principles of software testing, which is
also part of certain software testing certifications that are available.

These are worth reading through and understanding, as they can affect how
software testers work within software development, from how they test to how
they communicate with other people.

## Testing shows the presence of defects, not their absence

While testing is designed to demonstrate where defects exist, either by
discovering them or by observing their resulting failures, all this proves is
what defects are present.

Testing, no matter how hard we try or how much we do, cannot **show** the
absence of defects.

***Do say***: here are the defects I've found from what I've tested

***Don't say***: the product is perfect and I've checked there aren't any more
bugs

## Exhaustive testing is impossible

Unless you're testing some trivial code (and we're assuming you're always
working something of some degree of complexity) it's not possible to test
everything. Every possible input - or combination of inputs, in every possible
situation, from every possible initial state, with every possible set of data in
the database, etc.

This is one of the situations where by being risk-driven in our testing plans
and approaches, we're able to deal with the problem of exhaustive testing being
impossible. Because we can't do everything we might like, we have to have some
way of determining what's important to do first or to cover at some point, so
that we make the testing problem tractable.

***Do say***: I'll run tests around these areas because we think they're the
most risky

***Don't say***: I'll test everything and give 100% coverage

## Early testing saves time and money

Finding a defect in an early version of a requirements specification means that
can be rectified before design and implementation begin. Such a change, just
being a case of altering a document, is likely to be cheaper than finding out
this defect a week before the company plans to release the product to paying
customers, resulting in a lot of code rework, testing (and stress!) rather than
a document change. Such work is costly to the business in terms of time and
money, and potentially in other ways as well e.g. lost business as a result of a
missed deadline.

While the effects are less stark than the extreme example above, testing early
versions of testable code will produce defects that are quicker and cheaper to
fix than it would have been to have discovered them later on in the development
process.

***Do say***: get me involved in meetings early, even before coding starts - I
can add value

***Don't say***: let me know when you're done building it and then I'll take a
look

<img
src="https://www.paragoninnovations.com/gimages/Paragon_TreeSwing_Graphics_06_Middle.gif"
/>

## Defects cluster together

Related to the [Pareto
Principle](https://en.wikipedia.org/wiki/Pareto_principle) that says 80% of
consequences come from 20% of the causes ("the law of the vital few"), defects
in software have a tendency to cluster together.

The causes of this can be many but things like code complexity in certain
modules or functionality is a common one.

For a tester, it's important to be aware of the principle. While you may happen
upon a rich vein of tasty looking bugs, it's important not to entirely overlook
other parts of the product since risky defects may well exist there as well.

From a different perspective, attempting to determine what might constitute this
"20% of the product" can also be a good guide e.g. where a testing effort might
most valuably begin.

***Do say***: where do we think the most risky defects are most likely to be?

***Don't say***: I'm sure this bug is the last bug...

## Beware of the pesticide paradox

Named after the phenomenon where continually spraying pesticides eventually
results in pesticide-resistant foes, in software testing repeatedly testing a
single area in the same way will rapidly stop yielding new defects. Changes to
area and/or approach are needed in order for new defects to be uncovered.

In certain situations, such as regression testing in order to help reduce the
risk of particular failures from occurring again as a product changes, the
paradox can instead be seen to have a beneficial outcome.

***Do say***: let's run that test experiment again, it used to find lots of
things

***Don't say***: what could we try differently this time?

## Testing is context dependent

Simply put, in different contexts, different testing can or should be done, and
done in different ways.

A simple example would be that we'd approach testing differently if we were
working in a black box way as opposed to a white box. In one case, we don't know
how it's implemented and so there's an element of learning, discovery and
experimentation; in the other, we have more information about the implementation
and so we might be more targeted and specific about certain tests which we run,
based on what we've seen in the code.

***Do say***: what are we trying to test?

***Don't say***: I'll test it works by reading all your code before we ship the
product

## Absence-of-errors is a fallacy

Heavily tied to the first two principles: because we can't test everything and
we can only show the presence of defects, it follows that there are defects (or
errors) elsewhere of which we are not yet aware.

Similarly, just because we have found and fixed many defects, doesn't
necessarily tell us about the current state of a product. Perhaps we've fixed
hundreds of security vulnerabilities, data integrity problems and performance
issues... but as far as the customer is concerned, it's not usable and the user
experience is terrible.

***Do say***: do we want to keep testing?

***Don't say***: we've finished testing!

[Next Challenge](03_pair_exercise.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F02_principles.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F02_principles.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F02_principles.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F02_principles.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F02_principles.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
