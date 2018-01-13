from random import randint

ok   = "•"
ng   = "‣"
new  = "◦"
ab   = "※"
sos  = "Ŷ"
cl   = "ƈ"
abc  = "Ɔ"
cool = "Ť"
tm   = "ƌ"

special_case_replace_dictionary = {
    "cool": cool,
    "ok"  : ok,
    "ng"  : ng,
    "new" : new,
    "abc" : abc,
    "ab"  : ab,
    "sos" : sos,
    "cl"  : cl,
    "tm"  : tm
}

d_s = {
    '1': [":one:"],
    '2': [":two:"],
    '3': [":three:"],
    '4': [":four:"],
    '5': [":five:"],
    '6': [":six:"],
    '7': [":seven:"],
    '8': [":eight:"],
    '9': [":nine:"],
    '0': [":zero:"],
    'a': [":regional_indicator_a:", ":a:"],
    'b': [":regional_indicator_b:", ":b:"],
    'c': [":regional_indicator_c:", ":star_and_crescent:"],
    'd': [":regional_indicator_d:"],
    'e': [":regional_indicator_e:"],
    'f': [":regional_indicator_f:"],
    'g': [":regional_indicator_g:"],
    'h': [":regional_indicator_h:"],
    'i': [":regional_indicator_i:", ":information_source:"],
    'j': [":regional_indicator_j:"],
    'k': [":regional_indicator_k:"],
    'l': [":regional_indicator_l:"],
    'm': [":regional_indicator_m:", ":m:"],
    'n': [":regional_indicator_n:"],
    'o': [":regional_indicator_o:", ":o:", " :o2:"],
    'p': [":regional_indicator_p:"],
    'q': [":regional_indicator_q:"],
    'r': [":regional_indicator_r:"],
    's': [":regional_indicator_s:"],
    't': [":regional_indicator_t:"],
    'u': [":regional_indicator_u:"],
    'v': [":regional_indicator_v:"],
    'w': [":regional_indicator_w:"],
    'x': [":regional_indicator_x:", ":x:"],
    'y': [":regional_indicator_y:"],
    'z': [":regional_indicator_z:"],
    '!': [":exclamation:"],
    '?': [":question:"],
    ok : [":ok:"],
    ng : [":ng:"],
    new: [":new:"],
    ab : ["ab"],
    sos: ["sos"],
    cl : [":cl:"],
    abc: [":abc:"],
    cool:[":cool:"],
    tm:  [":tm:"]
}

print("Enter the sentence you would like to translate.")
continue_parse = True
total_parsed = ""
while (continue_parse):
    continue_parse = False

    s = input().lower()
    if s != "":
        continue_parse = True
        total_parsed += s + "\n"

# remove the last line break
total_parsed = total_parsed[:len(total_parsed) - 1]

for special_case in special_case_replace_dictionary:
    total_parsed = total_parsed.replace(special_case, special_case_replace_dictionary[special_case])

r_s = ""
for c in total_parsed:
    if c in d_s:
        choices = d_s[c]
        r_s += choices[randint(0, len(choices) - 1)] + " "
    else:
        r_s += (" " * 4) if c == " " else c

print(r_s :chipmunk:)
