def solution(participant, completion):
    if len(set(participant)) == len(set(completion)):
        participant.sort()
        completion.sort()
        for name in participant:
            try:
                completion.remove(name)
            except:
                return name
    else:
        (answer,) = set(participant) - set(completion)
        return answer