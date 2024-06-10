def solution(answers):
    answer = []
    
    # 수포자들의 답안 패턴
    patterns = [
        [1, 2, 3, 4, 5],               # 수포자 1의 패턴
        [2, 1, 2, 3, 2, 4, 2, 5],      # 수포자 2의 패턴
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 수포자 3의 패턴
    ]
    
    scores = [0,0,0]  # 각 수포자가 맞힌 문제 수를 저장하는 리스트
    
    # 주어진 answers배열을 순회하면서 각 수포자의 패턴과 비교
    # 수포자가 맞힌 문제 수를 계산
    # 정답 배열과 각 수포자의 답안 패턴 비교
    for i, answer in enumerate(answers):
        if answer == patterns[0][i % len(patterns[0])]:
            scores[0] += 1
        if answer == patterns[1][i % len(patterns[1])]:
            scores[1] += 1
        if answer == patterns[2][i % len(patterns[2])]:
            scores[2] += 1
        
    # 가장 높은 점수 찾기
    max_score = max(scores)
    
    
    # 가장 높은 점수를 받은 수포자 찾기 (여러 명일 경우 오름차순 정렬)
    result = []
    
    for i in range(len(scores)):
        if scores[i] == max_score:
            result.append(i + 1)  # 수포자는 1번부터 시작하므로 인덱스에 1을 더해줌
        
    
    return result