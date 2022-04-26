# https://leetcode.com/discuss/interview-question/1002811/Amazon-or-OA-2021-or-Fresh-Promotion
'''
Amazon is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.

Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana

Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.

Output
Return an integer 1 if the customer is a winner else return 0.

Note
'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Example 1:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
Output: 1
Explanation:
codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.

Example 2:

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

Example 3:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [apple, banana, apple, banana, orange, banana]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in an order which is not following the order of fruit names in the first group.

Example 4:

Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]
Output: 0
Explanation:
The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.
'''

####################################################################################################
'''
I think this is pattern matching actually
https://leetcode.com/problems/regular-expression-matching/
'''
###################################################################################################

# Python3 using 2-pointer approach: O(N) where N=len(cart)

class FreshPromo2:

    def __findCartIdx(self, cartIdx, code):
        codeIdx = 0
        for idx in range(cartIdx, self.numCart):
            if self.cart[idx] == code[codeIdx] or code[codeIdx] == 'anything':
                codeIdx += 1
                if codeIdx == len(code):
                    return idx
            else:
                codeIdx = 0
        return -1

    def isWinner(self, cart, codes):
        self.cart = cart
        self.numCart = len(self.cart)
        if self.numCart == 0: return False
        totalCodes = 0
        for code in codes: totalCodes += len(code)
        if totalCodes == 0 or totalCodes > self.numCart: return False

        cartIdx = 0
        for code in codes:
            cartIdx = self.__findCartIdx(cartIdx, code)
            if cartIdx < 0: return False
            cartIdx += 1
        return True
      
     
    
###################################################################################################
# REGEX IDEA

def freshPromotion(shoppingCart, codeList) -> int:
    s = ' '.join(shoppingCart)
    print(s)
    reg = ''
    for code in codeList:
        c = ' '.join(code)
        c = ' ' + c
        c = c.replace('anything', '\w+')
        reg += c + '[\w\s]*'
    r = re.compile(reg)
    res = r.findall(s)
    return min(1, len(res))
  
  
  
#####################################################################################################
# TWO STACKS
# %100 test cases passed JAVA solution with two stack.

	public class FreshPromotion {

	  public static int foo(List<String> codeList, List<String> shoppingCart) {
		Stack<String> orderStack = new Stack<>();
		Stack<Stack<String>> codeStack = new Stack<>();
		boolean isFound = false;
		String orderFruit = "";
		String prevCodeFruit = "";

		if (codeList.isEmpty()) {
		  return 1;
		}

		pushCodeStack(codeList, codeStack);
		pushOrderStack(shoppingCart, orderStack);

		while (!codeStack.isEmpty()) {
		  Stack<String> codeFruitStack = codeStack.pop();
		  isFound = false;
		  while (!codeFruitStack.isEmpty()) {
			String codeFruit = codeFruitStack.pop();
			if (orderStack.isEmpty()) {
			  return 0;
			}

			if (isFound) {
			  orderFruit = orderStack.pop();

			  if (!checkFruit(codeFruit, orderFruit)) {
				isFound = false;
				codeFruitStack.push(prevCodeFruit);
			  }
			}

			while (!isFound && !orderStack.isEmpty()) {
			  orderFruit = orderStack.pop();
			  if (checkFruit(codeFruit, orderFruit)) {
				isFound = true;
			  }
			}

			prevCodeFruit = codeFruit;
		  }
		}

		if (!isFound && orderStack.isEmpty()) {
		  return 0;
		}

		return 1;
	  }

	  private static void pushOrderStack(List<String> shoppingCart, Stack<String> orderStack) {
		for (int j = shoppingCart.size() - 1; j >= 0; j--) {
		  orderStack.push(shoppingCart.get(j));
		}
	  }

	  private static void pushCodeStack(List<String> codeList, Stack<Stack<String>> codeStack) {
		for (int j = codeList.size() - 1; j >= 0; j--) {
		  Stack<String> stringStack = new Stack<>();
		  String code = codeList.get(j);
		  String[] codeFruits = code.split(" ");

		  for (int i = codeFruits.length - 1; i >= 0; i--) {
			stringStack.push(codeFruits[i]);
		  }
		  codeStack.push(stringStack);
		}
	  }

	  private static boolean checkFruit(String codeFruit, String orderFruit) {
		if (codeFruit.equalsIgnoreCase("anything")) {
		  return true;
		} else if (codeFruit.equalsIgnoreCase(orderFruit)) {
		  return true;
		} else {
		  return false;
		}
	  }

	}
