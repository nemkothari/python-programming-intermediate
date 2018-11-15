## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i,x in enumerate(ships):
    print(x)
    print(cars[i])
    

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i,x in enumerate(things) :
    x.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled =[x*2 for x in apple_prices] 
apple_prices_lowered =[x-100 for x in apple_prices] 

## 5. Counting Female Names ##

name_counts ={}

for k in legislators:
    if (k[3] =="F") and ( k[7] > 1940):
        if k[1] in name_counts:
            name_counts[k[1]] = name_counts[k[1]]  +1
        else:
            name_counts[k[1]] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for i in values:
    if ( i is not None and i > 30):
        checks.append(True)
    else:
        checks.append(False)

## 8. Highest Female Name Count ##

max_value  = None

for i in name_counts:
    count = name_counts[i]
    if max_value  is None or count > max_value:
        max_value=count
        
        

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for i,x in plant_types.items():
    print(i)
    print(x)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for i,x in name_counts.items():
    if x ==2 :
        top_female_names.append(i)
        

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts={}

for i in legislators:
    if ( i[3]=="M" and i[7] > 1940):
        if i[1] in male_name_counts:
            male_name_counts[i[1]] = male_name_counts[i[1]] + 1
        else:
            male_name_counts[i[1]] = 1
            
highest_male_count = None
for name,count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

for name,count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)
        