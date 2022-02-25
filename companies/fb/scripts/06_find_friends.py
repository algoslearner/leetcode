'''
Given the CSV with the belowing information :
StartTime,user1,user2,action

There are 4 possible actions : REQUEST,ACCEPT,REJECT,REMOVE
REMOVE is only possible when users already be friend.

Going through the csv, determine the list of users who are friends.
csv format : (Thanks @alex_bb)
StartTime,user1,user2,action
10/01/2001 02:12 PM, UserA,UserB,ACCEPT
11/04/2019 12:47 PM, UserC,UserE,ACCEPT
12/01/2012 05:23 PM, UserA,UserD,ACCEPT
10/12/2012 02:00 PM, UserE,UserB,ACCEPT
03/01/2001 03:32 PM, UserA,UserJ,ACCEPT
10/01/2019 02:37 PM, UserP,UserB,ACCEPT
03/01/2018 02:28 PM, UserC,UserD,REQUEST
10/12/2016 09:00 PM, UserA,UserB,REJECT
10/01/2005 02:34 PM, UserA,UserB,ACCEPT
03/19/2019 09:38 PM, UserD,UserB,REQUEST
10/18/2008 02:27 PM, UserC,UserB,REMOVE
10/24/2001 02:26 PM, UserA,UserE,REJECT
10/01/2019 03:34 PM, UserA,UserJ,REJECT
06/01/2016 05:00 PM, UserC,UserJ,ACCEPT
12/01/2018 02:22 PM, UserD,UserB,REQUEST
11/15/2019 02:00 PM, UserA,UserB,REQUEST
10/01/2001 03:17 PM, UserA,UserJ,REJECT
12/01/2019 02:32 PM, UserC,UserP,REJECT
10/01/2019 02:22 PM, UserE,UserE,ACCEPT
03/16/2019 02:13 PM, UserA,UserD,REQUEST
10/01/2001 03:21 PM, UserP,UserB,REQUEST
03/01/2019 05:00 PM, UserC,UserJ,REJECT
10/25/2018 05:15 PM, UserA,UserB,ACCEPT
12/27/2016 02:00 PM, UserE,UserP,REMOVE
10/01/2001 03:21 PM, UserC,UserB,REJECT
03/01/2005 02:58 PM, UserA,UserE,ACCEPT
12/29/2019 02:19 PM, UserE,UserB,REMOVE
10/27/2001 03:12 PM, UserC,UserB,REMOVE
06/01/2019 09:43 PM, UserA,UserB,REMOVE
12/01/2001 02:12 PM, UserC,UserD,ACCEPT
12/11/2005 09:26 PM, UserA,UserE,REMOVE
06/05/2019 02:00 PM, UserC,UserB,ACCEPT
09/02/2016 09:12 PM, UserJ,UserB,REMOVE
09/02/2016 09:12 PM, UserJ,UserB,REMOVE
'''


# QUESTIONS asked
'''
Several questions to be asked :
[1] Are timestamps in sorted order with monotonic increase ?
[2] Type of user. Is it a userId ( integer) or a username (string) ?
[3] Are all the events valid ? Means can "ACCEPT" happen before "REQUEST". Can "REMOVE" happen before "ACCEPT". Can "REJECT" happen before "REQUEST".
[4] Is "friendship" relation Bi-directional ? Means if A->B sends request and B accepts it, Does B need to send 'A' a separate request or if A<->B are both each other's friend.
'''
