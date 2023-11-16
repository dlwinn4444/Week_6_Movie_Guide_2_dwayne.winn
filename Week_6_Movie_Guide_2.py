#Dwayne Winn CSI261 week 4 MOVIE GUIDE part 2



#set first three movies in list


from _pytest.junitxml import filename_arg

#start main
def main():
    #write movies.txt
    with open("movies.txt", "w") as file:
         file.write("Cat on a Hot Tin Roof\nOn the Waterfront\nMonty Python and the Holy Grail")
    #
    m_list = []  
    c_choice = ""
    f_name = "movies.txt"
    #run set first list function
    b_list(f_name,m_list)
    while c_choice != "exit":
          # call main menu function and get command
          c_choice = m_menu()
          print(c_choice)
          # check command from last function
          if c_choice == "list":
             d_list(m_list)
          elif c_choice== "add":
              c_add(m_list)
              wto_file(m_list)
              
          elif c_choice == "del":
              c_del(m_list)
              wto_file(m_list)
          elif c_choice==  "exit":
                break  
          else:
               print("Not a valid command. Please try again.")
    print("Thank you!") 


  
# Main Menu fuction
def m_menu():
    # display main menu
    print("The Movie list Program")
    print()
    print("Command Menu")
    print("list - list all movies")
    print("add - add a movie")
    print("del - delete a movie")
    print("exit - exit program")
    #get user Input 
    c_choice = input("Command: ")
    return c_choice
    
     
# write List movie functions
def b_list(f_name,m_list):
    
    with open(f_name, "r") as file:
         movies = file.read().split("\n")
         for movie in movies:
              m_list.append(movie)          
         return m_list
#display movie lisr
def d_list(m_list):
    
    print("Movie titles")
    print()
    for i, movie in enumerate(m_list, start = 1):
        print(i,": ",movie)
    return m_list 
             
          
#add movie functions
def c_add(m_list):
    
    #user input
    movie = input("Movie name: ")
    # add movie to list
    m_list.append(movie)
    print(movie," was added.")
    return m_list
   
#delete movie functions  

    
    #show list
    d_list(m_list)
    n_movie = int(input("Choose movie to delete: :"))
    if n_movie < 1 or n_movie > len(m_list):
       print("Invalid movie number.")
       print()
    else:
       #del movie 
       movie = m_list.pop(n_movie - 1)
       print(movie," was deleted.")
       return m_list
   
   
#write new list after changes
def wto_file(m_list):
    with open("movies.txt", "w") as file:
       for movie in m_list:
          file.write(movie + "\n") 
          return
if __name__ == '__main__':
     main()