# Myths of Software Testing

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/quality_engineering/intro_to_testing/phase4/workshops/myths.x.md)_

While your coach(es) will be running a session on this, here is some
accompanying course material.

There are many myths and misconceptions about the world of software testing.
Some of these may once have been true; many are either stereotypes or
misunderstandings which remain pervasive, often because (as testers) we're bad
at debunking them!

* Testing is easy! Anybody can test.
* Testing is boring! You're just testing / finding bugs.
* Testers break the software.
* The best testers are the ones who find the most bugs.
* Testers are just "failed developers".
* Testers don't need to know anything about code.
* Quality Assurance: testers can "assure quality".
* If you miss a bug, you're not doing your job properly.
* Testers should "test everything".
* Testing takes too long.
* Testers and developers don't get along with each other.
* "That's not a bug, because nobody would ever do that."
* All testing can be automated.
* You can't test until the product/feature is completed.
* You should always test before your code reaches production.

When myths are allowed to continue unchecked, they can make it harder for us to
do our jobs. You may find yourself excluded from activities where people feel
like "we don't need to involve the testers in this", or doors might be closed
(literally or metaphorically) in areas where you could provide valuable input. 

But all is not lost! Below, you'll find some brief guidance as to why each of
these is a myth. Together, we can destroy these misconceptions.

## Testing is easy! Anybody can test.

It's true that most people - even small children - are capable of picking up
something and evaluating whether it's fit-for-purpose. However, people will
generally only consider if something meets _their_ needs; software is much more
complicated than this.

Testers will often downplay the technical and analytical skills associated with
their roles. When evaluating a feature for the first time, they might say that
they're going to "have a play with it", which helps to give the impression that
testing is "just clicking around".

For the sake of your own reputation, it's valuable to display the skills that
you are utilising. You could do this by, for example, showcasing your test plans
/ outputs, or publishing your exploratory testing reports: suddenly, you're not
just "playing with" the email validation on a form - you're systematically
running through a predetermined list of scenarios which help to reveal risk in
an application, and varying your inputs according to information that you
uncover along the way. And you can't say that "anybody" could do that.

## Testing is boring! You're just testing / finding bugs.

It's rare for two days to be the same for a tester. The nature of the role,
especially in fast-paced agile environments, means that you could have
completely new work demanding your attention on any given day. And that work
needn't be the actual act of "testing" (e.g. running test cases): that's why
there's a noticeable shift in the industry to using the term "quality
engineering" (as you may have already noticed in the Makers course material).
Quality can be infused at many different points in a project, including before
any code has been written; if you're doing your job well, the actual "testing"
process should be a relatively small portion of your work (your "testing" will
simply be confirming things that you already know to be true).

If anything, testers are often involved in more areas of an engineering project
than a developer might be. Within development teams, there are often so-called
"knowledge silos", where developers have in-depth knowledge of areas that
they've worked on a lot, but are less familiar with areas which are "owned" by
other developers. Testers are much more likely to have familiarity with a whole
system, as they're more often thinking of end-to-end or user-focused scenarios.
For many, such varied (and non-repetitive) work across lots of areas of software
and/or a company can be more interesting or engaging.

## Testers break the software.

You'll occasionally hear exasperated noises (typically from people who are under
pressure to deliver software) that "it's not finished yet, because the testers
broke it". That's not accurate though: if you uncover a bug, that bug was always
there, just waiting to be found. As the famous test consultant James Bach puts
it: "We don't break the software. We break _illusions_ about the software."

This doesn't necessarily mean that a developer "broke" it, either! Bugs often
occur as a result of confusion or miscommunication; no competent developer is
deliberately writing broken code, but if they've misheard or misunderstood
something, they might implement the wrong behaviour. 

Testers can actually have a helpful healing role here! If you're able to
effectively establish the root cause of a bug (i.e. revealing how the bug came
to exist) then this can help the team to ensure that such problems don't recur
in the future. Serving such a role can help to build more positive regard
towards the testers in a team, with a vision of our role being more
constructive, as we saw in the Psychology section.

## The best testers are the ones who find the most bugs.

