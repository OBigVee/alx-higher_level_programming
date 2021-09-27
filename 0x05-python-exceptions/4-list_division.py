#!/usr/bin/python3                                                      
def list_division(my_list_1, my_list_2, list_length):                   
    division_list = []                                                  
    for element in range(0, list_length):                               
        try:                                                            
            quotient = my_list_1[element] / my_list_2[element]          
        except ZeroDivisionError:                                       
            print("division by 0")
            quotient = 0
        except (TypeError, ValueError):                                 
            print("wrong type")   
            quotient = 0
        except IndexError:                                              
            print("out of range")                                       
            quotient = 0                                                
        finally:                                                        
            division_list.append(quotient)                              
    return division_list
