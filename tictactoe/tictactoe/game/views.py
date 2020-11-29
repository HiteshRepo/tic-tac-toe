from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

theBoard = None
board = None
message = None
turn = None
count = None
lstNum = ['1','2','3','4','5','6','7','8','9']

def game(move):

    global message
    global theBoard
    global lstNum
    global turn
    global count

    message = ""

    print(turn)
    print(count)

    if theBoard[move] in lstNum:
        theBoard[move] = turn
        count += 1
    else:
        message = "That place is already filled. Move to another place?"
        return redirect('home')
    
    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] not in lstNum: # across the top
            message = "Game Over."            
            message += " **** " +turn + " won. ****"            
            return redirect('home')
        if theBoard['1'] == theBoard['2'] == theBoard['3']  not in lstNum: # across the bottom
            message = "Game Over."            
            message += " **** " +turn + " won. ****"            
            return redirect('home')
        if theBoard['1'] == theBoard['4'] == theBoard['7']  not in lstNum: # down the left side
            message = "Game Over."            
            message += " **** " +turn + " won. ****"            
            return redirect('home')
        if theBoard['2'] == theBoard['5'] == theBoard['8']  not in lstNum: # down the middle
            message = "Game Over."            
            message += " **** " +turn + " won. ****"            
            return redirect('home')
        if theBoard['3'] == theBoard['6'] == theBoard['9']  not in lstNum: # down the right side
            message = "Game Over."            
            message += " **** " +turn + " won. ****"            
            return redirect('home')
        if theBoard['7'] == theBoard['5'] == theBoard['3']  not in lstNum: # diagonal
            message = "Game Over."            
            message += " **** " +turn + " won. ****"            
            return redirect('home')
        if theBoard['1'] == theBoard['5'] == theBoard['9']  not in lstNum: # diagonal
            message = "Game Over."            
            message += " **** " +turn + " won. ****"            
            return redirect('home')

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            message = "Game Over."               
            message += "It's a Tie!!"
            return redirect('home')

    # Now we have to change the player after every move.
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'
    return redirect('home')        

def printBoard():
    global theBoard
    global board

    board = []

    board.append(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])#.replace(' ', '*'))
    board.append('-+-+-')
    board.append(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])#.replace(' ', '*'))
    board.append('-+-+-')
    board.append(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])#.replace(' ', '*'))

def setup():
    global theBoard
    global board
    global count
    global turn
    global message

    theBoard = {'7': '7' , '8': '8' , '9': '9' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '1': '1' , '2': '2' , '3': '3' }

    board = []
    count = 0
    turn = 'X'
    message = ''
    

def home(request):
    global theBoard
    global board
    global message

    if request.user.is_authenticated:
        if not theBoard:
            setup()
        printBoard()
        if not message:
            message = 'Message will be displayed here!!'
        return render(request, 'home.html', {'board' : board, 'loc' : '', 'msg' : message})
    else:
        setup()
        return render(request, 'home.html', {'board' : [], 'loc' : '', 'msg' : 'Hi'})

    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:   
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form' : form})

def change(request):
    if request.method == 'POST':
        game(request.POST.dict()['loc'])
    return redirect('home')

def reset(request):
    setup()
    return redirect('home')
