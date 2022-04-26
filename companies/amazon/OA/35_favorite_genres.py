# https://leetcode.com/discuss/interview-question/373006/Amazon-or-OA-2019-or-Favorite-Genres
'''
Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
Example 2:

Input:
userSongs = {  
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
},
songGenres = {}

Output: {  
   "David": [],
   "Emma":  []
}
'''

##########################################################################################

def favor(userSongs, songGenres):
    res = {}
    d = {s: g for g in songGenres for s in songGenres[g]}
    for name, songs in userSongs.items():
        c = collections.Counter(d[s] for s in songs if s in d)
        mxcnt = max(c.values() or [0])
        res[name] = [g for g in c if c[g] == mxcnt]
    return res
  
'''
 The creation of d is only O(numSongs) due to the every song has only one genre constraint. So, numGenres <= numSongs and creation of d is basically covering every song.

The for loop part to construct res is O(numUsers * numSongs) in the worst case if every user likes every song.
'''

##########################################################################################
# https://leetcode.com/playground/FneysqCB

def initialize():
    userSongs = {  
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    }
    songGenres = {  
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }
    return userSongs, songGenres

def favor(userSongs, songGenres):
    res = {}
    # inverting the mapping to dict[song] : genre
    d = {s: g for g in songGenres for s in songGenres[g]}
    # loop over userSongs[name] : songs
    for name, songs in userSongs.items():
        c = collections.Counter(d[s] for s in songs if s in d)
        #print(c)
        mxcnt = max(c.values() or [0])
        res[name] = [g for g in c if c[g] == mxcnt]
    return res

if __name__ == '__main__':
    userSongs, songGenres = initialize()
    print(favor(userSongs, songGenres))
