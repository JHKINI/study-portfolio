import random
def get_user_choice(who):
    rsp=None
    if who=="user":
        while True:
            rsp=input("가위, 바위, 보 중에서 선택하세요: ")
            if rsp in ["가위","바위","보"]:
                break
            print("잘못된 입력입니다. 다시 입력해주세요.")
    else:  
        rsp= list_rsp[random.randint(0,2)]
    return rsp

def determine_winner_count_check(user_rsp, computer_rsp,winner_count_accumulator):
    winner = judgement[user_rsp][computer_rsp]
    if winner == "user":
        winner_count_accumulator["user"] = winner_count_accumulator["user"] + 1
        print("{}가 이겼습니다!({} winner_count: {})".format(user_rsp, winner, winner_count_accumulator['user']))
        
    elif winner == "computer":
        winner_count_accumulator["computer"] = winner_count_accumulator[winner]+1
        print("{}가 이겼습니다!({} winner_count: {})".format(computer_rsp, winner, winner_count_accumulator['computer']))
    else:
        print("이번판은 무승부예요")
    return winner_count_accumulator
winner_count={"user":0, "computer":0}
list_rsp={0:'가위', 1:'바위', 2:'보'}
judgement = {
  '가위': {'가위': None, '바위': 'computer', '보': 'user'},
    '바위': {'가위': 'user', '바위': None, '보': 'computer'},
    '보': {'가위': 'computer', '바위': 'user', '보': None},
}
while True:
    user_choice = get_user_choice("user")
    computer_choice = get_user_choice("computer")
    winner_count=determine_winner_count_check(user_choice, computer_choice, winner_count)
    if winner_count["user"] >= 3 or winner_count["computer"] >= 3:
        break