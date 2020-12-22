import re 
pp_byr = []
pp_iyr = []
pp_eyr = []
pp_hgt = []
pp_hcl = []
pp_ecl = []
pp_pid = []
pp_cid = []

pp_count = 0
pp_byr.append('')
pp_iyr.append('')
pp_eyr.append('')
pp_hgt.append('')
pp_hcl.append('')
pp_ecl.append('')
pp_pid.append('')
pp_cid.append('')

with open("04_input.txt") as f:
  for line in f:
    l = line.strip('\n')
    if l=='':
      pp_count = pp_count+1
      pp_byr.append('')
      pp_iyr.append('')
      pp_eyr.append('')
      pp_hgt.append('')
      pp_hcl.append('')
      pp_ecl.append('')
      pp_pid.append('')
      pp_cid.append('')
    else:
      for pair in l.split(' '):
        if pair.split(':')[0]=='byr':
          pp_byr[pp_count]=pair.split(':')[1]
        if pair.split(':')[0]=='iyr':
          pp_iyr[pp_count]=pair.split(':')[1]
        if pair.split(':')[0]=='eyr':
          pp_eyr[pp_count]=pair.split(':')[1]
        if pair.split(':')[0]=='hgt':
          pp_hgt[pp_count]=pair.split(':')[1]
        if pair.split(':')[0]=='hcl':
          pp_hcl[pp_count]=pair.split(':')[1]
        if pair.split(':')[0]=='ecl':
          pp_ecl[pp_count]=pair.split(':')[1]
        if pair.split(':')[0]=='pid':
          pp_pid[pp_count]=pair.split(':')[1]
        if pair.split(':')[0]=='cid':
          pp_cid[pp_count]=pair.split(':')[1]

valid_passports = 0

for i in range(0, pp_count+1):
  if (pp_byr[i]!='') and (pp_iyr[i]!='') and (pp_eyr[i]!='') and (pp_hgt[i]!='') and (pp_hcl[i]!='') and (pp_ecl[i]!='') and (pp_pid[i]!=''):
    valid_passports = valid_passports + 1

print "\n\nPassport Count: " + str(pp_count)
print "Valid Passport Count: " + str(valid_passports)

