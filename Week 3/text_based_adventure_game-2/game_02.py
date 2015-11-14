def main():
    '''Getting your name'''
    play_name=(raw_input("What's your name? > "))
    play_age=(raw_input("enter your age? >"))
    print ("hi"+" "+play_name)

    result="my name is {name} and my age is {age}".format (name=play_name, age=play_age)
    print(result)
    
if __name__ == '__main__':
    main()