a='7'*40+'9'*40+'4'*50
while '49' in a or '97' in a or '47' in a:
    if '47' in a:
        a=a.replace('47','74',1)
    if '97' in a:
        a=a.replace('97','79',1)
    if '49' in a:
        a=a.replace('49','94',1)
print(a[24],a[70],a[104])