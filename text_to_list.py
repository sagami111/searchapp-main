import pykakasi


with open('search.txt', encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()

# ファイルの中身を出力してみる
print(lines)

l = []
now_alpha = "zzz"
now_num = ""

for i in range(len(lines)):
    if len(lines[i]) == 0:
        continue
    if lines[i][0] == '$':
        tyuuko_flag, Best_Hit_flag, new_flag = False, False, False

        now_alpha = lines[i][1]
        if "中古" in lines[i]:
            tyuuko_flag = True
        elif "BEST" in lines[i]:
            Best_Hit_flag = True
        else:
            new_flag = True   
        continue
    
    if len(lines[i]) == 2:
        if lines[i][0].isdigit() and lines[i][1].isdigit():
            now_num = lines[i]
            continue
        
    text = lines[i]  
    
    # インスタンス化
    kks = pykakasi.kakasi()

    # 変換
    result = kks.convert(text)
    
    text = list(text)
    re_text = []
    for j in range(len(text)):
        if text[j].isupper():
            re_text.append(chr(ord(text[j]) + 32))
            text[j] = chr(ord(text[j]) + 32)
            
            continue
        
        if not text[j] in [" ", "★", ",", ".", "'"]:
            re_text.append(text[j])
            
            
    text = "".join(text)
    re_text = "".join(re_text)
    
    if tyuuko_flag or (now_alpha == "F" and 0< int(now_num) < 10):
        lines[i] += "(中古)"
    elif Best_Hit_flag:
        lines[i] += ""
    elif new_flag:
        lines[i] += "(新品)"
    
    l.append([lines[i] + "_" + now_alpha + " " + now_num, lines[i] + " " + text + " " + ''.join([item['hira'] for item in result]) +  " " + ''.join([item['kunrei'] for item in result]) + " " + re_text])
    

print(f'const words = {l}')   

with open('output.txt', mode='w', encoding='utf-8') as f:
    f.write(f'const words = {l}')
        
         
    