Throughout the software development process, managers and executives are
constantly looking to measure process. Often this is for very important reasons,
such as the need to inform customers or shareholders of the intended ship date
for a product, or to ensure that teams are being empowered to work in an
efficient fashion.

When it comes to testing, bosses will often resort to counting the number of
bugs. After all, if we've logged 5 bugs this week, but there were 20 bugs
reported last week, that must mean the quality is improving, right? (Think about
some of the reasons why this might be a faulty assumption.)

Similarly, with testers, it can be tempting to look at who's raised the most
bugs, and assume that they are the "best" tester. But raw bug counting is
another flawed metric: compare the tester who found 10 problems on an
unsupported operating system, versus the tester who found 1 critical security
flaw in the application. The "best" testers often aren't logging bugs at all -
they're collaborating with stakeholders and developers to ensure that problems
don't creep into the code in the first place.

## Testers are just "failed developers".

There's often an assumption made that becoming a developer should be the
pinnacle that everyone strives for, and that people only end up as testers
because they weren't good enough to be a developer. Hopefully you've already
demonstrated the flaw in this myth for yourselves!

Being a developer isn't "better" than being a tester, any more than it's
"better" than being a project manager or a business analyst. It's just
different. Testing exercises a different set of skills and disciplines than
being a developer, and it's personal preference as to which you find more
enjoyable.

