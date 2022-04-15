'''
# https://leetcode.com/discuss/interview-question/1946698/Google-or-Onsite-or-Implement-match-method-for-Regular-Expression-Tree/1351804

I got the following question in the coding interview at Google.

Given a Tree Node representation for a regular expression, we consider the following cases:
// 'CHAR' a : matches only a, and not aa
// 'DISJ' a|b : matches a or b
// 'REP' a*: matches empty string or a or aa or aaa...
// 'CONCAT' a(b) : matches ab

Example: a(a|b)* valid examples: a, ab, aa, aab, aba, aaaaa, abbbb, ...

Represented in this tree:

                  CONCAT
               /         \
      CHAR (a)           REP
                         /
                     DISJ
                   /        \
                CHAR a    CHAR b
Provided the followng Class Node

enum Type {
    CHAR,
    DISJ,
    REP,
    CONCAT
}

static class Node {
    Type type;
    Node left; 
    Node right; 
    char c;
}
Impleent the Match method

    public static boolean isMatch(String s, Node n) {
    }
Edit: Moving my implementation to the comments to avoid confusing readers about the solution. https://leetcode.com/discuss/interview-question/1946698/Google-or-Onsite-or-Implement-match-method-for-Regular-Expression-Tree/1351804

I implemented the solution by traversing the tree as I mentioned in the comments and walked through the example and it seems to work.
However the interviewer said it doesn't work and said the method should take start and end instead of indx.
'''

##################################################################################
# TC
# SC

'''
This would be a hard problem if you never seen this topic before. This is basically from a compliers course on creating regular expressions.

Using the tree, construct the state machine graph using post order traversal. All edges in the state machine would have 3 values. (from, to, character)/

You have two primitives which are CHAR a and epsilon moves (basically free moves, empty string)

You need to know two things as you are building the state machine:

How to create small state machines for each of the types given
How to combine two state machines to create a larger state machine
REP has a tricky state machine graph.
The others are trivial.

After you built the graph. You need to perform dfs/bfs on the graph to see if you can match the string and reach a terminal state.
'''

counter = 0

class StateMachine:
      start; int
      terminal: int
      def __init(self, start, end):
              self.start = start
              self.terminal= end
              self.adjacents = defaultdict(set)
              
       def add_edge(self, v, w, char):
             self.adjacents[v].add((w, char))

       def adj_to(self, v):
            return self.adjancets[v]

       def nodes(self):
            for v in self.adjacents.keys():
                  for w, s in self.adj_to(v):
                       yield w,s

def epsilon():
       global counter
       start = counter + 1
       end = counter + 1  
       counter += 2
       sm = StateMachine(start, end)
       sm.add_edge(v,w, "")
       return sm

def char(s):
       global counter
       start = counter + 1
       end = counter + 1  
       counter += 2
       sm = StateMachine(start, end)
       sm.add_edge(v,w, s)
       return sm

def concat(sm1, sm2):
      """
      sm1 = left
      sm2 = right
      """
    sm1.add_edge(sm1.end, sm2.terminal, "")
     for (u,v,s) in sm2.nodes():
            sm1.add_edge(u,v,s)

    sm1.terminal  = sm2.terminal
    return sm1

def disjoint(sm1, sm2):
     """
      sm1 = left
      sm2 = right
      """
     counter += 1
     start= counter +1
     end = start+1
     sm0 = StateMachine(start, end)
     sm1.add_edge(start. sm1.start , "")
     for (u,v,s) in sm1.nodes():
            sm0.add_edge(u,v,s)
     sm1.add_edge(start. sm2.start , "")
     for (u,v,s) in sm2.nodes():
            sm0.add_edge(u,v,s)
    sm0.add_edge(sm1.end, end , "")
    sm0.add_edge(sm2.end, end , "")
    return sm0


def repeat(sm1):
      gloabal counter
      counter += 2
      start = counter + 1
      end = start  + 1
      sm = StateMachine(start, end)
      sm.add_edge(start, sm1.start. "")
      sm.add_edge(sm1.end, end. "")
      sm.add_edge(start, end, "")
      sm.add_edge(sm2.start, sm1.end, "")
      for (u,v,s) in sm1.nodes()
            sm.add_edge(u,v,s)
      return sm

def build(tree):
        if tree == None:
               return epsilon()
        sm_left = build(tree.left)
        sm_right = build(tree.right)
        if tree.type == Type .Char:
               return char(c)
        elif tree.type == Type.Concat:
               return concat(sm_left, sm_right)
       elif tree.type == Type.Disj:
               return disjoint(sm_left, sm_right)
       else tree.type == Type.Rep:
               -- assume that it always falls left, we could just always check, (this is trivial)
               return repeat(sm_left)
       else:
               raise Exception("invalid tree")

def match(query, node):
      graph = build(node)
      q = [(graph.start, 0)]
      while q:
           v, i = q.pop()
           if v == graph.end:
                 return True
           if i >= len(query):
                 continue
           for w, s in graph.adj_to(v):
                if s == "" or s == query[i]:
                   item = (w, i+1)
                   q.append(item)
      return False
