swimming = int(input('Enter the time in minutes to complete your swimmming race: '))
cycling = int(input('Enter the time in minutes to complete your cycling race: '))
running = int(input('Enter the time in minutes to complete your running race: '))

tot = swimming + cycling + running

if tot <= 100: 
    print('Provincial Colours')

elif tot <= 105: 
    print('Provincial Half Colours')

elif tot <= 110: 
    print('Provincial Scroll')

elif tot > 110: 
    print('No award')
