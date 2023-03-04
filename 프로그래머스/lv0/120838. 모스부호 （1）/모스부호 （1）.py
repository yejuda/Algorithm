def solution(letter):
    
    answer = ''
    
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    
    letter = letter.split()
    
    # for i in letter:
    #         a = morse.get(i)  # key로 value(값) 추출
    #         answer += a
    
    for i in letter:
        answer += morse[i]
            
    return answer