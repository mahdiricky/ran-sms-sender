#random verse sender project
import requests,os,time,winsound,sys
from kavenegar import *

def connector():
    '''
    this function will connect us to our api
    '''
    global api,response
    os.system('cls')
    api='https://bible-api.com/?random=verse'
    response=requests.get(api)
    match response.status_code:
        case 200:
            print('The Connection Is OK')
        case _:
            print(f'We Have Problems In Connection\nProblem Code:{response.status_code}')
connector()

def json_file():
    '''
    then we want to load our json file
    '''
    global api,response,my_json_file,question
    my_json_file=response.json()
    print('\n')
    time.sleep(1)
    winsound.Beep(1000,100)
    print('Json File Loaded Succesfuly')
    try:
        question=int(input('Do You Want To See Json File Info (0=no,1=yes)?\n'))
    except:
        print("Please Enter Numeric Value")
        sys.exit(0)

    try:
        match question:
            case 0:
                print('Ok')
            case 1:
                print('\n',my_json_file,end='')
            case _:
                question=int(input('Do You Want To See Json File Info (0=no,1=yes)?\n'))
    except:
        print('Please Enter True Value')
        sys.exit(0)
json_file()

def sms_sender():
    '''
    this function will send the sms to the user that we want
    '''
    global api,response,my_json_file,question,fourth_question
    try:
        time.sleep(1)
        api2 = KavenegarAPI('Your Api Key') #You need an Apikey to send sms please buy once at https://kavenegar.com/
        params = {
            'sender': '09...',#The sender phone number(yourself) or the number that you bought from kavenegar
            'receptor' : f'{fourth_question}',#The recievers
            'message' : f"{my_json_file['verses'][0]['text']}"
        } 
        response2 = api2.sms_send(params)
        print(f'Your Sms Response Is:{response2}')
    except:
        print('''We Have An Error In Sending Messages To User Please Try Again!''')
        os._exit(0)

def edit_data():
    '''
    we will edit the data that we have
    '''
    global api,response,my_json_file,question,fourth_question
    print('\n')
    try:
        second_question=int(input('Do You Want To See The Text Info?(0=no / 1=yes):'))
        match second_question:
            case 0:
                print('Ok Have A Nice Day')
                os._exit(0)
            case 1:
                print(f'Great \n The Text Is:{my_json_file['verses'][0]['text']}')
                third_question=int(input('Do You Want To Send This To Your GF Or Maybe BF Or A Person?(0=no,1=yes):'))
                try:
                    match third_question:
                        case 0:
                            print('Ok Have A Nice Day My Friend')
                            os._exit(0)
                        case 1:
                            fourth_question=input('Please Enter The Reciever Phone Number:')
                            if(fourth_question.startswith('0')):
                                try:
                                    sms_sender()
                                except:
                                    pass
                            else:
                                print('The Phone Number Is Invalid Please Try Again Later!')
                                os._exit()
                        case _:
                            print('Invalid Input Please Try Again Later!')
                            os._exit()
                except:
                    print('Invalid Input Please Try Again Later!')
                    os._exit(0)
            case _:
                print('Invalid Input Please Try Again!')
                os._exit(0)
    except:
        print('Invalid Input Please Try Again!')
        os._exit(0)
edit_data()
