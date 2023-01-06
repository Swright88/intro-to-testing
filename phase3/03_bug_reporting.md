# Bug Reporting

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/quality_engineering/intro_to_testing/phase3/workshops/bug_reports.x.md)_

While your coach(es) will be running a session on this, here is some
accompanying course material.

We've discussed exploratory testing techniques, and how they contribute to
informing us about product quality. We've also seen that sometimes these
activities will identify unexpected results - commonly referred-to as "bugs".
But what happens when you uncover a bug? What is the path from discovery to
resolution - and which bugs might never get fixed at all?

In this chapter, we'll examine:
* What is a bug
* Why bug reports matter
* Where they are reported
* What goes into a bug report
* When you might NOT write a bug report

## What is a bug?

As we saw in the previous section, a **bug** (or **defect**) is something that
is wrong with a piece of work, whether that's code or otherwise, and is the
result of human error.

The result of discovering a bug (which usually manifests itself when you observe
a failure) is the creation of a bug report. Depending on the system that you use
for reporting the bug, you may find other terms being used, such as **issues**
or **problems**. The most important thing is: you've found something which seems
wrong in your application, and you want to tell people about it. But why?

## Why bug reports matter

One of the primary goals of a tester is to communicate information about the
perceived quality of a product, so that stakeholders can utilise that
information to make important business decisions (such as whether it's deemed
"safe" to ship a piece of software). Testing can uncover bugs, but those bugs
only have a chance of being fixed if decision-makers are effectively informed
about them.

Imagine a world in which testing was performed, and bugs were uncovered, but
those bugs are never communicated with anybody. Those bugs are unlikely to ever
get fixed (unless a developer happens to stumble across one of those bugs by
themselves).

Now imagine a more realistic scenario, where bugs are uncovered, but they aren't
communicated effectively. A tester might have confidence that they have "done
their job", but if the team doesn't fix an important bug because they've
misunderstood the impact of the issue, the bug still won't be fixed and you're
no better off than the first scenario.

The act of communicating information about bugs in a manner which persuades
others to fix them is known as "bug advocacy". It's a fundamental skill for any
quality engineer, and one which is often neglected. Yet there are some simple
guidelines and practices which will allow your bug reports to shine, and
increase the chance of important problems being solved before your team's code
arrives in production.

## Where are bugs reported?

Depending on your experience, you may have already had some exposure to bug
reports. Often these will be recorded in some kind of project management or
defect management tool, such as JIRA, Bugzilla, or the "Issues" section of a
project in GitHub.

Different teams/projects will operate with differing degrees of formality, so
it's also possible that a bug report could be something less tangible:

* A ticket on an electronic kanban system, such as a Trello board.
* A post-it on a whiteboard, or on a developer's desk.
* A comment in a team Slack channel.
* A verbal conversation ("I have a bug to report to you").

Your team should have a generally-agreed consensus on its bug reporting process.
There are various factors which might determine the strictness of a process. For
example, if you're working on the first iteration of a brand-new project
(sometimes referred to as a "Minimum Viable Product", or "MVP" for short) then
the team may be comfortable with an informal reporting process. On the other
hand, if you're working in a tightly-regulated environment, or developing
applications on behalf of a third-party client, it's highly likely that formal
bug reports will be requested. It's possible that these bug reports will also be
reviewed with a degree of formality - for instance, a committee which might
refer to themselves as the "Bug Review Board", who make the ultimate decision
about whether a problem should be fixed.

## What's in a bug report?

Regardless of your bug report format, certain key aspects are usually included,
to aid stakeholders in their decision-making process, and to assist developers
with fixing the issues.

While most of these aspects are self-explanatory, there's an art to completing
them in a way which is likely to be most effective. Your role here is like a
cross between an SEO expert (utilising keywords and generally-recognised
parlance to make your issues easy to discover) and a clickbait journalist (using
convincing language and calls-to-action to make people want to read your
reports).

Here are some key aspects that you're likely to encounter, and some tips on
using them effectively.

### Title / Summary

Think of this as your "headline": a one-line summary, which will often be
visible in a list alongside other bugs. Ideally, anybody who's sufficiently
familiar with your application should be able to read the title, and understand
the nature of the problem that's being described.

If you're working in a distributed enterprise environment where dozens (if not
hundreds) of bug reports are created each week, if your bug's title isn't clear
enough, it's possible that it will be overlooked altogether, or lost among the
noise of much clearer bugs.

Much like a news headline, shorter titles tend to be preferable, but they
shouldn't sacrifice clarity for brevity. Consider these three titles for the
same fictional issue:

* **No search results found** - This is too vague. Is the search feature
completely broken, or is there something more subtle happening?
* **If I use speech marks when I'm searching on my Mac then the search doesn't
work** - This is both wordy and vague, and comprised of words which would be
difficult to remember if you were trying to search for the bug report.
* **Phrase searching fails to return results in Safari** - Much better! It's
concise, explains specific conditions (e.g. it's a Safari-specific issue) and
uses technical terminology appropriately ("phrase searching" is the term for
enclosing words within speech marks within a search term).

### Description

After the title, it's typical to include a textual explanation of what the
problem is, and why that problem matters. In many ways, you can think of this as
being a lot like storytelling: you need to offer a compelling "plot" which
describes the problem, who it's impacting, and why it matters.

Let's continue the example of our fictional broken search feature. Which of
these descriptions do you think would be most likely to persuade a stakeholder
to address the problem?

> #### Description A:
> 
> I searched for John Smith but it said there were no results when there should
> have been

> #### Description B:
> 
> When attempting to use the search feature to locate someone by their full name
> (e.g. `"John Smith"`), Safari shows a "No results found" message, even though
> there are users with that name in our system.
> 
> The same search works correctly in Chrome and Firefox, however according to
> our stats, Safari accounts for almost half of our traffic, so this will have a
> significant impact on those users' ability to locate data on our site.

This isn't to say that you need to treat all bugs as if they are the most
important problems in the world - if you "cry wolf" in such a fashion, people
may overlook your concerns when something genuinely important comes along. But
there's value in presenting the fullest story possible for the bug that you're
reporting.

### Steps to reproduce

Rather than just providing an abstract explanation of a problem, your colleagues
will understand a bug much more clearly if you are able to provide an
illustration of the problem, in such a way that somebody else could replicate
the problem for themselves. This is especially useful if a developer is
investigating a problem that you report: they might attempt to follow the steps
on their own machine, with additional debugging enabled, and they might want to
repeat these steps after making a fix, so that they can determine if their fix
has worked.

When you first encounter a problem, it's possible that you don't know the
precise steps that were required in order to encounter the bug (you might not
know if it relates to a specific browser, a specific input, or a specific user).
It's worth investing time here to ensure that you can replicate the problem, and
to attempt to narrow the scope by identifying the minimum possible steps to make
the problem happen. 

Often, the steps to reproduce will be a series of bullet-points, and will
conclude by stating the "Expected result" and the "Actual result", similar to
those that you might have written in a test plan. Consider this as an example
for our ongoing search problem:

> #### Steps to reproduce:
>
> 1. Load the homepage on Safari 
> 2. Type "John Smith" (including quote marks) into the search box
> 3. Press Enter
>
> **Expected result:** 28 matches found (this is what we get in Chrome)  
> **Actual result:** 0 matches found, and there is an error visible in the dev
> console: `Bad character "&apos;" at index 0`

Depending on the bug, it might be tempting to attach a screenshot and/or a video
to the bug report. This is generally a good idea - it's a lot easier to
understand a problem (especially a display problem) if you can see the problem
with your own eyes.

However there's an important caveat: if you've encountered a specific error
message or a stack trace, make sure you include that message somewhere within
the bug report itself, not just in the screenshot/video. This way, if others
encounter the same error message in the future, they can search the defect
tracking system and identify the previous time that somebody encountered a
similar problem.

### Severity / Priority

Among the other fields that your bug reporting system might require you to
complete are some important but often difficult-to-judge attributes: severity
and priority.

* **Severity:** A bug's impact on the overall functionality of your application.
This might range from Low (a problem which users might not even notice) up to
Critical (nobody can access the application at all). 
* **Priority:** How urgently the team should seek to fix the problem. This might
range from Low (it's not important to fix right now) to High (it should be fixed
at the earliest possible opportunity).

Often, you would expect these values to stay in-line with each other. For
instance, surely the highest severity bugs are also the most important ones to
fix? However, this isn't always the case. Consider these examples:

* Due to a browser compatibility issue, a site's checkout page has stopped
working in versions of Internet Explorer older than version 11. This is **high
severity** (a major piece of functionality is unavailable) but it may be deemed
**low priority** if the site's metrics demonstrate that nobody has visited the
website in Internet Explorer 20 for over six months.
* Your company has just completed an expensive rebranding exercise, but the site
homepage still shows the old version of the logo. This may be **low severity**
as it won't affect any users' ability to browse your site, but it may be deemed
**high priority** as the business is deeply invested in completing their
rebranding.

Depending on how your team (and your defect management system) are configured,
it's possible that the assignment of severity and priority might be performed
automatically on your behalf. For instance, maybe all of the new bugs in your
system are defaulted to "Medium severity, Medium priority" until a stakeholder
chooses to escalate a problem. If this is the case, it's even more important to
provide clarity as to the scope of a problem when you're writing your bug report
titles and descriptions, as this might be the only determining factor for
whether a bug is important to fix. 

### Other bug metadata

Most defect management systems allow for other fields to be added, removed, or
given default values. Some other important terms that you are likely to
encounter include:

* **ID:** Most electronic reporting systems will give you some sort of unique
bug report ID whenever a ticket is created (for instance, `MAK-123`).
* **Reporter:** The name of the person who reported the bug. If you reported it,
this will be you! This means that others are likely to come to you in the future
with questions about the issue. Importantly, this means that one of the
audiences for your bug report is **you** - if you revisit a bug report in a
year's time, will you be likely to remember/understand what the problem was?
* **Assigned To:** Depending on how your system is configured, this might
default to "Unassigned", or there might be a default assignee (such as your
team's Product Owner). Or, your team might be asked to determine the best person
to assign a bug to.
* **Status:** Newly-reported bugs will have a default state, such as Open, or
Pending Triage. As bugs are reviewed and dealt with, these will move through a
workflow which your team has predetermined, probably passing through statuses
such as Fixed and Closed. However, not all statuses will result in a bug being
fixed: some common "invalid" statuses are Won't Fix, Duplicate and Cannot
Reproduce. Can you think of what might cause a bug to end up in one of these
states, and how it could be avoided?

## When might you NOT write a bug report?

Once you develop a healthy relationship with bugs (and bug reporting) within
your team, there might be situations in which you agree not to write a report
for a particular bug. Agile teams are encouraged to eliminate waste, and
unnecessary administration certainly falls into that category. Imagine these
scenarios (but also consider their caveats):

* If you've uncovered a bug, and you (or a developer) are going to fix that bug
immediately: if the bug is sufficiently trivial (such as a text typo) then there
might not be much point in crafting a bug report, complete with title,
description and steps to reproduce. However, don't underestimate the value of
**traceability**: while a problem might _seem_ small, it could potentially break
something (including, for example, your test automation). Some teams are even
required to include a bug report ID in their Git commit messages, which you
wouldn't be able to do if you didn't create a report!
* If you've uncovered a bug, and the team's consensus is that it will never get
fixed (for example, if it's both low-priority and low-severity, or if the
application is so close to its ship date that it won't ever get onto your team's
radar). However, be aware of **accountability**: particularly as a new tester,
if someone were to later ask "how come you didn't find that bug" or "why didn't
we fix that before release", it can be helpful to be able to point to a written
record of the decision.

## Exercise

/** EDU
  Before beginning this exercise - ensure that you've closed any "old" bug
  reports in the repository which were created by a previous cohort.
**/

This is a two-part exercise. The first part is a solo activity; the second part
is a peer review activity.

1. Revisit your testing notes from the email validation and wrap_it exercises in
Phase Two. (If you didn't complete those exercises, now is the perfect time to
do it.)
2. Look at the issues that you encountered during those exercises. Try to rank
them (look for the highest severity/priority bugs).
3. Open this repository on GitHub.com, and proceed to the "Issues" tab.
4. Starting with the most important bug, use the "New Issue" button to create a
new bug report for each of your issues. You might want to use [this
template](03_resources/sample_bug_report_template.md) as a starting point.
5. Continue creating these bug reports until maximum 1 hour has elapsed, or
until you don't have any more bug reports to create, whichever comes first.

/** EDU
  It's possible to create a default issue template for a GitHub
  repository, to bypass the need for devs to use a template markdown file. See
  this URL:
  https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/manually-creating-a-single-issue-template-for-your-repository
  However I think it's useful to have this bug report template as a reference
  point, regardless.
**/

After this hour has elapsed, speak to the other person in your pair, and confirm
that they have also completed the activity. Now, review each other's bug reports
on the GitHub Issues page:

1. Filter the issues page so that it only shows you the bugs that your partner
has reported (you can type `author:USERNAME` in the filter, where `USERNAME` is
their GitHub username).
2. Open each bug report in turn. Review the content to see if you think that the
bug is understandable, and whether the importance is communicated effectively.
(Imagine that you don't have prior knowledge of this application - can you still
make sense of what is being reported?)
3. Using the "Leave a comment" box beneath each bug, add some feedback for each
of the issues.

Later, your coach(es) will perform a walkthrough of everyone's bug reports (and
the comments that you have left for each other) to assess how effective they
are.

[Next Challenge](04_pair_test_analysis.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F03_bug_reporting.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F03_bug_reporting.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F03_bug_reporting.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F03_bug_reporting.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fintro-to-testing&prefill_File=phase3%2F03_bug_reporting.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