For example, testers are often required to exercise greater creativity and
analytical ability. Developers will often focus on implementing what they've
been asked to do - the "happy path" - whereas testers are required to consider
the myriad ways in which things might go wrong for users who venture off the
happy path, and consider the impact on a wider system (rather than just the
component that they're working on). If those activities sound exciting for you,
you're more likely to be at home in a tester's role, regardless of your coding
ability.

## Testers don't need to know anything about code.

Despite the above, gone are the days when testers sat in a room full of other
testers, waiting for a new version of an application to be "thrown over the
wall" by a development team, and tested in isolation. Testers need to equip
themselves will the strongest possible arsenal in order to reveal valuable
information about the risks within their product, and developing "code literacy"
is a great way to do this.

This doesn't mean that you need to be 100% proficient in every language that
your development team is using. However, a general understanding of the
constructs of a given language can be hugely valuable. If you're comfortable
with looking inside a pull request, and understanding where code has changed,
you can sometimes uncover bugs without even looking at the application.
(Remember the example from the Bug Reporting section, where a developer added an
`age > 13` check when trying to allow entry to people who are 13 and over; if
you know what `age > 13` is doing, you can already tell that this isn't doing
what's expected.)

The more that you look at code - particularly in languages or areas of a product
that you've not encountered before - the greater the chance of identifying
subtle and deeply pervasive issues in your software.

Even if you don't have "developer" in your job title, it's also hugely useful to
be able to wield some of the power of coding for yourself, such as being
comfortable with using Python so that you can programmatically generate test
data to support your testing.

## Quality Assurance: testers can "assure quality".

The phrase "Quality Assurance" was carried-over into software engineering from
factories and production lines, but it's never truly meant what people think
that it does. The infinite ways in which software can interact means that, at
best, we can say that software has been observed working, on some occasions,
under certain conditions.

Similarly, there's no such thing as a "bug-free" application. Testing can show
the **presence** of bugs in a particular situation, but it can never demonstrate
the **absence** of problems. The most critical bug in your application might be
the one which is hardest to find, if it requires a "perfect storm" of inputs in
order to trigger it: for instance, imagine a bug which only occurs when a
request is submitted at _exactly_ midnight (down to the millisecond). Even if
you knew that you wanted to test this, it could prove difficult to reproduce;
and if you knew that you wanted to test this, it probably meant that you already
knew about the bug!

The phrase "Quality Assurance" is gradually beginning to drift out of usage,
although the acronym "QA" still often persists within job titles (QA Engineer,
QA Analyst, etc). People also have a knack of using QA as a verb ("Can you QA
this for us?") - it's important to ensure that such people understand exactly
what service you are (and aren't) offering to them.

<img
src="https://user-images.githubusercontent.com/7154703/207561428-69ee4a96-2014-49d7-a56c-b2433bb880fd.jpg">

## If you miss a bug, you're not doing your job properly.

Even the teams with the healthiest, most collaborative working environments can
sometimes come unstuck when a bug is spotted in their production system,
especially if it has significant impact to customers. Companies will perform
Root Cause Analysis in order to establish what happened, and how they can
prevent it from happening again, which is a valuable exercise.

However, when performing a Root Cause Analysis exercise, one question is often
asked repeatedly: "Why didn't the testers spot this bug?" 

Whilst accountability is important, it's important that testers don't kick
themselves too much over individual issues - especially if they are relatively
minor. For example, any additional time which could have been spent identifying
Bug X, is time which might have led to you missing Bug Y or Bug Z instead - and
maybe those were more important things to find.

Once useful way to reframe this question, if you encounter it, is to ask "Why
didn't _the team_ spot this bug". This allows you to have a wider conversation
about whether, for instance, there were ambiguous requirements, insufficient
attention to unit tests, or simply too much simultaneous work-in-progress for it
to all be tested to a satisfactory standard.

## Testers should "test everything".

During exploratory testing exercises, you've already seen that there are an
infinite number of ways in which software can be tested. Even if you were to
narrow your scope to a single function of a single feature, there are multitudes
of inputs and variables that you could apply to your testing - and that's before
you even consider how each component of your code interacts with every other
piece.

This means that so-called "exhaustive testing" - testing until you've tested
everything that could possibly tested - is a myth. But that's a good thing: If
we can't test everything, then we need to at least make sure that we are testing
the _correct_ things. This means that testers become skilled at tasks such as
assessing risk, prioritisation, and learning to communicate effectively with
developers and stakeholders.

## Testing takes too long.

Once stakeholders acknowledge the myth of exhaustive testing, this often sparks
a chain reaction of panic. If you can't test everything, how will you ever know
when you're done?

Combine this with the simple fact that teams tend to have more developers than
testers. People often speak in terms of ratios, and it's not uncommon to have a
4:1 or 5:1 ratio of developers to testers. Sometimes it's lower; sometimes it's
_much_ higher. Whatever the case, there are generally more people generating
code than those testing it.

Bizarrely, this is then often presented to be _the testers' problem_. We can
find ourselves accused of being a "bottleneck" within the workflow; and when
stakeholders attempt to rush items through testing in order to get them released
quickly, the only thing that can possibly be sacrificed is quality.

This is another myth which you should attempt to reframe as being a _team_
problem. It's the entire team that's being asked to deliver the work: what can
you do as a team to ease the process of getting quality work released? Maybe it
means hiring more testers; maybe it means working with developers to give them
some guidelines for testing their own work, or sharing information with them
about common pitfalls which often delay work items when they're being tested.

## Testers and developers don't get along with each other.

The world loves memes, and regrettably there are some funny memes out there
about the relationship between developers and testers, which can lead to this
myth being reinforced.

Certainly, in the days before agile software development, there was often a
terse relationship between developers and testers. There wasn't much interaction
between the two disciplines:

* Developers would write some code, give it to testers, and then they only heard
back from testers if something was wrong, or if the tester had misunderstood
something. When somebody's only interactions with you are going to directly
inconvenience you, you don't tend to enjoy talking to them.
* Testers would sit in their own room, patiently waiting for code to be
delivered to them, with only some specifications/requirements to look at. When
they received code which didn't meet those requirements, they would wonder what
the heck the developers had been doing for all this time.

The divide was very real. Like all divides, they have been gradually worn down
through discussion, understanding and empathy. It's absolutely essential for
testers and developers to collaborate on modern software development projects,
and despite occasional hiccups, we wouldn't want it any other way. So while the
memes may be funny, don't expect to encounter such a hostile and
counter-productive relationship in the wild.

## "That's not a bug, because nobody would ever do that."

Sometimes you might uncover the _perfect_ bug: the one which requires such a
precise combination of inputs that you wonder how (despite your planning) you
even managed to find it in the first place. This is immensely satisfying,
especially if it's a bug which had the potential for a severe impact.

You take the bug to your product owner, but you're surprised to hear that they
don't intend to fix it, because "nobody would ever do that": your inputs were so
peculiar that they estimate that the chances of it happening in the real world
are negligible.

This is where bug advocacy can be valuable:

* Make sure the person understands the potential impact of the problem, if it
were to be encountered. A high-severity issue with a low probability of
occurring could still be deemed worthy of fixing.
* Extrapolate the problem, by outlining a "worst case scenario" for this bug. A
product owner might not be concerned if they hear that one of your form fields
gives a strange SQL error when you include an apostrophe in the field. They
might be more alarmed if you could explain that this means that your form is
vulnerable to a SQL injection attack, which could allow a hacker to gain access
to your data, or to destroy it.
* Bugs are easier (and cheaper) to fix at the earliest possible point. Imagine a
developer being asked to make a change on the same day that they wrote the code,
versus a different developer being asked to make that change in a year's time,
when the bug has already reached production (and maybe you even have customers
who are depending on the "wrong" behaviour).

But one important thing to remember is that it's your stakeholder who will have
the final decision about whether or not a bug will be fixed. Because of this,
you need to know when it's okay to let go. If you've successfully communicated
the nature and severity of an issue, and a stakeholder decides not to fix it,
you'll immediately be avoiding the "Why didn't you find that bug?" trap that we
discussed above.

## All testing can be automated.

Test automation is inherently valuable. You've already seen how you can use it
to automate multiple scenarios, in multiple environments, far faster and more
accurately than a human could ever repeat the same steps.

So it's perhaps not a surprise that the natural inclination of teams is to say
"well, let's automate _all_ of our tests then". We'll look a bit more about the
infeasibility of this in the Automating Checking module.

One of the problems is that everything which isn't automation tends to get
grouped together under a different umbrella term, "manual testing", where the
word "manual" makes it seem like a lesser, lower-class form of testing, which we
might want to eradicate. But as you've seen with exploratory testing, the act of
exploring and evaluating a product is a deeply human skill, and one which could
never be automated.

While it's almost certainly preferable to automate any mundane tests which are
likely to be time-consuming, boring or repetitive for a human to follow,
automation isn't a replacement for having a tester looking at the product - the
two activities are symbiotic. And despite what tool vendors might tell you, even
the act of designing test automation requires a skilled person to make sure that
the automation is providing the most value. The machines won't be taking away
our jobs just yet.

## You can't test until the product/feature is completed.

Hopefully you've already seen for yourselves that this is a falsehood. There are
many ways that a tester can be usefully involved, even before a line of code has
been written; alternatively, there may be opportunities to pair with a
developer, to assist them with their implementation and unit testing.

That said, even if _you're_ aware that this is a myth, that's not to say that
there won't be others in your team (or even managers) who do believe in the
myth. Because of this, testers can sometimes find themselves excluded from
valuable activities; for instance, "we don't need to invite the testers to the
discussion about this feature, because they won't be testing it for ages yet". 

Hopefully this is a myth which will erode over time, but the quickest way that
you can personally combat this is by demonstrating your value, and showing an
eagerness to be involved at all steps of the software development lifecycle.
Once you've gained credibility by demonstrating your value, you won't have to
beg for invites to meetings - you'll be one of the first on the guest list.

## You should always test before your code reaches production.

There are certain industries and products where you wouldn't want to wait until
your code reaches production to discover whether it works or not. Aeroplanes and
critical medical devices are good examples where you don't want to suddenly
discover that, for example, your engine fails when you take it above 10,000
feet.

It's all about risk - and there are many companies for whom their products have
a very different risk profile, and they're therefore much more comfortable with
"let's ship it and see what happens". Famously, this is how companies like
Facebook do much of their testing: once they're relatively confident that a
piece of functionality is working as expected, they'll send the code to
production (perhaps just to a small set of users, using a technique known as
"A-B testing", where some customers see version A - the old version - and others
see version B). Then they monitor their production environment (for example,
their log files) to see if customers are encountering errors with the feature.
If there's a problem, they can just "roll back" to the previous version, and fix
the problem in their own time.

Those are two extremes, and whilst most companies sit more on the "let's test it
before we ship it" side of the fence, don't forget that this isn't the only way.
We'll talk more about post-release activities, such as log monitoring, in an
upcoming module.

[Next Challenge](02_principles.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F01_myths.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F01_myths.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F01_myths.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F01_myths.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase4%2F01_myths.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
