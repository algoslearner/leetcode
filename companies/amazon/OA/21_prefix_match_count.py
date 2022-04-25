# https://leetcode.com/discuss/interview-question/1276002/Amazon-OA
'''
Amazon Frontend OA

Prob 1: Given an array of strings input : ["Jacky" , "Jack", "Jackster"] and a query : ["Jack"] return number of string items for which query is the prefix but doesn't match the whole input. In this case it will be [2] as Jack is prefix for "Jacky" and "Jackster" but matches word by word with "Jack" so that won't be counted.
Prob 2 : https://leetcode.com/discuss/interview-question/862371/VISA-online-Assignment/708848

Easy one took me max 7-10 mins to wrap it up.
'''

public static void main(String[] args) {
  String[] array = new String[]{"Jacky" , "Jack", "Jackster"};
  String query = "Jack";
  int count=0;
  for (String value : array) {
    int index = value.indexOf(query);
    if (value.equals(query) || index == -1) continue;
    if(index==0) count++;
  }
  System.out.println(count);
}
