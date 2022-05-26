# 해시
def solution(phone_book):
  phone_hash = {}
    
   for phone_num in phone_book:
       phone_hash[phone_num] = 1
    
   for phone_num in phone_book:
       temp = ''
       for number in phone_num:
           temp += number
           if temp in phone_hash and temp != phone_num:
               return False
   return True

# loop startswith
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False 
    return True
