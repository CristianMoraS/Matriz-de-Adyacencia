#assume you stored every line of your input as a tuples (eventid, mnbr).
observations = [(20, 1), (26, 1), (12, 2), (14, 2), (15,3 ), (14, 3), (10, 3)]

#then creates an event link dictionary. i.e something that link every event to all its mnbrs
eventLinks = {}

for (eventid, mnbr) in observations :
       #If this event have never been encoutered then create a new entry in links
       if not eventid in eventLinks.keys():
           eventLinks[eventid] = []

       eventLinks[eventid].append(mnbr)

#collect the mnbrs
mnbrs = set([mnbr for (eventid, mnbr) in observations])

#create a member link dictionary. This one link a mnbr to other mnbr linked to it.
mnbrLinks = { mnbr : set() for mnbr in mnbrs }

for mnbrList in eventLinks.values() :
       #add for each mnbr all the mnbr implied in the same event.
       for mnbr in mnbrList:
           mnbrLinks[mnbr] = mnbrLinks[mnbr].union(set(mnbrList))

print(mnbrLinks)
