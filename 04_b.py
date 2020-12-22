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
    this_valid = 1

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if (int(pp_byr[i]) < 1920) or (int(pp_byr[i]) > 2002):
      this_valid = 0

    if len(pp_byr[i])!=4:
      this_valid = 0


    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if (int(pp_iyr[i]) < 2010) or (int(pp_iyr[i]) > 2020):
      this_valid = 0

    if len(pp_iyr[i])!=4:
      this_valid = 0


    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if (int(pp_eyr[i]) < 2020) or (int(pp_eyr[i]) > 2030):
      this_valid = 0

    if len(pp_eyr[i])!=4:
      this_valid = 0


    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    unit = pp_hgt[i][-2:]
    value = pp_hgt[i][:-2]
    print value + ' ' + unit
    if (unit != 'cm') and (unit != 'in'):
      this_valid = 0
      print "Invalid HGT (units)"

    if (unit == 'cm'):
      if (int(value) < 150) or (int(value) > 193): 
        this_valid = 0
        print "Invalid HGT (cm range)"

    if (unit == 'in'):
      if (int(value) < 59) or (int(value) > 76):
        this_valid = 0
        print "Invalid HGT (in range)"


    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    pattern = re.compile("^#[a-z0-9]{6}$")
    if (pattern.match(pp_hcl[i])):
      dummy = 0
    else:
      this_valid = 0

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if (pp_ecl[i] == 'amb') or (pp_ecl[i] == 'blu') or (pp_ecl[i] == 'brn') or (pp_ecl[i] == 'gry') or (pp_ecl[i] == 'grn') or (pp_ecl[i] == 'hzl') or (pp_ecl[i] == 'oth'): 
      dummy = 0
    else:
      this_valid = 0

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pattern = re.compile("^[0-9]{9}$")
    if (pattern.match(pp_pid[i])):
      dummy = 0
    else:
      this_valid = 0

    # cid (Country ID) - ignored, missing or not.

    if (this_valid == 1):
      valid_passports = valid_passports + 1

print "\n\nPassport Count: " + str(pp_count)
print "Valid Passport Count: " + str(valid_passports)

