# Terminology

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/quality_engineering/intro_to_testing/phase3/workshops/terminology.x.md)_

While your coach(es) will be running a session on this, here is some
accompanying course material.

In testing domain within software development there can be some different terms
used to mean the same thing and sometimes are used incorrectly or to mean
different things.

You learned about the origin of the term "bug" during the Golden Square. There
are many different terms which you might hear when encountering a bug, many of
which sound quite similar, but they occur in a cascade. In this section, we'll
look at those three cascading terms and their alternative names:

    Error  ->  Defect  ->  Failure

## Errors

**Errors** or **Mistakes** are things made by humans and can occur for lots of
reasons e.g.:

* Inexperience
* Rushing
* Misunderstanding (between people, of inter-dependencies, specifications, etc.)
* Human fallibility

Someone might make a typo in the code, misunderstand a requirement, implement
the wrong functionality, or not write code to handle a particular input because
they didn't think of it.

> For example, imagine a developer was asked to prevent users under 13 from
> entering a website. In their head, they decide they're going to code this
> check as `age > 13`. This is an error, because it will prevent users aged
> exactly 13 from entering.

Although it's not always the case, errors can often lead on to cause defects
which we'll cover next.

## Defects

**Defects** or **Bugs** or **Faults** are problems within a piece of work where
there is an implementation gap or incorrectness, and these are caused by human
error - see above. The pieces of work where defects can exist are not just 
code - for example, a defect in a functional specification document.

Defects can be found by various test activities, from simply looking at the code
to observing any resulting effects they can cause (see the next section for more
details). They are also the things that developers try to "fix" by making code
changes. A defect can exist regardless of whether or not anybody has discovered
it - it's just lying in wait.

> To continue our example, our developer adds the `age > 13` check and commits
> their code into the production environment. We now have a defect; we just
> don't know it yet.

As you may have noticed from our materials and others you can find online,
defects are also frequently referred to as bugs.

## Failures

**Failures** are the effects that can be observed by users or testers, when
something goes wrong. They can be caused by defects, or by other things such as
external factors (e.g. faulty hardware or radiation).

> To finish our example, our tester might observe some unexpected behaviour when
> entering `age = 13` then log a bug report. Alternatively, a real 13-year-old
> user may react negatively when they can't use the website and sign up with one
> of our competitors instead.

Failures can be observed by executing tests as well as by end users, so it's the
risk of failures that testers are often working to reduce.

## Conclusion

In many workplaces, many of the above terms are used interchangeably. But it's
important to understand if your organisation is assigning particular meaning to
any of these specific terms, in order to reduce ambiguity and confusion.

[Next Challenge](03_bug_reporting.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F02_terminology.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F02_terminology.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F02_terminology.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F02_terminology.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F02_terminology.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
