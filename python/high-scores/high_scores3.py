from heapq import nlargest

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
    	return self.scores[-1]

    def highest(self):
    	return max(self.scores)

    def top(self):
    	return nlargest(3, self.scores)

    def report(self):
    	if self.latest() == self.highest():
    		return "Your latest score was %d. That's your personal best!" %self.latest()
    	else:
    		return "Your latest score was %d. That's %d short of your personal best!" % (self.latest(), self.highest() - self.latest())