from errbot import BotPlugin, re_botcmd


class Lmgtfy(BotPlugin):
    """
    For all those people who find it more convenient to bother you with their
    question rather than search it for themselves.
    """

    MSG = (
        "Hey! You seem to have asked a question which could have been solved "
        "by other means easily.Click [this]({}) When you ask a question, be "
        "sure to try out a few things first - you're in a much better position "
        "to help yourself then we are. Try googling, thinking, the GitHub "
        "search or git grep if you are looking for source code."
        "[StackOverflow](http://stackoverflow.com/help/how-to-ask) "
        "has a good guide on how to ask questions in a way that allows us to "
        "help you even faster!"
    )

    @re_botcmd(pattern=r"lmgtfy\s+(.+)")
    def lmgtfy(self, msg, match):
        link = "https://www.lmgtfy.com/?q=" + match.group(1)
        return self.MSG.format(link)
