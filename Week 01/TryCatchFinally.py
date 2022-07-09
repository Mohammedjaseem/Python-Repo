while True:
    try:
       x=int(input('Enteranumber:'))
       print("works")
       break
    except:
       print('That\'snotavalid number!')
       print('Please try again...')
    finally:
        print("\nAttempted Input\n")