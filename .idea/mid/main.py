from decimal import Decimal
import itertools
import time

'''
Function Definitions
'''

# Association rules generator for support item sets
def associationRules(supportList, supportListCount):
    ruleCount = 0
    for ele in supportList:
        eleSupport = supportListCount[supportList.index(ele)]
        for item in supportList:
            if((len(item) == len(ele) - 1) and set(item).issubset(ele)):
                itemSupport = supportListCount[supportList.index(item)]
                ruleConfidence = (eleSupport / itemSupport) * 100
                if ruleConfidence >= minConfidence:
                    if ele > item:
                        ruleCount += 1
                        print()
                        print(' , '.join(str(x) for x in item)+' ------> '+' , '.join(str(e) for e in set(ele)-set(item))+'\tSupport:'+ str(round(Decimal(eleSupport/len(transactions)*100), 1))+'%\tconfidence:'+str(round(Decimal(ruleConfidence), 1))+' %')
    if(ruleCount == 0):
        print('No Association Rules can be formed')


# Frequent item set generator based on transactions and minimum support
def getFrequentItemSet(transactions, listOfItemSet, minSupportItems):
    list = []
    for itemSet in listOfItemSet:
        itemSetOccurence = countItemSetOccurence(transactions, itemSet)
        if itemSetOccurence >= minSupportItems:
            supportList.append(itemSet)
            supportListCount.append(itemSetOccurence)
            list.append(itemSet)
    return list


# Item set generator by creating item combinations
def combineItems(itemSets, setItems):
    combineList = []
    for combination in itertools.combinations(itemSets, 2):
        temp = [] + combination[0]
        for item in combination[1]:
            if item not in temp:
                temp.append(item)
        if compareList(combineList, temp) == False and len(temp) == setItems:
            combineList.append(temp)
    return combineList



def countItemSetOccurence(transactions, itemSet):
    count = 0
    for transaction in transactions:
        findAll = True
        for item in itemSet:
            if item not in transaction:
                findAll = False
                break
        if findAll:
            count += 1
    return count




def compareList(list, item):
    for ele in list:
        if(set(ele) - set(item) == set([])):
            return True
    return False


'''
Script Start Point
'''

database = 1
print('Choose the database')
print('1 for supermarket\n2 for electronics\n3 for cloths\n4 for Kmart\n5 for Home Depot')
database = input()
minSupport = float(input('Enter minimum support (in %)'))
minConfidence = float(input('Enter minimum confidence (in %)'))


# Loading the data
start_time = time.time()
fileObject = open('A://NewFolder/dataset'+str(database)+'.txt', 'r')
transactions = []
items = []

for line in fileObject:
    tokenList = line.split(' ')
    itemsInCurrentTransaction = tokenList[1].rstrip('\n').split(',')
    transactions.append(itemsInCurrentTransaction)
    for item in itemsInCurrentTransaction:
        if item not in items:
            items.append(item)

print('\nITEMS\n')
no=1
for x in items:
    print(no,' '+str(x))
    no+=1

print('\nTRANSACTIONS\n')
for x in transactions:
    print('\n'+str(x))


minSupportItems = ((minSupport * len(transactions)) / 100)
noOfItems = len(items)

listOfItemSet = []

# Creating initial list of item set
for item in items:
    listOfItemSet.append([item])

supportList = []
supportListCount = []

# Generating the first set of frequent item
frequentItemSet = getFrequentItemSet(transactions, listOfItemSet, minSupportItems)

setItems = 2
while True:
    if len(frequentItemSet) < 2:
        break
    else:
        # Generating the combination of items from frequent set
        candidateSet = combineItems(frequentItemSet, setItems)
        # Updating the frequent set with new combinations
        frequentItemSet = getFrequentItemSet(transactions, candidateSet,minSupportItems)
        setItems += 1

# Generating the Association Rules
print('\n\n\nAssociation Rules \n')
associationRules(supportList, supportListCount)
print("\n--- Time taken to calculate the Association Rules is %s seconds ---\n" % (time.time() - start_time))
