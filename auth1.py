#Decoding query
#auth 1
from socket import*
serv_addr="xxx" # xxx=self ip address
serv_port=8000
serv_sock=socket(AF_INET,SOCK_DGRAM)
serv_sock.bind((serv_addr,serv_port))
print("the server is ready to receive")
lookuptable={"1":"xxx","2":"66.254.124.62","3":"12.116.1.10"}#xxx=ip address of auth 2 
def bin_to_str(b):
    n=len(b)
    low=0
    high=8
    q=""
    for i in range(0,int(n/8)):
        ch=b[low:high:]
        ch_ascii=int(ch,2)
        low+=8
        high+=8
        q+=chr(ch_ascii)
    return q
def convert_to_16(tr_id):
    tr_id=bin(tr_id)
    tr_id=tr_id[2::]
    n=len(tr_id)
    for i in range(0,16-n):
        tr_id="0"+tr_id
    return tr_id
def str_to_bin(str):
    op=""
    for i in str:
        x=bin(ord(i))[2::]
        for j in range(0,8-len(x)):
            x="0"+x
        op+=x
    return op
def ip_to_bin(ip):
    arr=ip.split('.')
    print(arr)
    str=""
    for i in range(len(arr)):
        print(arr[i])
        x=bin(int(arr[i]))[2::]
        for j in range(0, 8 - len(x)):
            x = "0" + x
        str+=x
    print(str)
    return str
while 1:
    payload,client_addr=serv_sock.recvfrom(2048)
    payload=payload.decode()
    print("Got msg from ",client_addr)
    print(payload)
    identification=payload[:16:]
    flags=payload[16:32:]
    no_questions=payload[32:48:]
    question=payload[96::]
    len_question=len(question)
    flags_new="1000010000010000"
    no_answer_new=convert_to_16(1)
    #payload_new=identification+flags_new+no_questions+no_answer_new+convert_to_16(0)+convert_to_16(0)+question+str_to_bin(lookuptable[bin_to_str(question[0:len_question-32:])])
    #payload_new = identification + flags_new + no_questions + no_answer_new + convert_to_16(0) + convert_to_16(0) +question+ ip_to_bin(lookuptable[bin_to_str(question[0:len_question-32:].strip())])
    answer=ip_to_bin(lookuptable[bin_to_str(question[0:len_question-32:]).split('/')[1]])
    payload_new = identification + flags_new + no_questions + no_answer_new + convert_to_16(0) + convert_to_16(0) + question + answer
    
    serv_sock.sendto(payload_new.encode(), client_addr)
