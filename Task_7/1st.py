probability_distribution = {}
data = input("Enter a list of numbers separated by spaces: ").split()
data = [int(i) for i in data]  
total_count = len(data)

for value in data:

    if value in probability_distribution:
        probability_distribution[value] += 1

    else:
        probability_distribution[value] = 1
    

for key in probability_distribution:
    probability_distribution[key] /= total_count
    
print(probability_distribution)
