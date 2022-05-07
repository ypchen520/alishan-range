# [Google Developers](https://www.youtube.com/watch?v=LDRbO9a6XPU)

from numpy import column_stack


training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

# Column labels.
# These are used only to print the tree.
header = ["color", "diameter", "label"]

## Utility function 

def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    return set([row[col] for row in rows])

#######
# Demo:
# print(unique_vals(training_data, 0))
# unique_vals(training_data, 1)
#######

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)

#######
# Demo:
# print(is_numeric(7))
# print(is_numeric("Red"))
#######   

def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {} # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

#######
# Demo:
# print(class_counts(training_data))
#######

def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return
    # Print the question at this node
    print(spacing + str(node.question))
    # Call this function recursively on the true branch
    print(spacing + "--> True:")
    print_tree(node.true_branch, spacing + "  ")
    # Call this function recursively on the false branch
    print(spacing + "--> False:")
    print_tree(node.false_branch, spacing + "  ")

class Decision_Node:
    def __init__(self):
        pass

class Leaf:
    def __init__(self):
        pass

class Question:
    """A Question is used to partition a dataset.

    This class just records a 'column number' (e.g., 0 for Color) and a
    'column value' (e.g., Green). The 'match' method is used to compare
    the feature value in an example to the feature value stored in the
    question. See the demo below.
    """
    def __init__(self, column, value):
        self.column = column
        self.value = value
        
    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value
        
    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        pass

def partition(rows, question):
        """Partitions a dataset.

        For each row in the dataset, check if it matches the question. If
        so, add it to 'true rows', otherwise, add it to 'false rows'.
        """
        true_rows, false_rows = [], []
        for row in rows:
            if(question.match(row)):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows

#######
# Demo:
# Let's partition the training data based on whether rows are Red.
true_rows, false_rows = partition(training_data, Question(0, 'Red'))
# This will contain all the 'Red' rows.
# print(true_rows)
# This will contain everything else.
# print(false_rows)
#######

def gini(rows):
    """Calculate the Gini Impurity for a list of rows.

    There are a few different ways to do this, I thought this one was
    the most concise. See:
    https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity
    """
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

#######
# Demo:
# Let's look at some example to understand how Gini Impurity works.
#
# First, we'll look at a dataset with no mixing.
no_mixing = [['Apple'],
              ['Apple']]
# this will return 0
# print(gini(no_mixing))
# Now, we'll look at dataset with a 50:50 apples:oranges ratio
some_mixing = [['Apple'],
               ['Orange']]
# this will return 0.5 - meaning, there's a 50% chance of misclassifying
# a random example we draw from the dataset.
# print(gini(some_mixing))
# Now, we'll look at a dataset with many different labels
lots_of_mixing = [['Apple'],
                  ['Orange'],
                  ['Grape'],
                  ['Grapefruit'],
                  ['Blueberry']]
# This will return 0.8
print(gini(lots_of_mixing))
#######

def info_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1-p) * gini(right)

#######
# Demo:
# Calculate the uncertainy of our training data.
current_uncertainty = gini(training_data)
print(current_uncertainty)
# How much information do we gain by partioning on 'Green'?
true_rows, false_rows = partition(training_data, Question(0, 'Green'))
print(info_gain(true_rows, false_rows, current_uncertainty))
# What about if we partioned on 'Red' instead?
true_rows, false_rows = partition(training_data, Question(0,'Red'))
print(info_gain(true_rows, false_rows, current_uncertainty))
# It looks like we learned more using 'Red' (0.37), than 'Green' (0.14).
# Why? Look at the different splits that result, and see which one
# looks more 'unmixed' to you.
true_rows, false_rows = partition(training_data, Question(0,'Red'))
# Here, the true_rows contain only 'Grapes'.
print(true_rows)
# And the false rows contain two types of fruit. Not too bad.
print(false_rows)
# On the other hand, partitioning by Green doesn't help so much.
true_rows, false_rows = partition(training_data, Question(0,'Green'))
# We've isolated one apple in the true rows.
print(true_rows)
# But, the false-rows are badly mixed up.
print(false_rows)
#######

def find_best_split(rows):
    pass

def classify():
    pass