def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = input('input celsius: ')
    fahrenheit = (int(celsius) * 9/5) + 32
    print (f'fahrenheit \t {fahrenheit:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()

