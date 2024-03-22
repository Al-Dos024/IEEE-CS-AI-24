# P(B∣A)= P(A∩B) / P(A)

event_a = input("Enter a list of numbers separated by spaces for event A: ").split()
event_a = [int(i) for i in event_a]  

event_b = input("Enter a list of numbers separated by spaces for event B: ").split()
event_b = [int(i) for i in event_b]  

# Total Events in A
total_a = event_a.count(1)  

# Total Events in A and B
total_a_b = sum(1 for i in range(len(event_a)) if event_a[i] == 1 and event_b[i] == 1)

# Handle division by zero if event A never occurs
if total_a == 0:  
    print("cant be done")
    exit()
    
print(total_a_b / total_a)

