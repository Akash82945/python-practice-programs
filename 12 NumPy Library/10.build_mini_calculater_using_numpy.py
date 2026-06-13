import numpy as np


# Create mini calculater

print(f'''
        === 1D , 2D  Mini Calculater ===
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Diviosion
            5. Dot Product
            6. Mean of each
            7. Min of each
            8. Max of each
            9. Exit
            ''')

def calculater(num1, num2):
    
    while True:
        arr_a = np.array(num1)
        arr_b = np.array(num2)
        
        
        operation = int(input("\nEnter operation [1, 2, 3, 4, 5, 6, 7, 8, 9] :- "))
        
        try: 
            if operation == 1:
                print(f"\nAddition of Array.")
                print(f"{arr_a[0]} + {arr_b[0]} = {(arr_a + arr_b)[0]}")
                print(f"{arr_a[1]}   {arr_b[1]}   {(arr_a + arr_b)[1]}")
                # print(f"{arr_a} + {arr_b}\n = \n{arr_a + arr_b}")
            
            elif operation == 2:
                print(f"\nSubtraction of Array.")
                print(f"{arr_a[0]} - {arr_b[0]} = {(arr_a - arr_b)[0]}")
                print(f"{arr_a[1]}   {arr_b[1]}   {(arr_a - arr_b)[1]}")
                # print(f"{arr_a} - {arr_b} = {arr_a - arr_b}")
                
            elif operation == 3:
                print(f"\nMultlipcation of Array.")
                print(f"{arr_a[0]} * {arr_b[0]} = {(arr_a * arr_b)[0]}")
                print(f"{arr_a[1]}   {arr_b[1]}   {(arr_a * arr_b)[1]}")
                # print(f"{arr_a} X {arr_b} = {arr_a * arr_b}")
            
            elif operation == 4:
                print("\nDivision of Array.")
                divided_data = np.round(np.divide(arr_a, arr_b),2)
                print(f"{arr_a[0]} / {arr_b[0]} = {divided_data[0]}")
                print(f"{arr_a[1]}   {arr_b[1]}   {divided_data[1]}")
                # print(f"{arr_a}\n / \n{arr_b} = \n{(divided_data)}")
            
            elif operation == 5:
                print('\nDot Product of Array.')
                try:
                    dot_result = arr_a @ arr_b
                    print(f"{arr_a[0]} X {arr_b[0]} = {dot_result[0]}")
                    print(f"{arr_a[1]}   {arr_b[1]}   {dot_result[1]}")
                    
                    print(f"Dot product : \n{arr_a @ arr_b}")
                except ValueError as e:
                    print(f"Error : Shape not equal. {e}")
                
            elif operation == 6:
                print(f"\nArray A : \n{arr_a}")
                print(f"Array B : \n{arr_b}")
                print(f"\nMean of array_a : {np.mean(arr_a):.2f}")
                print(f"Mean of array_b : {np.mean(arr_b):.2f}")
                
            elif operation == 7:
                print(f"\nArray A : \n{arr_a}")
                print(f"Array B : \n{arr_b}")
                print(f"\nMin of array_a : {np.min(arr_a)}")
                print(f"Min of array_b : {np.min(arr_b)}")
                
            elif operation == 8:
                print(f"\nArray A : \n{arr_a}")
                print(f"Array B : \n{arr_b}")
                print(f"\nMax of array_a : {np.max(arr_a)}")
                print(f"Max of array_b : {np.max(arr_b)}")
                
            elif operation == 9:
                print("\nThank You. visit again.")
                break
                
            else:
                print("Error! Enter Valid Operation.")
                continue
            
        except ValueError as e:
            print(f"Error : {e}")

        
number1 = [[1,2],[3,4]]
number2 = [[5,6],[7,8]]
calculater(number1,number2)