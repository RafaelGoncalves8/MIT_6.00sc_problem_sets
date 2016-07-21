# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================
# Problem 1
class NewsStory(object):
    def __init__ (self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title
    
    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link
        

#======================
# Part 2
# Triggers
#======================
import string, re

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def is_word_in(self, String):
        String = String.lower()
        word = self.word.lower()
        String = re.findall(r"[\w]+|[^\s\w]", String)
        for i in range(len(String)):
            if String[i] == word:
                return True
                break
            else:
                pass

        return False

#s = WordTrigger('koala')
#print s.is_word_in("My Koala's name is Fred")
        

class TitleTrigger(WordTrigger):
    def __init__(self, word):
        self.word = word
    def evaluate(self, story):
        return self.is_word_in(story.get_title())


class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        self.word = word
    def evaluate(self, story):
        return self.is_word_in(story.get_subject())

class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        self.word = word
    def evaluate(self, story):
        return self.is_word_in(story.get_summary())


# Composite Triggers
# Problems 6-8

class NotTrigger(WordTrigger):
    def __init__(self, Trigger):
        self.trigger = Trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

class AndTrigger(WordTrigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)

class  OrTrigger(WordTrigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)



# Phrase Trigger
# Question 9

class PhraseTrigger(WordTrigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        phrase = self.phrase
        return phrase in story.get_title()\
or phrase in story.get_summary() or phrase in \
story.get_subject()

#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    nstories = []
    for i in range(len(stories)):
        for e in range(len(triggerlist)):
            if triggerlist[e].evaluate(stories[i]):
                nstories.append(stories[i])
                break
    return nstories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(trigger_map, trigger_type, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and returns a new
    trigger instance.

    trigger_map: dictionary with names as keys (strings) and triggers as values
    trigger_type: string indicating the type of trigger to make (ex: "TITLE", "AND")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"], ["t2", "t3"])
    name: a string representing the name of the new trigger (ex: "t1", "t2")

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).

    Modifies trigger_map, adding a new key-value pair for this trigger.
    """
    if trigger_type == "TITLE":
        trigger = TitleTrigger(params[0])

    elif trigger_type == "SUBJECT":
        trigger = SubjectTrigger(params[0])

    elif trigger_type == "SUMMARY":
        trigger = SummaryTrigger(params[0])

    elif trigger_type == "NOT":
        trigger = NotTrigger(trigger_map[params[0]])

    elif trigger_type == "AND":
        trigger = AndTrigger(trigger_map[params[0]], trigger_map[params[1]])

    elif trigger_type == "OR":
        trigger = OrTrigger(trigger_map[params[0]], trigger_map[params[1]])

    elif trigger_type == "PHRASE":
        trigger = PhraseTrigger(" ".join(params))

    else:
        return None

    trigger_map[name] = trigger


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    triggers = []
    trigger_map = {}
    for line in lines:
        linesplit = line.split(" ")
        if linesplit[0] != "ADD":
            trigger = makeTrigger(trigger_map, linesplit[1], linesplit[2:], linesplit[0])
        else:
            for name in linesplit[1:]:
                triggers.append(trigger_map[name])
    return triggers


import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

