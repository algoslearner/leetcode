# https://leetcode.com/discuss/interview-question/846585/Amazon-Online-Assessment-Question-1
'''
Input
The input to the function/method consists of five arguments - numCompetitors, an integer representing the number of competitors for the Echo device;
topNCompetitors, is an integer representing the maximum number of competitors that Amazon wants to identify;
competitors, a list of strings representing the competitors;
numReviews, an integer representing the number of reviews from different websites that are identified by the automated webcrawler;
reviews, a list of string where each element is a string that consists of space-separated words representing user reviews.

Output
Return a list of strings representing Amazon's top N competitors in order of most frequently mentioned to least frequent.

Note
The comparison of strings is case-insensitive. If the value of topNCompetitors is more than the number of competitors discussed in the reviews then output the names of only the competitors mention.
If competitors have the same count (e.g. newshop=2, shopnow=2, mymarket=4), sort alphabetically. topNCompetitors=2, Output=[mymarket, newshop]

Example
Input:
numCompetitors=6
topNCompetitors = 2
competitors = [newshop, shopnow, afashion, fashionbeats, mymarket, tcellular]
numReviews = 6
reviews = [
"newshop is providing good services in the city; everyone should use newshop",
"best services by newshop",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks Newshop for the quick delivery"]

Output
["newshop", "fashionbeats"]

Explanation
"newshop" is occurring in 3 different reviews. "fashionbeats" is occuring in 2 different user reviews and "mymarket" is occurring in only 1 review.

public List<string> TopNumCompetitors(int numCompetitors,
                                        int topNCompetitors,
                                        List<string> competitors,
                                        int numReviews, List<string> reviews)
{
	// Your code here
}
'''

########################################################################################################
# SOLUTION 1
# Time: O(N^2) - we have to loop through the dictionary n amount of times to get the greatest results.
# Space - O(N) - created dictionary counting the inputs
# Sort the comps array first so that it will always come out in alphabetical order if tied.

def topcompetitors(numComp, topComp, comps, numReviews, reviews):
    comps.sort()
    d = {}
    output = []
    for i in comps:
        d[i] = 0

    for review in reviews:
        review = review.split()
        for word in review:
            if word in d:
                d[word] += 1
                break

    for _ in range(topComp):
        maxval = 0
        maxkey = ''
        for key, val in d.items():
            if val > maxval:
                maxval = val
                maxkey = key
        output.append(maxkey)
        del d[maxkey]
    return output


numComp = 6
topComp = 2
comps = ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular']
numReviews = 6
reviews = [
    "newshop is providing good services in the city; everyone should use newshop",
    "best services by newshop",
    "fashionbeats has great services in the city",
    "I am proud to have fashionbeats",
    "newshop has awesome services",
    "Thanks newshop for the quick delivery"]

print(topcompetitors(numComp, topComp, comps, numReviews, reviews))

########################################################################################################
# SOLUTION 2
# Python solution using Dictionary + Heap

# N: top N competitors
# C: # of competitors 
# R: # of reviews
# W: avg # of words in a review
# Time complexity: O(C + R * (W + N))
# Space complexity: O(C + N)

import heapq


class HeapNode:

    def __init__(self, competitor):
        self.competitor = competitor
        self.count = 0

    def __gt__(self, other):
        if self.count != other.count:
            return self.count > other.count
        else:
            return self.competitor > other.competitor

def topNumCompetitors(numCompetittors, topNCompetitors, competitors, numReveiws, reviews):
    hashTable = {} # Space O(C)
    for competitor in competitors: # Time O(C)
        hashTable[competitor] = HeapNode(competitor)
    # Min heap and will always kick out the competitor who has the most less freq count
    heap, heapHash = [], {} # Space O(N)
    for review in reviews: # Time O(R)
        words = review.split()
        for word in words: # Time O(W)
            if word.lower() in hashTable:
                # Found competitor
                break
        competitor = word.lower()
        if competitor in heapHash:
            heapNode = heapHash[competitor]
            heapNode.count += 1
            heapq.heapify(heap) # Time O(N)
        else:
            heapNode = hashTable[competitor]
            heapNode.count += 1
            heapq.heappush(heap, heapNode) # Time O(logN)
        heapHash[competitor] = heapNode
        if len(heap) > topNCompetitors:
            victim = heapq.heappop(heap)
            del heapHash[victim.competitor]
    return [heapNode.competitor for heapNode in heapHash.values()]

if __name__ == '__main__':
    print(topNumCompetitors(6, 2, ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular'], 6,  [
"newshop is providing good services in the city; everyone should use newshop",
"best services by newshop",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks Newshop for the quick delivery"])) # Output ['newshop', 'fashionbeats']
    
    
####################################################################################
# SOLUTION 3

def findNcompititors(numCompetitors,topNCompetitors,competitors,numReviews,reviews):
    dt = {}
    for i in competitors:
        dt[i] = 0
    for review in reviews:
        temp = review.lower()
        #print(temp)
        for i in competitors:
            if i in temp:
                dt[i]+=1
                break
    sorted_map = sorted(dt, key=dt.get, reverse=True)
    res = []
    res = sorted(dt, key=lambda x: (-dt[x], x))
    return res[:topNCompetitors]

####################################################################################
# SOLUTION 4
# Top-N Competitor Problem: https://leetcode.com/playground/Y7wiv8Md

// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        List<String> reviews = new ArrayList(
				Arrays.asList(
                    "newshop is providing good services in the city; everyone should use newshop",
			        "best services by newshop's friendly staff", 
                    "fashionbeats has great services in the city",
					"I am proud to have fashionbeats's shoes.", 
                    "mymarket has awesome services",
					"Thanks newshop. You're better than fashionbeats."));

		List<String> competitors = new ArrayList<String>(
				Arrays.asList("newshop", "shopnow", "afashion", "fashionbeats", "mymarket", "tcellular"));

		System.out.println(topNumCompetitors(6, 2, competitors, 6, reviews));
    }
    private static List<String> topNumCompetitors(int numCompetitors,
                                        int topNCompetitors,
                                        List<String> competitors,
                                        int numReviews, List<String> reviews){
        
        Set<String> competitorSet = new HashSet<>();
        competitorSet.addAll(competitors);
        
        Map<String, Integer> competitorOccurenceMap = new HashMap<>();
        for(String competitor : competitors){
            competitorOccurenceMap.put(competitor, 0);
        }
        
        for(String review : reviews){
            Set<String> repeatingNameSet = new HashSet<>();
            //review = review.replaceAll("[^a-zA-Z0-9]", " ");
            String[] words = review.split("\\W");
            for(String word : words){
                if(competitorSet.contains(word) && !repeatingNameSet.contains(word)){
                    competitorOccurenceMap.put(word, competitorOccurenceMap.get(word)+1);
                    repeatingNameSet.add(word);
                }
            }
        }
        /*
        for(Map.Entry<String, Integer> entry : competitorOccurenceMap.entrySet()){
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
        */
        
        PriorityQueue<String> minHeap = new PriorityQueue<String>(
                                        (c1, c2) -> competitorOccurenceMap.get(c1) == competitorOccurenceMap.get(c2) ? c2.compareTo(c1) : competitorOccurenceMap.get(c1) - competitorOccurenceMap.get(c2));
        
        for(String competitor : competitors){
            minHeap.offer(competitor);
            
            if(minHeap.size() > topNCompetitors){
                minHeap.poll();
            }
        }
        
        List<String> result = new ArrayList<>();
        while(!minHeap.isEmpty()){
            result.add(0, minHeap.poll());
        }
        
        return result;
    }
}
