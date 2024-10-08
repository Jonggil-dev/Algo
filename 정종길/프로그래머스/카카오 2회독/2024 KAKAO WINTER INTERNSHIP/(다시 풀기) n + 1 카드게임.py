def solution(coin, cards):
    
    answer = 0
    n = len(cards)
    idx = n // 3
    
    my_cards = set(cards[ : idx])
    get_cards = set()
    
    flag = True
    
    while flag:
        flag = False
        answer += 1
        
        for _ in range(2):
            if idx == n:
                return answer
            get_cards.add(cards[idx])
            idx += 1
            
        for card in my_cards:
            target = n + 1 - card
            if target in my_cards:
                my_cards.remove(card)
                my_cards.remove(target)
                flag = True
                break
            
            if coin >= 1 and target in get_cards:
                coin -= 1
                my_cards.remove(card)
                get_cards.remove(target)
                flag = True
                break
        
        if not flag and coin >= 2:
            for card in get_cards:
                target = n + 1 - card
                if target in get_cards:
                    coin -= 2
                    get_cards.remove(card)
                    get_cards.remove(target)
                    flag = True
                    break
    return answer