dict=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shift=5
new_dict={}
for letter in dict:
    if dict.index(letter)<=20:
        new_dict[letter]=dict[dict.index(letter)+int(shift)]
    else:
        new_dict[letter]=dict[dict.index(letter)-21]
#print(new_dict)
plain_text=input("Please enter a sentence: ").lower()
print(plain_text)
temp_text=[]
for letter in plain_text:
    if letter in new_dict:
        x=new_dict.get(letter)
        temp_text.append(x)
    else:
        temp_text.append(letter)
#print(temp_text)
enc_text="".join(temp_text)
print(enc_text)
# add your code here
